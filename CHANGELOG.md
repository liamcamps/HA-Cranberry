# Changelog

## 4.2.0 (2026-11-24)

- **Contrast check:** `tools/contrast.py` checks every colour pair the cards use, in both modes: text needs 4.5:1, icons, dots and bars 3:1. CI runs it, so a colour that makes something unreadable can't be released. It found and fixed:
  - **Stone** (secondary text, light mode) #6E6560 → #675F5A, readable on the page as well as on cards.
  - **Ochre** #8B621F (was #8E6420): cream text on the drying thermostat now passes.
  - **Calendar colours 3–5 in light mode** are the deep harbour, ochre and quail; the light versions were too pale on paper. Dark mode keeps the light ones.
  - **New `cc-brick-text`**: brick as text on a card ("Delete", errors). Lighter in dark mode (#E06B62), where plain brick was 2.3:1.

## 4.1.0 (2026-11-24)

- Every colour the Cranberry cards use is now a theme token, so the theme is the one place to change them. New tokens, in both modes:
  - **Fills** for whole coloured cards: `cc-fill-cranberry`, `cc-fill-olive`, `cc-fill-harbour`, `cc-fill-ochre`, `cc-fill-quail`, `cc-fill-ember`.
  - **Text on them:** `cc-cream`, `cc-cream-muted` and `cc-on-cream`, plus `cc-shadow`.
  - **Weather:** `cc-sun`, `cc-mist`, `cc-taupe`, and the temperature line from `cc-temp-freezing` through `cc-temp-cold`, `cc-temp-mild` and `cc-temp-warm` to `cc-temp-hot`.
  - **Bins**, lighter in dark mode: `cc-bin-green`, `cc-bin-paper`, `cc-bin-plastic`, `cc-bin-rest`.
  - **Calendars**, in the order they are picked: `cc-calendar-1` … `cc-calendar-5`.
- `cranberry-home-card-background` now points at `cc-fill-cranberry`.
- The colours themselves are unchanged. Needs Cranberry Canvas cards 2.33.0 or newer to use them; older cards keep working.

## 4.0.0 (2026-11-23)

- The theme has its own repository, so HACS installs and updates it. The cards moved to
  [HA-Cranberry-cards](https://github.com/liamcamps/HA-Cranberry-cards).
- The palette is official, and every colour means one thing:
  - **Cranberry** is the house.
  - **Olive** is running.
  - **Harbour** #40606A is cool and wet.
  - **Ochre** #8E6420 is caution.
  - **Quail** is off.
  - **Brick** is only for problems.
- Light-mode cards are Paper #EEE9DF, lighter than the page.
- Secondary text is warm: Stone #6E6560 in light mode, Taupe #B5ABA0 in dark mode. Dark-mode text is Cream #F2ECE0.
- Cool and info states use Harbour; warnings use Ochre. Brick is the same in both modes.
- New tokens `cc-harbour`, `cc-ochre-tone`, `cc-paper` and `cc-ember`.
