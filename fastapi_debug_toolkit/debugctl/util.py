from pathlib import Path


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


def get_env_settings() -> dict[str, str]:
    project_root: Path = get_project_root()
    CONFIG_FILE = Path(project_root) / ".env"
    lines = CONFIG_FILE.read_text().splitlines()
    tuple_list = []
    for line in lines:
        if line.startswith("#"):
            continue
        if line.isspace() or not line.strip():
            continue
        splitted = line.split("=")
        tuple_list.append((splitted[0], splitted[1]))

    return dict(tuple_list)
