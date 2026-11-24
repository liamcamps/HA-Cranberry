# Changelog

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
