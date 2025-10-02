import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "Movie-Recommendation-System"



list_of_files = [
    f"src/{project_name}/preprocess.py",
    f"src/{project_name}/build_content_model.py",
    f"src/{project_name}/build_cf_model.py",
    f"src/{project_name}/evaluate.py",
    f"src/{project_name}/app_streamlit.py",
    f"models/{project_name}/cosine_sim.pkl",
    f"models/{project_name}/tfidf_vectorizer.pkl",
    f"models/{project_name}/svd_model.pkl",
    f"models/{project_name}/indices.pkl",
    "Dockerfile",
    "README.md",
    "requirements.txt"


]



for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")