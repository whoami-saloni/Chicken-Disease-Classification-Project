import os
import yaml
from cnnClassifier import logger
import json
import joblib
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_you:Path) ->ConfigBox:
    """
    Reads a YAML file and returns a Box object.

    Args:
        path_to_you (Path): Path to the YAML file.
    Raises:
        ValueError: If the YAML file is empty.
        e:empty file
    Returns:
        ConfigBox: ConfigBox type 
    """
    try:
        with open(path_to_you, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file:{path_to_you} loaded Successfully")
        return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"The YAML file {path_to_you} is empty.")
    
    except Exception as e:
        raise e

@ensure_annotations
def create_directory(path_to_directories:list,verbose=True):
    """
    Creates a list of directories.

    Args:
        path_to_directories (list): List of directories to be created.
        ignore_log(bool,optional):ignore if multiple directories to be created.Default to false.
    """
    for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Directory {path} created successfully.")

@ensure_annotations
def save_json(path:Path, data: dict):
     """ save json data
     Args:
         path (Path): Path to json file.
         data (dict): data to be saved in json file.
    """
     with open(path, 'w') as f:
         json.dump(data, f, indent=4)
     logger.info(f"Json data saved successfully at {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
     """ load json data
     Args:
         path (Path): Path to json file.
     Returns:
         config_box: data as class attribute instead of dict 
     """
     with open(path, 'r') as f:
         content = json.load(f)
     logger.info(f"Json data loaded successfully from {path}")
     return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
     """ save binary file
     Args:
         data (Any): data to be saved in binary file.
         path (Path): Path to binary file.
    """
     joblib.dump(value=data, filename=path)
     logger.info(f"Binary data saved successfully at {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
     """ load binary file
     Args:
         path (Path): Path to binary file.
     Returns:
         Any: data loaded from binary file.
     """
     data=joblib.load(filename=path)
     logger.info(f"Binary data loaded successfully from {path}")
     return data
@ensure_annotations
def get_size(path: Path) -> str:
     """ get size in KB
     Args:
         path (Path): Path to file.
     Returns:
         str: size in KB.
     """
     size_in_KB = round(os.path.getsize(path)/1024)
     return f"~ {size_in_KB} KB"

@ensure_annotations
def decode_image(imgstring,filename):
     imgdata = base64.b64decode(imgstring)
     with open(filename, 'wb') as f:
           f.write(imgdata)
           f.close()

def encodeImageIntoBase64(filename):
     with open(filename, "rb") as f:
        return base64.b64encode(f.read())
     