from fastapi_debug_toolkit.debugctl.cli import app
from fastapi_debug_toolkit.util import is_docker
from typer.testing import CliRunner

runner = CliRunner()


def test_local_get_status():
    if is_docker():
        pass

    result = runner.invoke(app, ["status"])
    assert result.exit_code == 0
    assert "ENABLED" in result.output or "DISABLED" in result.output


def test_docker_get_status():
    if not is_docker():
        pass

    result = runner.invoke(app, ["status"])
    assert result.exit_code == 0
    assert "ENABLED" in result.output or "DISABLED" in result.output


def test_local_enable():
    if is_docker():
        pass
    result = runner.invoke(app, ["enable"])
    assert result.exit_code == 0
    assert "Debug routes enabled" in result.output


def test_docker_enable():
    if not is_docker():
        pass
    result = runner.invoke(app, ["enable"])
    assert result.exit_code == 0
    assert "IN_DOCKER" in result.output


def test_local_disable():
    if is_docker():
        pass
    result = runner.invoke(app, ["disable"])
    assert result.exit_code == 0
    assert "Debug routes disabled" in result.output


def test_docker_disable():
    if not is_docker():
        pass
    result = runner.invoke(app, ["disable"])
    assert result.exit_code == 0
    assert "IN_DOCKER" in result.output
