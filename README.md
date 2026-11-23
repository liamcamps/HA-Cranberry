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
| Ochre | `#8E6420` | Caution: warnings, drying |
| Quail | `#7D8689` | Off and idle |
| Brick | `#A8352F` | Only when something needs you |
| Mist, Sun | `#9CC3D6`, `#F0B85A` | Weather data only |

| Neutrals | Light | Dark |
| --- | --- | --- |
| Page | Canvas `#E3DDCF` | Night `#1B1513` |
| Cards | Paper `#EEE9DF` | Ember `#2E2422` |
| Text | Ink `#231C1A` | Cream `#F2ECE0` |
| Secondary text | Stone `#6E6560` | Taupe `#B5ABA0` |

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

## Tokens for your own cards

Both modes define `--cc-cranberry`, `--cc-olive`, `--cc-quail`, `--cc-brick`, `--cc-harbour`,
`--cc-ochre-tone`, `--cc-canvas`, `--cc-paper`, `--cc-ember`, `--cc-panel` and `--cc-ink`,
for card-mod or your own cards.
