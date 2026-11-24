"""Checks that every colour pair the Cranberry cards use is readable, in both modes.

Text needs 4.5:1 against what it sits on (WCAG AA); icons, dots, bars and other marks 3:1.
Run: python3 tools/contrast.py   (exits with 1 when a pair fails; CI runs it on every push)
"""
import re
import sys
import yaml

THEME = 'themes/cranberry_canvas.yaml'
TEXT, MARK = 4.5, 3.0

# (what sits on top, what it sits on, minimum, where you see it)
PAIRS = [
    # Home Assistant's own text on cards and the page
    ('primary-text-color', 'card-background-color', TEXT, 'text on a card'),
    ('secondary-text-color', 'card-background-color', TEXT, 'secondary text on a card'),
    ('primary-text-color', 'primary-background-color', TEXT, 'text on the page'),
    ('secondary-text-color', 'primary-background-color', TEXT, 'secondary text on the page'),
    # cream text on every coloured card
    ('cc-cream', 'cc-fill-cranberry', TEXT, 'the home card, active scenes'),
    ('cc-cream-muted', 'cc-fill-cranberry', TEXT, 'secondary text on the home card'),
    ('cc-cream', 'cc-fill-olive', TEXT, 'heating, music playing, a pressed extra button'),
    ('cc-cream', 'cc-fill-harbour', TEXT, 'cooling'),
    ('cc-cream', 'cc-fill-ochre', TEXT, 'drying'),
    ('cc-cream', 'cc-fill-quail', TEXT, 'fan, off'),
    ('cc-cream', 'cc-fill-ember', TEXT, 'idle thermostat'),
    ('cc-cream', 'cc-brick', TEXT, 'a card that needs you'),
    # on cream: chips and menus
    ('cc-brick', 'cc-cream', TEXT, 'the problem chip on the home card'),
    ('cc-fill-cranberry', 'cc-cream', TEXT, 'the bins chip on the home card'),
    ('cc-on-cream', 'cc-cream', TEXT, 'thermostat menus, Turn on'),
    # the weather on the home card
    ('cc-temp-freezing', 'cc-fill-cranberry', TEXT, 'temperatures below 0°'),
    ('cc-temp-cold', 'cc-fill-cranberry', TEXT, 'temperatures around 3°'),
    ('cc-temp-mild', 'cc-fill-cranberry', TEXT, 'temperatures around 9°'),
    ('cc-temp-warm', 'cc-fill-cranberry', TEXT, 'temperatures around 14°'),
    ('cc-temp-hot', 'cc-fill-cranberry', TEXT, 'temperatures above 20°'),
    ('cc-mist', 'cc-fill-cranberry', MARK, 'rain bars, rain icons'),
    ('cc-sun', 'cc-fill-cranberry', MARK, 'the sun icon'),
    ('cc-taupe', 'cc-fill-cranberry', MARK, 'clouds at dusk, fog'),
    # accents, where the cards use them: behind cream text, as text on cream, as marks on a card
    ('cc-cream', 'cc-cranberry', TEXT, 'today in the calendar, a lit room, New event'),
    ('cc-cranberry', 'cc-cream', TEXT, 'cranberry text on cream buttons'),
    ('cc-olive', 'card-background-color', MARK, 'olive icons: home, running'),
    ('cc-quail', 'card-background-color', MARK, 'icons of things that are off'),
    ('cc-rain', 'card-background-color', TEXT, 'rain on a card: the weather card’s chance of rain'),
    ('cc-ochre-tone', 'card-background-color', MARK, 'the weather card: sun icons, temperature bars'),
    ('cc-brick-text', 'card-background-color', TEXT, 'brick text on a card: errors, Delete'),
    # event titles on their calendar's tint (24% of the accent over the card)
    (('mix', 'cc-cranberry', 24, 'card-background-color'), None, TEXT, 'event on the first calendar tint'),
    (('mix', 'cc-olive', 24, 'card-background-color'), None, TEXT, 'event on the second calendar tint'),
    (('mix', 'cc-harbour', 24, 'card-background-color'), None, TEXT, 'event on the third calendar tint'),
    (('mix', 'cc-ochre-tone', 24, 'card-background-color'), None, TEXT, 'event on the fourth calendar tint'),
    (('mix', 'cc-quail', 24, 'card-background-color'), None, TEXT, 'event on the fifth calendar tint'),
    # bins and calendars
    ('cc-bin-green', 'card-background-color', MARK, 'green bin'),
    ('cc-bin-paper', 'card-background-color', MARK, 'paper bin'),
    ('cc-bin-plastic', 'card-background-color', MARK, 'plastic bin'),
    ('cc-bin-rest', 'card-background-color', MARK, 'residual bin'),
    ('cc-calendar-1', 'card-background-color', MARK, 'first calendar'),
    ('cc-calendar-2', 'card-background-color', MARK, 'second calendar'),
    ('cc-calendar-3', 'card-background-color', MARK, 'third calendar'),
    ('cc-calendar-4', 'card-background-color', MARK, 'fourth calendar'),
    ('cc-calendar-5', 'card-background-color', MARK, 'fifth calendar'),
]


def load():
    data = yaml.safe_load(open(THEME))
    theme = next(iter(data.values()))
    base = {k: v for k, v in theme.items() if k != 'modes' and isinstance(v, str)}
    return {m: dict(base, **theme['modes'][m]) for m in ('light', 'dark')}


def resolve(tokens, name, seen=()):
    v = str(tokens[name]).strip()
    m = re.fullmatch(r'var\(--([\w-]+)(?:,\s*(.+))?\)', v)
    if m:
        if m.group(1) in seen:
            raise ValueError('loop at ' + name)
        if m.group(1) in tokens:
            return resolve(tokens, m.group(1), seen + (name,))
        return m.group(2)
    return v


def rgb(v):
    v = v.strip()
    if v.startswith('#'):
        h = v[1:]
        if len(h) == 3:
            h = ''.join(c * 2 for c in h)
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    m = re.fullmatch(r'rgba?\(([^)]+)\)', v)
    if m:
        return tuple(int(float(x)) for x in m.group(1).split(',')[:3])
    raise ValueError('not a colour: ' + v)


def lum(c):
    f = lambda x: x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4
    r, g, b = (f(x / 255) for x in c)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a, b):
    x, y = sorted((lum(a), lum(b)), reverse=True)
    return (x + 0.05) / (y + 0.05)


def main():
    modes = load()
    failed = 0
    for mode, tokens in modes.items():
        print(f'{mode} mode')
        for fg, bg, need, where in PAIRS:
            if isinstance(fg, tuple):
                # an event title (the card's text colour) on a tint: the accent mixed into the card
                _, acc, pct, base = fg
                a, b = rgb(resolve(tokens, acc)), rgb(resolve(tokens, base))
                tint = tuple(round(x * pct / 100 + y * (1 - pct / 100)) for x, y in zip(a, b))
                r = ratio(rgb(resolve(tokens, 'primary-text-color')), tint)
                label = f'text on {acc} {pct}%'
            else:
                r = ratio(rgb(resolve(tokens, fg)), rgb(resolve(tokens, bg)))
                label = f'{fg} on {bg}'
            ok = r >= need
            failed += not ok
            print(f"  {'ok  ' if ok else 'FAIL'} {r:5.2f} (needs {need}) {label}: {where}")
    print(f'{failed} pair(s) too low' if failed else 'every pair is readable')
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
