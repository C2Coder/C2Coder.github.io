from __future__ import annotations

import json
import sys
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


ROOT = Path(__file__).resolve().parent
TEMPLATES = ROOT / "templates"
CONTENT = ROOT / "content"
DIST = ROOT / "dist"


def load_json(name: str):
    with open(CONTENT / name, "r", encoding="utf-8") as handle:
        return json.load(handle)


def project_href(slug: str) -> str:
    return f"/projects/{slug}/"


def build() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True, exist_ok=True)

    env = Environment(loader=FileSystemLoader(TEMPLATES))
    data = load_json("site.json")
    projects = load_json("projects.json")
    skills = load_json("skills.json")
    setup = load_json("setup.json")

    site = dict(data["site"])
    site["shared"] = data["shared"]

    html = env.get_template("index.html").render(
        site=site,
        projects=projects,
        skills=skills,
        setup=setup,
        project_href=project_href,
    )
    (DIST / "index.html").write_text(html, encoding="utf-8")

    for project in projects["projects"]:
        slug = project.get("slug")
        if not slug:
            continue
        page_dir = DIST / "projects" / slug
        page_dir.mkdir(parents=True, exist_ok=True)
        page_html = env.get_template("project.html").render(
            site=site,
            project=project,
            detail=project["detail"],
            project_href=project_href,
        )
        (page_dir / "index.html").write_text(page_html, encoding="utf-8")

    c_name = ROOT / "CNAME"
    if c_name.exists():
        shutil.copy2(c_name, DIST / "CNAME")

    assets = ROOT / "assets"
    if assets.exists():
        shutil.copytree(assets, DIST / "assets", dirs_exist_ok=True)


def serve() -> None:
    from livereload import Server

    build()
    server = Server()
    server.watch(str(TEMPLATES / "*.html"), build)
    server.watch(str(CONTENT / "*.json"), build)
    if (ROOT / "assets").exists():
        server.watch(str(ROOT / "assets" / "**"), build)
    server.serve(root=str(DIST), host="0.0.0.0", port=8000)


if __name__ == "__main__":
    if "--serve" in sys.argv:
        serve()
    else:
        build()
