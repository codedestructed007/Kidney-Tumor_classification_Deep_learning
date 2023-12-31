import os
from pathlib import Path
import logging



# logging format
format = '[%(asctime)s]: - %(filename)s\nAt Module -%(module)s %(message)s\n line number - %(lineno)s'

logging.basicConfig(
    level= logging.INFO, format = format
)

project_name = 'cnnClassifier'

list_of_files  = [
    '.github/workflow/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/entity/config_entity.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'schema.yaml',
    'main.py',
    'app.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
    'templates/index.html'
]



for filepath in list_of_files:
    filepath  = Path(filepath)
    filedir, filename  = os.path.split(filepath)



    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info("Creating directory {} for the file :{}".format(filedir,filename))


    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info("Creating empty file: {}".format(filepath))

    else:
        logging.info('{} is already exists'.format(filename))
