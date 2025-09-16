import os
from pathlib import Path

from dotenv import load_dotenv


def is_docker() -> bool:
    def text_in_file(text, filename):
        try:
            with open(filename, encoding="utf-8") as lines:
                return any(text in line for line in lines)
        except OSError:
            return False

    cgroup = "/proc/self/cgroup"
    return os.path.exists("/.dockerenv") or text_in_file("docker", cgroup)


def get_project_root() -> Path:
    if is_docker():
        return Path("/app")

    # Get the absolute path of the current script
    script_path = Path(__file__).resolve()

    # Get the directory of the current script
    script_directory = script_path.parent

    # Example: Find the project root by looking for a .git directory
    project_root = script_directory
    while (
        not ((project_root / ".git").exists() and (project_root / ".git").is_dir())
        and project_root != project_root.parent
    ):
        project_root = project_root.parent

    # print(f"Project Root (based on .git): {project_root}")
    return project_root


def get_backend_folder() -> Path:
    if is_docker():
        return Path("/app")

    backend = "backend"
    # Get the absolute path of the current script
    script_path = Path(__file__).resolve()

    # Get the directory of the current script
    script_directory = script_path.parent

    # Example: Find the project root by looking for a .git directory
    bakend_root = script_directory
    while not (
        (bakend_root / backend).exists() and (bakend_root / backend).is_dir()
    ) and (bakend_root != backend or bakend_root != bakend_root.anchor):
        bakend_root = bakend_root.parent

    # print(f"Backend Root: {bakend_root}")

    return bakend_root


def get_env_setting(name: str) -> str | None:
    return os.getenv(name)


def set_env_setting(name: str, value: str = ""):
    os.environ[name] = value
    print(f"key: {name} value: {os.environ.get(name)}")


def is_debug_routes_set() -> bool:
    debug_routes = os.environ.get("DEBUG_ROUTES_ENABLED", "false")
    # for key, value in os.environ.items():
    #     print(f"{key}: {value}")
    return True if debug_routes == "true" else False


def set_debug_routes_env(value: bool | str):
    if isinstance(value, bool):
        set_env_setting("DEBUG_ROUTES_ENABLED", "true" if value else "false")
    else:
        set_env_setting("DEBUG_ROUTES_ENABLED", value.lower())


def get_env_settings() -> dict[str, str] | None:
    f_dic = dict(os.environ)
    if f_dic:
        return f_dic  # type: ignore

    # For local development try to find in .env file
    bakend_root: Path = get_backend_folder()
    ENV_FILE = Path(bakend_root / ".env")
    if not Path(bakend_root / ".env").exists():
        return None
    load_dotenv(dotenv_path=ENV_FILE, override=True)
    result = dict(os.environ)
    return result


def write_env_file_setting(
    env_file: Path, key: str = "DEBUG_ROUTES_ENABLED", value: str = ""
) -> list[str]:
    lines = env_file.read_text().splitlines()
    updated = False
    new_lines = []

    for line in lines:
        KEY = key.upper()
        if line.startswith(f"{KEY}="):
            new_lines.append(f"{KEY}={value}")
            updated = True
        else:
            new_lines.append(line)

    if not updated:
        new_lines.append(f"{key}={value}")
    return new_lines


def read_env_file_setting(env_file: Path, key: str = "DEBUG_ROUTES_ENABLED") -> str:
    lines = env_file.read_text().splitlines()
    value = ""
    for line in lines:
        if line.startswith(f"{key}="):
            value = line.split("=")[1].strip()
            break
    return value
