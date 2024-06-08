# N-grams and Sentiment Analysis

This repository contains solutions to two main problems: identifying random sentences using n-grams and predicting sentiment from movie reviews using a Naïve Bayes classifier.

## Table of Contents

- [Overview](#overview)
- [Problems Solved](#problems-solved)
  - [N-grams Problem](#n-grams-problem)
  - [Sentiment Analysis Problem](#sentiment-analysis-problem)
- [Usage](#usage)
  - [N-grams Functions](#n-grams-functions)
  - [Sentiment Analysis Functions](#sentiment-analysis-functions)
- [Installation](#installation)
- [Testing](#testing)

## Overview

This project is implemented in Python 3.8+ and leverages `nltk` and `sklearn` libraries. The provided functions perform specific tasks related to text analysis, including n-gram creation and sentiment prediction.

## Problems Solved

### N-grams Problem

The first part of the project focuses on creating n-grams from a training file and using them to identify randomly generated sentences.

- **Function**: `calcNGrams_train(trainFile)`
  - **Input**: A text file where each line is arbitrary real-world (human-generated) text.
  - **Output**: Generates n-grams (bigrams and trigrams) from the text and stores them for further analysis.

- **Function**: `calcNGrams_test(sentences)`
  - **Input**: A list of sentences where one sentence is randomly generated.
  - **Output**: Returns the index of the randomly generated sentence based on the n-grams trained earlier.

### Sentiment Analysis Problem

The second part involves training a Naïve Bayes classifier to predict the sentiment of movie reviews.

- **Function**: `calcSentiment_train(trainFile)`
  - **Input**: A JSON list file where each line contains a movie review and a boolean sentiment value.
  - **Output**: Trains a Naïve Bayes classifier to predict sentiment based on the provided reviews.

- **Function**: `calcSentiment_test(review)`
  - **Input**: A string containing a movie review.
  - **Output**: Predicts and returns the sentiment (True for positive, False for negative) of the review using the trained Naïve Bayes model.

## Usage

### N-grams Functions

1. **Training N-grams**
    ```python
    from ngram-sentiment import calcNGrams_train
    calcNGrams_train('problem1_trainingFile.txt')
    ```

2. **Testing N-grams**
    ```python
    from ngram-sentiment import calcNGrams_test
    sentences = [
        "We have heard her clear, bird-like voice mingling with the scarlet symbol, and the most agreeable of his.",
        "poetry unthrifty ignominy devoting passages ceases strewn wished concerned progenitors arrangement borne sergeants express contains flowers medicine vain mahogany social",
        "I have ever cherished, and would be convulsed with rage of grief and sob out her love for her."
    ]
    random_sentence_index = calcNGrams_test(sentences)
    print(f"The randomly generated sentence is at index: {random_sentence_index}")
    ```

### Sentiment Analysis Functions

1. **Training Sentiment Analysis**
    ```python
    from ngram-sentiment import calcSentiment_train
    calcSentiment_train('problem2_trainingFile.jsonlist')
    ```

2. **Testing Sentiment Analysis**
    ```python
    from ngram-sentiment import calcSentiment_test
    review = "The movie was fantastic with outstanding performances and a thrilling plot."
    sentiment = calcSentiment_test(review)
    print(f"The sentiment of the review is: {'Positive' if sentiment else 'Negative'}")
    ```

## Installation

Ensure you have Python 3.8+ installed. Clone the repository and install the required libraries:

```bash
git clone https://github.com/rfeinberg3/NLP_N-grams_Sentiment-analysis.git
cd NLP_N-grams_Sentiment-analysis
pip install -r requirements.txt
```

## Testing

The project includes a grader script `ngram-sentiment_grader.py` to automatically test the functions. Ensure your functions meet the performance criteria and correctness by running the grader:

```bash
python ngram-sentiment_grader.py
```