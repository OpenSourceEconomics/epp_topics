from pathlib import Path

ROOT = Path(__file__).parent

BLD = ROOT / "bld"


def task_write_hello(produces=BLD / "hello.txt"):
    produces.write_text("Hello")
