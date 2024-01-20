import os
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any, List

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'Read {path_to_yaml} successfully')
            return ConfigBox(content)
    except ValueError:
        raise ValueError(f'Yaml file is empty')
    

def create_dir(path_to_dir: list, verbose = True) -> None:
    if isinstance(path_to_dir, list):
        for dir in path_to_dir:
            if not os.path.exists(dir):
                os.makedirs(dir, exist_ok=True)
                if verbose:
                    logger.info(f'{dir} created')
            else:
                if verbose:
                    logger.info(f'{dir} already exists')

@ensure_annotations
def get_size(path_to_file: Path) -> str:
    size = os.path.getsize(path_to_file)
    if size > 1024 ** 2:
        return f'{size / 1024 ** 2:.2f} MB'
    elif size > 1024:
        return f'{size / 1024:.2f} KB'
    else:
        return f'{size:.2f} bytes'

