import os
from pathlib import Path

from fastapi_debug_toolkit.util import get_project_root


def test_get_project_root():
    exppected = "ai-agent"
    project_root: Path = get_project_root()
    path_str: str = os.fspath(project_root)
    head, tail = os.path.split(path_str)
    print(f"Last comp: {tail}")
    assert tail == exppected
