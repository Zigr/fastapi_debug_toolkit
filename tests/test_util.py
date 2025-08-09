from fastapi_debug_toolkit.debugctl.util import get_project_root


def test_get_project_root():
    exppected = "ai-agent"
    project_root = get_project_root()
    assert project_root == exppected
