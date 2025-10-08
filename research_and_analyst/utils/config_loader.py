from pathlib import Path 
import os 
import yaml 

def _project_root() ->Path:
    """
    Returns the parent directory of the current file.
    Note: parent[1] is likely a bug; it should probably be .parent.parent to go up two levels.
    """ 
    return Path(__file__).resolve().parent.parent.parent

def load_config(config_path: str | None = None) -> dict:
    """ 
    Loads a YAML config file using the following priority:

    - If config_path is provided as an argument, use it.
    - Else, if the CONFIG_PATH environment variable is set, use that.
    - Else, use <project_root>/config/configuration.yaml as the default.
    - If the path is not absolute, it is resolved relative to the project root.
    - Raises FileNotFoundError if the config file does not exist.
    - Loads and returns the YAML config as a dictionary.


    Resolve config path reliably irrespective of CWD
    Priority: explicit arg > CONFIG_PATH env > <project_root>/config/config.yaml
    """

    env_path = os.getenv('CONFIG_PATH')
    if config_path is None:
        config_path = env_path or str(_project_root()/'config'/'configuration.yaml')

    path = Path(config_path)
    # If path is not absolute and does not already start from project root, join with project root
    if not path.is_absolute():
        path = _project_root() / path

    if not path.exists():
        raise FileNotFoundError(f'Config file not found: {path}')
    
    with open(path,'r', encoding='utf-8') as f:
        return yaml.safe_load(f) or {} 