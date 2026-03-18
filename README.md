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

Since most of the code is in jupyter notebooks, it would help to use an IDE like VSCode with the Python extension
- In addition, be sure to install the jupyter notebooks extension

Prior to installing any libraries, it would be a good idea to create a new python virtual environment.
Use the virtual environment for this project

1. This can be done with `virtualenv dir` (e1) where the interpreter and libraries will be stored. 
2. Once `e1` is created, activate it using: `source ./e1/bin/activate`
    - To deactivate use command run `deactivate`. You can find it using `which deactivate`
3. Install the following libraries at a minimum. More may be needed
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
        - Store it under the models directory in this repo
    
    **TODO** more content for Libs & dependencies

### Understand the Train-test split
**This is an important part of understanding the image similarity project**

1. There are 10,002 total products
2. Those products have 33,975 total images that are valid and can be downloaded
3. A product can have anywhere from 1 to **at most 7** images associated with it
4. Lots of products have less than 7. Some have just one. Many have up to 5
5. We index (write to the database), the first 5 images for every product
   1. "Question: First 5 in which order?"; Answer: the order in which they appear in the json file from huggingface
   2. As a result, the first 5 will not change with repeated runs of the ingestion
6. For any product, this does not index images numbered 6 or 7 and they are used for testing
   1. Testing means: we use an image - **that is not indexed in the database** to find a similar image
   2. This way we avoid asking the database for exact data

### Running the project

Run everything in order from 00 onwards. The `00_config.py` must be run for other files to have the context they need.

1. 10 - get_product_metadata Downloads the product metadata from huggingface and saves it to a json file
   1. Take some time to understand the schema of product data
   2. Some keys you will see - Uniq Id, Product Name, "About Product", Brand Name, Category, Image, Product Description
   3. The Image key has a value that's a pipe (|) character split of image URLs
   4. We will not work with all of the keys
2. 20 - download_products downloads images from the given URLs to the product_images directory
   1. Expect around 1,302,219,430 total bytes or 1.3 gigs in total
   2. Expect 33,975 images
3. 30 - validate_product_data - provides stats on the dataset
   1. This notebook lists out some stats on how many products (10002) were found
   2. How many total images were downloaded (some URLs are invalid)
      1. How many product had all their images
      2. How many were not downloaded due to missing 404 erors
      3. How many malformed image URLs were found
      4. How many were transparent-pixe.jpg images which were skipped
   3. Analyzes the size of the product description columns for creating a text index later
4. 32 - bulk_write_and_import - Illustrates how to use bulk_writer
   1. This notebook defines the schema for the bulk_writer and our milvus collection
   2. In a multi-threaded way, this runs the embedding model and writes parquet files to the minio container
   3. This process is very slow because model invocation is slow. Expect 30-45 minutes
   4. The notebook then launches a job within the database to read from minio and ingest the data
   5. Indexes are also defined on a handful of fields
5. 35 - prod_schema_FTS - This notebook buils a full text index
   1. Uses the BM25 metric to bulid a sparse index
   2. Data comes from the "Product Name", "Categories" and "About Product" fields
6. 55 - rsearch_examples - This notebook is for testing image similarity
   1. **TODO** provide an explanation
