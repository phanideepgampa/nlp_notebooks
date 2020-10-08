# SentiMix Task - Sentiment classification of code mixed tweets:
- The task is taken from [SemEval 20 Sentimix](https://competitions.codalab.org/competitions/20654).

- The task is to predict the sentiment of a given code-mixed tweet. The sentiment labels are positive, negative, or neutral, and the code-mixed languages will be English-Hindi and English-Spanish. Besides the sentiment labels, we will also provide the language labels at the word level. The word-level language tags are en (English), hi (Hindi), mixed, and univ (e.g., symbols, @ mentions, hashtags).

- I have solved the task by keeping ML Pipeline in mind with different stages of Data Extraction, Preprocessing, Model Training and Serving. 


## Running the Notebook:

For creating the same anaconda environment with relevant packages:

```

conda env create -f environment.yml

conda activate sentimix

```

Then to run the notebook:

```
jupyter notebook

```
