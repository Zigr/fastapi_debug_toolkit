import os
from pathlib import Path

from dotenv import load_dotenv


def is_docker():
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
    print(
        f"1-st: {not ((bakend_root / backend).exists() and (bakend_root / backend).is_dir())}"
    )
    print(f"2-nd: { (bakend_root != backend or bakend_root != bakend_root.anchor)}")

    while (
        not ((bakend_root / backend).exists() and (bakend_root / backend).is_dir())
        and (bakend_root != backend or bakend_root != bakend_root.anchor)
        # and backend not in bakend_root.as_uri()
    ):
        bakend_root = bakend_root.parent
        print(
            f"Trying: {bakend_root}  for {bakend_root / backend} bakend_root.parent {bakend_root.parent}"
        )

    print(f"Backend Root: {bakend_root}")

    return bakend_root


def get_env_setting(name: str) -> str | None:
    return os.getenv(name)


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
