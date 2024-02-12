import subprocess
from pathlib import Path
import os

import click
from livereload import Server

@click.command()
@click.argument("pathsource", default=".", type=Path)
@click.option("-o", "--outputdir", default="_build/html", type=Path, show_default=True)
@click.option("-p", "--port", default=8002, type=click.INT, show_default=True)
def main(pathsource: Path, outputdir: Path, port: int):
    """
    Script to serve a jupyter-book site, which rebuilds when files have
    changed and live-reloads the site. Basically `mkdocs serve`
    but for jupyter-book. Use by calling `python jb-serve.py [OPTIONS] [PATH_SOURCE]`.

    \b
    Args
    ----
    PATHSOURCE: Directory in `jb build <dir>`
    outputdir: Directory where HTML output is generated. `jb` defaults to `_build/html`
    port: Port to host the webserver. Default is 8002

    \b
    Refs
    ----
    + https://github.com/executablebooks/sphinx-autobuild/issues/99#issuecomment-722319104
    + mkdocs docs on github
    """

    def build():
        subprocess.run(["jb", "clean", pathsource])
        subprocess.run(["jb", "build", pathsource])

    # Build if not exists upon startup
    if not os.path.exists(outputdir):
        build()

    server = Server()

    # Globbing for all supported file types under jupyter-book
    # Ignore unrelated files
    #server.watch(pathsource / "**/*.md", build)
    #server.watch(pathsource / "**/*.ipynb", build)
    #server.watch(pathsource / "**/*.rst", build)
    server.watch(pathsource / "./content/IT/*.myst.md", build)
    #server.watch(pathsource / "_config.yml", build)
    #server.watch(pathsource / "_toc.yml", build)

    server.serve(root=outputdir, port=port)

if __name__ == "__main__":
    main()
