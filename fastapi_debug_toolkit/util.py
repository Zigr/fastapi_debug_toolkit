import os
from pathlib import Path


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
    while (
        not ((bakend_root / backend).exists() and (bakend_root / backend).is_dir())
        and (bakend_root != backend or bakend_root != bakend_root.anchor)
        and backend not in bakend_root.as_uri()
    ):
        bakend_root = bakend_root.parent
        print(
            f"Trying: {bakend_root}  for {bakend_root / backend} bakend_root.parent {bakend_root.parent}"
        )

    print(f"Backend Root: {bakend_root}")

    return bakend_root


def get_from_env(name: str | None = None) -> dict | str | None:
    if name is not None:
        return os.getenv(name)
    else:
        return dict(os.environ)


def get_env_settings(name: str | None = None) -> str | dict[str, str] | None:
    if name is not None:
        f = get_from_env(name)
        if f is not None:
            return f  # type: ignore
    else:
        f_dic = get_from_env()
        if f_dic:
            return f_dic  # type: ignore

    # For local development try to find in .env file
    bakend_root: Path = get_backend_folder()
    ENV_FILE = Path(bakend_root / ".env")
    if not Path(bakend_root / ".env").exists:
        return None

    lines = ENV_FILE.read_text().splitlines()
    tuple_list = []
    for line in lines:
        if line.startswith("#"):
            continue
        if line.isspace() or not line.strip():
            continue
        splitted = line.split("=")
        tuple_list.append((splitted[0], splitted[1]))
    result = dict(tuple_list)

    return result if name is None else result[name]
