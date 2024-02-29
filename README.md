# Course-Recommendation-System

### Software And Tools Requirements

1. [GithubAccount](https://github.com)
2. [HerokuAccount](https://heroku.com)
3. [VSCodeIDE](https://code.visualstudio.com/)
4. [GitCLI](https://git-scm.com/downloads)
5. [AnacondaPackage/JupyterNoteBook](https://www.anaconda.com/products/distribution)

### Creata a New Environment and Activate!!

```
conda create -p venv python==3.9 -y
conda activate venv/
```

### Install all the Required Libraries!!

```
pip install -r requirements.txt
```

### Run Command

```
streamlit run app.py
```
.
.
.
.
### Getting started with the Project!!

1. Import all the necessary libraries
2. Import the Dataset
3. Do all the necessary Data Cleaning and Standardization
4. Start with TFIDF Vectorizer using Sigmoid function
5. Extraxt Index, List & Enumerate, Sorted, Took the first Sig Score and Returned the corresponding Course Name
6. Starting Bag of Words Memory Based Model 
7. Used PorterStemmer of NLTK for Stemming the dataset
8. After Stemming started CountVectorizer with CosineSimilarity function
9. Repeated Step 5
10. Finalized the Recommendations and Pickeled the same

##  Note - these both approaches can be used to build any memory based recommendation system.
.
.
.
.
# Enjoy the Recommendations