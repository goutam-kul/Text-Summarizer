import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a YAML file and return a ConfigBox object
    
    Args:
        path_to_yaml (Path): Path to the YAML file
        
    Raises : 
    
        ValueError: If the YAML file is empty
        e : empty file
    
    Returns:
    
        ConfigBox: A ConfigBox object
    
    """
    try :
        with open(path_to_yaml, "r") as f:
            content = yaml.safe_load(f)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError :
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose= True):
    """creata list of directories

    Args:
        path_to_directories (list): list of paths to directories
        verbose (bool, optional): Ignore if multiple directories are created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Creating directory:{path} for the file {path}")
            

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in kb
    
    Args:
    
        path (Path): Path to the file
        
    Returns:
    
        str: size in kb
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb}"