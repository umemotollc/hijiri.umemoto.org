# hijiri

## Slides

- [2026-03-01 wikimedia25 (source)](./_slides_src/2026-03-01-wikimedia25.md)
- [2026-03-01 wikimedia25 (HTML slides)](./slides/2026-03-01-wikimedia25.html)
- [2026-11-05 dentsudai (source)](./_slides_src/2026-11-05-dentsudai.md)
- [2026-11-05 dentsudai (HTML slides)](./slides/2026-11-05-dentsudai.html)

## Build slides

1. Install Marp CLI (one time): `npm install -g @marp-team/marp-cli`
2. Export HTML: `marp ./_slides_src/2026-03-01-wikimedia25.md -o ./slides/2026-03-01-wikimedia25.html`

## Commit and push (slides)

### Recommended (commit source only)

The HTML under `slides/` is generated during the GitHub Pages deployment, so
you only need to commit the source and assets. The generated files are included
in the Pages artifact and do not need to be committed.

```bash
git status -sb
git add _slides_src/ assets/
git commit -m "Update slide source"
git push
```

### If you generated HTML locally (optional)

If you generated `slides/` locally and want to commit it, you must force-add it
because `slides/` is ignored.

```bash
git status -sb
git add _slides_src/ assets/ -f slides/2026-03-01-wikimedia25.html
git commit -m "Update slides"
git push
```