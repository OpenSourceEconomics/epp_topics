from pathlib import Path

ROOT = Path(__file__).parent

BLD = ROOT / "bld"


def task_write_world(produces=BLD / "world.txt"):
    produces.write_text("world!")
