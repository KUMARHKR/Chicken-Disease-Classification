import os
from box.exceptions import BoxvalidateError
import yaml
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ Read yaml file and return
     
      Args:
        path_to_yaml (str): path lick input
         
      Reises:
        valueError: if yaml file is empty
        e: empty file 
        
      Returns:
        ConfigBox: Configbox type
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info(f"yaml file loaded from {path_to_yaml} loaded Successfully")
            return ConfigBox(config)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise(e)
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """ Create directories if not exists
      Args:
        path_to_directories (list): list of paths to create directories
        verbose (bool, optional): Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at {path}")

@ensure_annotations
def save_json(path: Path, date: dict):
    """ save json file
      Args:
        path (Path): path to save json file
        date (dict): data to save
    """
    with open(path, "w") as json_file:
        json.dump(date, json_file, indent=4)

    logger.info(f"json file saved at {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """ get size of file in MB
      Args:
        path (Path): path to file
      Returns:
        float: size of file in MB
    """
    size_in_bytes = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"



def decodeImage(imgstring , fileName ):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImage(image):
    with open(image, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string.decode('utf-8')


