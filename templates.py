import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

list_of_files = [
    "src/__init__.py",
    "src/embeddings.py",
    "src/document_loaders.py",
    "src/chunking.py",
    "src/vectorstore.py",
    "src/rag_pipeline.py",
    "src/llm_integration.py",
    "config/config.yaml",
    ".env",
    "setup.py",
    "requirements.txt",
    "app.py",
    "exploration/notebook.ipynb",
    "data/sample_pdfs/.gitkeep",
    "Project_Preparation/README.md",
    ".gitignore",
]

for file_path in list_of_files:
    filepath = Path(file_path)
    filedir, filename = os.path.split(filepath)

    try:
        # Create directory if it doesn't exist
        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Created directory: {filedir}")

        # Create empty file if it doesn't exist or is empty
        if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
            with open(filepath, "w") as f:
                pass
            logging.info(f"Created file: {filepath}")
        else:
            logging.info(f"File already exists: {filepath}")

    except Exception as e:
        logging.error(f"Error creating {filepath}: {e}")



# import os
# from pathlib import Path
# import logging

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# list_of_files = [
#     "src/__init__.py",
#     "src/embeddings.py",
#     "src/document_loaders.py",
#      "src/chunking.py",
#     "src/vectorstore.py",
#     "src/rag_pipeline.py",
#     "src/llm_integration.py",
#     "config/config.yaml",
#     ".env",
#     "setup.py",
#     "requirements.txt",
#     "app.py",
#     "exploration/notebook.ipynb",
#     "data/sample_pdfs/.gitkeep",
#     "Project_Preparation/README.md",
#     ".gitignore",
# ]

# for file_path in list_of_files:
#     filepath = Path(file_path)
#     filedir,filename = os.path.split(filepath)

#     try:
#         if filedir != "":    # src
#             os.makedirs(filedir, exist_ok=True)
#             logging.info(f"Created directory: {filedir}")

#         if (not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):    # src/__init__.py
#             with open(filepath, 'w') as f:
#                 pass
#             logging.info(f"Created file: {filepath}")
#         else:
#             logging.info(f"File already exists: {filepath}")

#     except Exception as e:
#         logging.error(f"Error creating {filepath}: {e}")

