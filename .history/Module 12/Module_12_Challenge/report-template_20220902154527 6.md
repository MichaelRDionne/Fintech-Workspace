# Credit Risk Analysis Report (Module 12 Challenge)

## Overview of the Analysis

* Analyzing credit risk poses a classification problem that’s inherently imbalanced. This is because healthy loans easily outnumber risky loans. Various techniques can be used to train and evaluate models with imbalanced classes. The dataset used was of historical lending activity from a peer-to-peer lending services company to build a model that can identify the creditworthiness of borrowers.

* The financial data used was activity from the lending services company. The data was provided by LendingClub, a peer-to-peer lending services company. The data was used to build a model that can identify the creditworthiness of borrowers.

* The balance of the labels was checked with the `value_counts` function. This was to identify if the data was balanced or imbalanced. The data was imbalanced with the initial model and then modified to be balanced with the `RandomOverSampler` algorithms in the second model.

* The dataset was split into training and testing sets using the `train_test_split` function.  The training set was over sampled using the `RandomOverSampler` algorithm.  

* The stages of the machine learning process used were as follows:
  * training the model
  * making predictions
  * evaluating the model

* The `LogisticRegression` model was used to train and evaluate the model using the balanced accuracy score, precision, and recall scores.

## Results of the Analysis

* Machine Learning Model 1:
  * Model 1 Accuracy Score =  0.9520479254722232 or 95.2%
  * Model 1 Precision Score of '0' = 1.00 or 100%
  * Model 1 Precision Score of '1' = 0.85 or 85%
  * Model 1 Recall Score of '0' = 0.99 or 99%
  * Model 1 Recall Score of '1' = 0.91 or 91% 

* Machine Learning Model 2:
  * Model 2 Accuracy Score =  0.9936781215845847 or 99.4%
  * Model 2 Precision Score of '0' = 1.00 or 100%
  * Model 2 Precision Score of '1' = 0.84 or 84%
  * Model 2 Recall Score of '0' = 0.99 or 99%
  * Model 2 Recall Score of '1' = 0.99 or 99%

## Summary

### Model 1

The (LRM) predicts the '0's as 1.0 or 100% precision.
The (LRM) predict's the '1's as 0.85 or 85% precision.

Since 'O' represents healthy loans it is 100 % accurate at determining healthy loans but only 85% accurate at determining high-risk loans ('1').

The recall for '0' is .99. That means we are 99% confident that the model correctly identified healthy loans.
The recall for '1' is 0.91. That means we are 91% confident that the model correctly identified high-risk loans.

### Model 2

The (LRM) predicts the '0's as 1.0 or 100% precision.
The (LRM) predict's the '1's as 0.84 or 84% precision.

Since 'O' represents healthy loans it is 100 % accurate at determining healthy loans but only 84% accurate at determining high-risk loans ('1').

Since the recall for '0' & '1' is 0.99. That means we are 99% confident that the model can equally & correctly identify either healthy or  high-risk loans.

The second model seems to perform best. The second model has a higher accuracy score, precision score, and recall score. The second model is also more balanced in its predictions.

The performance of the model depends on the problem we are trying to solve. In this case, it is more important to predict the `1`'s. The `1`'s represent high-risk loans. If we were to predict the `0`'s, we would be predicting healthy loans. It is more important to predict high-risk loans because we want to avoid lending money to people who are not likely to pay it back.
