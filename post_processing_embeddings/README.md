# Post Processing Word Embeddings
This repo contains the code for the algorithm given in the paper [ALL-BUT-THE-TOP: SIMPLE AND EFFECTIVE POSTPROCESSING FOR WORD REPRESENTATIONS
](https://arxiv.org/pdf/1702.01417.pdf). The algorithm removes the common mean from the embeddings and makes the embeddings isotropic. 

## Conda environment setup
```
conda env create -f environment.yml

conda activate post_process_emb
python -m ipykernel install --user --name post_process_emb --display-name "Python (post_process_emb)" #so that jupyter can detect the kernel

jupyter notebook
```
## Other Steps Required
1. Download Glove embeddings from http://nlp.stanford.edu/data/glove.6B.zip and place it in this folder. 
2. Processed vectors are stored in the file *processed_embeddings.npz* after running the jupyter notebook. The code to read the file is given in *read_embeddings.py*. 
3. Word Embeddings Benchmark is a package with variety of tasks to test the performance of word embeddings. https://github.com/kudkudak/word-embeddings-benchmarks. Install **web** package by following the instructions given in the repo or place the source code manually in this folder.

