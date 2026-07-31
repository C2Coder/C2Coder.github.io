# c2coder.eu

Source for [c2coder.eu](https://c2coder.eu) - my personal site: projects, skills,
and the gear/setup I work with. A static site built by a small Python + Jinja2
generator, deployed to GitHub Pages.

The photography portfolio at [photo.c2coder.eu](https://photo.c2coder.eu) is a
sibling site (`../photo.c2coder.eu` in this checkout) built the same way - see
`DESIGN.md` for the shared visual language between the two.

## Layout

```
content/
  site.json      # site chrome: nav, hero copy, section intros, contact block
  projects.json  # project cards on the homepage + full /projects/<slug>/ pages
  skills.json    # "what I do well" inventory list
  setup.json     # "how I work" inventory list (daily rig, servers, etc.)
templates/
  index.html     # homepage
  project.html   # per-project detail page, one per project with a "detail" block
assets/          # favicon, CSS (copied into dist/ as-is)
build.py         # renders content/*.json through templates/*.html into dist/
```

## Content model

- `content/site.json` has a `shared` block (contact info, footer quote) reused
  across pages, and a `site` block (nav, hero, section copy).
- Each entry in `content/projects.json` → `projects` is a project card. External
  projects just need `title`, `description`, `tags`, `link`. Projects with their
  own write-up need a `slug` **and** a `detail` object
  (`{ summary, sections: [{heading, body}], specs: [{key, value}] }`, optionally
  `files: [{name, href}]`) - that's what generates `/projects/<slug>/`. A project
  with a `slug` but no `detail` is skipped (with a warning) rather than breaking
  the build.
- `skills.json` / `setup.json` are both `{ title, items: [...] }` groups rendered
  as label → value rows.

## Build & run

Requires Python 3 and the packages in `requirements.txt` (`Jinja2`, `livereload`).

```
make build       # renders content/*.json + templates/*.html -> dist/
make serve       # build once, then serve dist/ on :8000
make serve-live  # build + rebuild on every content/template/asset change, serve on :8000
```

Equivalent to `python build.py` / `python build.py --serve`.

## Deployment

Pushing to `main` runs `.github/workflows/pages.yml`, which builds the site and
publishes `dist/` to GitHub Pages. The custom domain (`c2coder.eu`) is set via
the `CNAME` file at the repo root, which `build.py` copies into `dist/` on every
build.
