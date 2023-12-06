import setuptools


with open('README.md', 'r', encoding='utf-8') as f:
    description = f.read()
    
    
    
__version__ = '0.0.0'

REPO_NAME = 'Kidney-Tumor_classification_Deep_learning'
AUTHOR_USER_NAME = 'codedestructed007'
SRC_REPO = 'src'
AUTHOR_EMAIL = 'codexistslonglastingnotfog@gmail.com'


setuptools.setup(
    name = SRC_REPO,
    version= __version__,
    author=AUTHOR_USER_NAME,
    url= f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}.git',
    packages = setuptools.find_packages(where='src/cnnClassifier'),
    license='MIT',
    package_dir={'': 'src/cnnClassifier'}
)
