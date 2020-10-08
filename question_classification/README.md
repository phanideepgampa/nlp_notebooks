# Coarse Question Classification Task:
The task deals with [Question Classification](https://cogcomp.seas.upenn.edu/Data/QA/QC/)

The goal is to build a text classification system which takes as input a string and outputs a categorical (one of “DESC”, “ENTY”, “ABBR”, “HUM”, “LOC”, “NUM”). While the original task also contains fine grained classes, the current repo deals with coarse classes. 

## Conda environment setup
```
conda env create -f environment.yml

conda activate question_classification
python -m ipykernel install --user --name question_classification --display-name "Python (question_classification)" #so that jupyter can detect the kernel

jupyter notebook
```
## Notebook Details
1. *qc_with_feat* notebook deals with using non deep learning classifiers like LinearSVC, Xgboost etc on linguistic features extracted from the data. 
2. *qc_With_bert* notebook deals with finetuning a BERT model for question classification.

## Results

| Model (Features)| Coarse Set Accuracy |
| ------------- | ------------- | 
| BERT-base (bert's tokenizer) | **97.0** | 
| LinearSVC (NER+POS+Lemma+Shape+Syntactic Dep)| 87.0 |
| Xgboost (NER+POS+Lemma+Shape+Syntactic Dep) | 85.0 |
| SVC (NER+POS+Lemma+Shape+Syntactic Dep) | 75.0 |

