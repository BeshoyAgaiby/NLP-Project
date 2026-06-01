# NLP-Project
Developed an NLP-based text classification system that performs text preprocessing, feature extraction using Bag of Words and TF-IDF, and document classification using Logistic Regression. The project includes data cleaning, stemming, lemmatization, model evaluation, and prediction on unseen text samples.

# NLP Text Classification and Preprocessing Pipeline

## 📌 Overview

This project demonstrates a complete Natural Language Processing (NLP) workflow for text preprocessing, feature extraction, and text classification using Python and Scikit-Learn.

The system cleans raw textual data, applies multiple NLP preprocessing techniques, converts text into numerical representations using Bag of Words (BoW) and TF-IDF, then trains a Logistic Regression model to classify text documents into predefined categories.

---

## 🚀 Features

* Text cleaning and normalization
* Removal of:

  * URLs
  * Mentions (@username)
  * Hashtags
  * Numbers
  * Punctuation
* Tokenization using NLTK
* Stopword removal
* Stemming using Porter Stemmer
* Lemmatization using WordNet Lemmatizer
* Bag of Words (BoW) feature extraction
* TF-IDF feature extraction
* Text classification using Logistic Regression
* Model evaluation with:

  * Accuracy Score
  * Classification Report
  * Confusion Matrix
* Saving and loading trained models using Joblib
* Prediction on custom user input

---

## 🛠️ Technologies Used

* Python
* Pandas
* NLTK
* Scikit-Learn
* NumPy
* Joblib

---

## 📂 Project Workflow

### 1. Data Preprocessing

The dataset undergoes several cleaning stages:

* Remove noise (URLs, hashtags, mentions, numbers)
* Convert text to lowercase
* Remove punctuation
* Tokenize text
* Remove stopwords
* Apply stemming
* Apply lemmatization

Processed text is then saved into a new CSV file for further analysis.

---

### 2. Bag of Words (BoW)

A Bag of Words representation is generated using:

```python
CountVectorizer()
```

This converts textual documents into numerical vectors based on word frequency.

---

### 3. TF-IDF Feature Extraction

The project applies TF-IDF vectorization using:

```python
TfidfVectorizer()
```

to measure the importance of words across the dataset while reducing the impact of very common terms.

---

### 4. Model Training

A Logistic Regression classifier is trained on TF-IDF features:

```python
LogisticRegression(max_iter=1000)
```

The dataset is split into training and testing sets before model fitting.

---

### 5. Model Evaluation

Performance is evaluated using:

* Accuracy Score
* Classification Report
* Confusion Matrix

to measure the effectiveness of the classifier.

---

### 6. Model Persistence

The trained model and vectorizer are saved using Joblib:

```python
joblib.dump(model, "logistic_text_model.joblib")
joblib.dump(vectorizer, "tfidf_vectorizer.joblib")
```

allowing future predictions without retraining.

---

### 7. Prediction on New Text

Example:

```python
new_text = ["machine learning improves data analysis"]
```

The model predicts the corresponding category and provides prediction probabilities.

---

## 📊 Example Output

```text
Input:
"machine learning improves data analysis"

Predicted Label:
Technology

Prediction Probability:
[0.02, 0.95, 0.03]
```

---

## 🎯 Learning Outcomes

Through this project, the following NLP concepts were implemented and explored:

* Text preprocessing
* Feature engineering for text data
* Bag of Words representation
* TF-IDF weighting
* Supervised machine learning for NLP
* Logistic Regression for classification
* Model serialization and deployment preparation

---

## 📜 License

This project is developed for educational and learning purposes in Natural Language Processing and Machine Learning.

