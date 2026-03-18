# Milvus Image Demo: Image Indexing with Visualised BGE

This repo has some noteoboks and python files to help the audience install milvus on their computer, running with docker-compose.
This will require having docker on your computer.

## Pre-requisites. 

- Install docker and have docker-compose on the command line
- Install Docker Desktop for ease of management
- Be sure to install python and pip, with which to install the required libraries and dependencies
- **Optional**: TODO


## What you can expect to learn

1. Huggingface datasets
1. Running Milvus
1. Installing the Visualised BGE model on your python environment
1. Downloading images on your computer from huggingface dataset which has image URLs
1. Multi-threaded way to create embeddings from the images
1. Milvus Schemas and Indexing
1. Curing data to be inserted in a Milvus collection

**TODO**

### Getting started with Milvus
Visit this url https://milvus.io/docs and go to the **Get Started** section.

- See Install Milvus -> Run Milvus Standalone
- Create a new directory to run Milvus and store files
- Follow the instructions on this page https://milvus.io/docs/install_standalone-docker-compose.md
- Get the file milvus-standalone-docker-compose.yml
- Run this command `sudo docker compose up -d`
    - verify with docker ps or...
    - Verify in Docker Desktop that these 3 containers are running with ports:
    - `milvus-standalone` (19530, 9091), `milvus-etcd`, `milvus-minio` (9000, 9001)

### Libraries & Dependencies

Prior to installing any libraries, it would be a good idea to create a new python virtual environment.
Use the virtual environment for this project

1. This can be done with `virtualenv dir` (e1) where the interpreter and libraries will be stored. 
1. Once `e1` is created, activate it using: `source ./e1/bin/activate`
    - To deactivate use command `deactivate`. You can find it using `which deactivate`
1. Install the following libraries at a minimum. More may be needed
    - pymilvus
    - pymilvus[model]
    - datasets
    - matplotlib
    - numpy
    - torch
    - glob
    - ipywidgets
    - visual_bge -> instructions [to install](https://github.com/FlagOpen/FlagEmbedding/blob/master/research/visual_bge/README.md)
        - **very important** Use this command: `pip install -e . --config-settings editable_mode=compat`
    - Model file: [Visualized_base_en_v1.5](https://huggingface.co/BAAI/bge-visualized/blob/main/Visualized_base_en_v1.5.pth)
        - Download Link https://huggingface.co/BAAI/bge-visualized/resolve/main/Visualized_base_en_v1.5.pth

**TODO**
