import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


__version__ = "0.0.1"

REPO_NAME = "Chicken-Disease-Classification"
AUTHOR_NAME = "DIP KUMAR DHAWA"
AUTHOR_USERNAME = "KUMARHKR"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "dipkumardhawa020@gmail.com"


setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A snall python NLP 'Text Summarization' App",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls={ 
        "Bug Tracker": f"https://github.com/KUMARHKR/Chicken-Disease-Classification.git/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),

    )