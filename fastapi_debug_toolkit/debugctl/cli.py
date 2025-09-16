from pathlib import Path

import typer
from rich import print
from rich.panel import Panel

from fastapi_debug_toolkit.util import (
    get_backend_folder,
    is_debug_routes_set,
    is_docker,
    read_env_file_setting,
    write_env_file_setting,
)

"""CLI to manage FastAPI debug routes.
This CLI allows you to enable or disable debug routes in your FastAPI application.
It reads and writes to a .env file in the current directory to manage the state of debug routes.
"""
app = typer.Typer(help="CLI to manage FastAPI debug routes")

backend: Path = get_backend_folder()
# print(backend)

ENV_FILE = Path(backend) / ".env"


def update_flag(value: bool) -> int:
    if is_docker():
        print(
            "[bold magenta]Warning![/bold magenta] Perhaps, running in Docker environment."
        )
        written = 0
    else:
        new_lines = write_env_file_setting(
            ENV_FILE, "DEBUG_ROUTES_ENABLED", "true" if value else "false"
        )
        written = ENV_FILE.write_text("\n".join(new_lines) + "\n")
    return written


@app.command()
def enable():
    """Enable debug routes"""
    result = update_flag(True)
    print(
        Panel(
            f"{ '✅ Debug routes enabled. ⚠️ Will take effect after server reload.' if result > 0 else ' ⚠️ IN_DOCKER. Swithcing routes debug is impossible.' }",
            title="Debugctl",
            subtitle="enable",
            expand=False,
        )
    )


@app.command()
def disable():
    """Disable debug routes"""
    result: int = update_flag(False)
    print(
        Panel(
            f"{ '❌ Debug routes disabled. ⚠️ Will take effect after server reload.' if result > 0 else ' ⚠️ IN_DOCKER. Swithcing routes debug is impossible.' }",
            title="Debugctl",
            subtitle="disable",
            expand=False,
        )
    )


@app.command()
def status():
    """Show current debug route status"""
    if is_docker():
        print(
            f"Perhaps, running in Docker environment. IN_DOCKER Enable/disable is not allowed. Debugging routes allowed: {is_debug_routes_set()}"
        )
        status = is_debug_routes_set()
    else:
        value = read_env_file_setting(ENV_FILE, "DEBUG_ROUTES_ENABLED")
        status = True if value.lower() == "true" else False
    print(
        Panel(
            f"🔍 Debug routes currently: {'✅ ENABLED' if status  else '❌ DISABLED'}",
            title="Debugctl",
            subtitle="status",
            expand=False,
        )
    )
