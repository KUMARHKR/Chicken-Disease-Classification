import os 
import pathlib as Path
import logging 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configurations.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml"
    "params.yaml",
    "Requirements.txt",
    "Setup.py",
    "research/trials.ipynb",
    ]

for filepath in list_of_files:
    # filepath = Path(filepath) # pathlib.Path is not needed (this is for windows)
    filedir , filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created {filedir} for the {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            f.write("pass")
            logging.info(f"Created {filename}")
    else:
        logging.info(f"{filename} already exists")

logging.info("Done")