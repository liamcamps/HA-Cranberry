# Cranberry Canvas theme for Home Assistant

A warm, calm theme for Home Assistant, light and dark, where every colour means one thing.
It themes the dashboard and Home Assistant's own interface: buttons, dialogs, forms, chips,
tooltips, tables, the code editor and graphs.

Made to go with the [Cranberry Canvas cards](https://github.com/liamcamps/HA-Cranberry-cards),
and works without them too.

## Palette

| Colour | | Means |
| --- | --- | --- |
| Cranberry | `#591E21` | The house: lights and scenes on, selected, the home card |
| Olive | `#514718` | Running and fine: heating, playing, locked, armed |
| Harbour | `#40606A` | Cool and wet: cooling, rain, water, info |
| Ochre | `#8B621F` | Caution: warnings, drying |
| Quail | `#7D8689` | Off and idle |
| Brick | `#A8352F` | Only when something needs you |
| Mist, Sun | `#9CC3D6`, `#F0B85A` | Weather data only |

| Neutrals | Light | Dark |
| --- | --- | --- |
| Page | Canvas `#E3DDCF` | Night `#1B1513` |
| Cards | Paper `#EEE9DF` | Ember `#2E2422` |
| Text | Ink `#231C1A` | Cream `#F2ECE0` |
| Secondary text | Stone `#675F5A` | Taupe `#B5ABA0` |

Fonts: Fraunces for large numbers and the clock, Figtree for everything else. The Cranberry
home card loads them; without it, add them as a resource (see the top of the theme file).

## Install

### Through HACS

1. HACS → ⋮ → **Custom repositories** → `https://github.com/liamcamps/HA-Cranberry`,
   type **Theme**.
2. Search for **Cranberry Canvas theme** and download it. HACS puts it in `/config/themes/`
   and shows an update whenever a new release is published.
3. Once: make sure `configuration.yaml` has

   ```yaml
   frontend:
     themes: !include_dir_merge_named themes
   ```

   and restart Home Assistant.
4. Profile → Theme → **Cranberry Canvas**.

After an update, run the action `frontend.reload_themes` (or restart) to see it.

### By hand

Copy `themes/cranberry_canvas.yaml` to `/config/themes/`, then steps 3 and 4 above.

## Tokens

Every colour the [Cranberry cards](https://github.com/liamcamps/HA-Cranberry-cards) use comes
from these tokens, so this file is the one place to change a colour. They work in card-mod and
your own cards too.

| Group | Tokens |
| --- | --- |
| Accents, for small marks (lighter in dark mode) | `cc-cranberry`, `cc-olive`, `cc-quail`, `cc-brick`, `cc-harbour`, `cc-ochre-tone` |
| Fills, for whole coloured cards (the same in both modes) | `cc-fill-cranberry`, `cc-fill-olive`, `cc-fill-harbour`, `cc-fill-ochre`, `cc-fill-quail`, `cc-fill-ember` |
| Text on fills and on cream | `cc-cream`, `cc-cream-muted`, `cc-on-cream`, `cc-shadow`, `cc-brick-text` (brick as text on a card) |
| Neutrals | `cc-canvas`, `cc-paper`, `cc-ember`, `cc-panel`, `cc-ink` |
| Weather | `cc-sun`, `cc-mist`, `cc-taupe`, `cc-temp-freezing`, `cc-temp-cold`, `cc-temp-mild`, `cc-temp-warm`, `cc-temp-hot` |
| Bins (per mode) | `cc-bin-green`, `cc-bin-paper`, `cc-bin-plastic`, `cc-bin-rest` |
| Calendars, in the order they are picked | `cc-calendar-1` … `cc-calendar-5` |
| The home card | `cranberry-home-card-background` |
| Corners | `cc-r-card` (24px), `cc-r-ctl` (12px), `cc-r-chip` (8px) |

## Contrast

`python3 tools/contrast.py` checks every colour pair the cards use, in light and dark: text
against what it sits on needs 4.5:1, icons, dots and bars 3:1. CI runs it on every change.
