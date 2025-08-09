from pathlib import Path

import typer
from fastapi import HTTPException

from fastapi_debug_toolkit.debugctl.util import get_project_root

"""CLI to manage FastAPI debug routes.
This CLI allows you to enable or disable debug routes in your FastAPI application.
It reads and writes to a .env file in the current directory to manage the state of debug routes.
"""
project_root: Path = get_project_root()
# print(project_root)

CONFIG_FILE = Path(project_root) / ".env"
print(f"Config file: {CONFIG_FILE}")
# load_dotenv(dotenv_path=CONFIG_FILE, override=True)
app = typer.Typer(help="CLI to manage FastAPI debug routes")


def update_flag(value: bool):
    if not CONFIG_FILE.exists():
        print(
            f"Config file does not exist. Creating a new one at {CONFIG_FILE}.",
            CONFIG_FILE,
        )
    lines = CONFIG_FILE.read_text().splitlines()
    updated = False
    new_lines = []

    for line in lines:
        if line.startswith("DEBUG_ROUTES_ENABLED="):
            new_lines.append(f"DEBUG_ROUTES_ENABLED={'true' if value else 'false'}")
            updated = True
        else:
            new_lines.append(line)

    if not updated:
        new_lines.append(f"DEBUG_ROUTES_ENABLED={'true' if value else 'false'}")

    CONFIG_FILE.write_text("\n".join(new_lines) + "\n")


@app.command()
def enable():
    """Enable debug routes"""
    update_flag(True)
    typer.echo("✅ Debug routes enabled.")


@app.command()
def disable():
    """Disable debug routes"""
    update_flag(False)
    typer.echo("❌ Debug routes disabled.")


@app.command()
def status():
    """Show current debug route status"""

    if not CONFIG_FILE.exists():
        raise HTTPException(status_code=403, detail="Access denied")

    lines = CONFIG_FILE.read_text().splitlines()
    status = False
    for line in lines:
        if line.startswith("DEBUG_ROUTES_ENABLED="):
            status = line.split("=")[1].strip().lower() == "true"
            break
        else:
            # If the line is not found, we assume it's disabled
            status = False

    typer.echo(
        f"🔍 Debug routes currently: {'✅ ENABLED' if status  else '❌ DISABLED'}"
    )
