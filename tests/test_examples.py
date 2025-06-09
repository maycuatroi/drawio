import runpy
import subprocess
import sys
from pathlib import Path


def test_examples_run(monkeypatch):
    repo_root = Path(__file__).resolve().parents[1]
    subprocess.check_call([sys.executable, "-m", "pip", "install", str(repo_root)])

    class DummyBrowser:
        def __init__(self, *args, **kwargs):
            pass

        def render(self, *args, **kwargs):
            return None

        def export(self, output_file: str):
            return output_file

    monkeypatch.setattr(
        "drawio.entities.drawio_browser.DrawIOBrowser", DummyBrowser
    )
    monkeypatch.setattr(
        "drawio.entities.renderers.drawio_render.DrawIOBrowser", DummyBrowser
    )
    monkeypatch.setattr("builtins.input", lambda *args, **kwargs: "")

    runpy.run_path(repo_root / "examples" / "draw-flow-diagrams.py", run_name="__main__")
    runpy.run_path(repo_root / "examples" / "mermaid-to-drawio.py", run_name="__main__")
    runpy.run_path(repo_root / "examples" / "complex-example.py", run_name="__main__")

