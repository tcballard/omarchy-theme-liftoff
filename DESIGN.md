# Liftoff

A dark, launch-inspired theme for Omarchy Quattro. The supplied photograph remains the centrepiece; the interface picks up its blue shadow, warm white vapour, copper exhaust and open sky.

| Role | Colour | Intent |
| --- | --- | --- |
| Background | #151E26 | Deep blue-charcoal, avoiding flat black |
| Raised surface | #253440 | Cool smoke-blue separation |
| Foreground | #ECE5D8 | Warm cloud white |
| Focus / accent | #F3B77B | Exhaust amber |
| Selection | #334D5D | Muted sky-blue field |
| Secondary text | #A2ACAE | Readable smoke grey |
| Blue | #7BBCE0 | Daylight sky |
| Cyan | #8BC8D0 | Coastal water |
| Warning | #EAD093 | Pale warm yellow |
| Error | #EF8D80 | Coral, separate from amber focus |
| Success | #A9C59A | Coastal marsh green |

Closest inspected built-in: Nord, at omacom/omarchy commit e332dc975d5f635294c497ebb54feb98dc3d89eb. Liftoff changes the whole hierarchy: substantially darker surfaces, warm rather than cool whites, amber rather than blue focus, and brighter sky/sea ANSI colours. It is not a two-accent Nord recolour.

All shell and supported app configuration is palette-derived through Omarchy's templates. No full shell override freezes upstream tokens. Native typography, spacing, disabled-state handling and interactions remain inherited. Fonts and spacing are intentionally unchanged. These defaults include opaque bar, menu and notification surfaces, while launcher and lock surfaces require live contrast checks over the photograph.

Target source: Quattro e332dc975d5f635294c497ebb54feb98dc3d89eb, matching the v0.2.1 contract. Installed target version is unknown. No local user templates were available for inspection.

## Live acceptance

Record omarchy-version and display scale. Verify bar in both orientations, launcher, menus, notifications, lock input, terminal ANSI/selection, editor syntax and GTK controls. Inspect focus, selected, hover and disabled states. Check the centred rocket on 16:9, 16:10 and ultrawide displays; portrait crops and lock controls may obscure the rocket. Exercise switch away/back, restart/login and the Git-installed path once a repository exists. Restore the original theme/background after a temporary test. Capture preview.png only from that live desktop.
