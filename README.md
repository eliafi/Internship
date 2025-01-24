# Internship Project: Predictive Modeling with LightGBM and Random Forest

## Overview

This project involves building predictive models to forecast customer purchase behavior using machine learning techniques. The primary goal is to predict the next product a customer is likely to buy based on their purchase history and other relevant features.

## Project Structure

- **Data Preparation**: The data is read from an Excel file and preprocessed to handle missing values, encode categorical variables, and create new features.
- **Feature Engineering**: New features such as `DaysSinceLastOrder`, `TotalPurchases`, `AvgTurnover`, and `AvgOrderQty` are created to enhance the predictive power of the models.
- **Model Training**: Two machine learning models, LightGBM and Random Forest, are trained on the prepared dataset.
- **Model Evaluation**: The models are evaluated using accuracy, precision, recall, and F1-score metrics.

## Key Components

### Data Preparation

- **Reading Data**: The data is read from an Excel file using `pandas`.
- **Datetime Conversion**: The `sal_orderDate` column is converted to datetime format.
- **Handling Missing Values**: Missing values in the `DaysSinceLastOrder` column are filled with zero.
- **Encoding Categorical Variables**: Label encoding is applied to categorical columns such as `sal_Prod_Grp`, `sal_Prod_id`, `sal_Prod_Name`, and `sal_custID`.

### Feature Engineering

- **Datetime Features**: New features like `DayOfWeek` and `Month` are extracted from the `sal_orderDate` column.
- **Aggregation Features**: Aggregated features such as `TotalPurchases`, `AvgTurnover`, and `AvgOrderQty` are created for each customer.

### Model Training

- **Random Forest**: A Random Forest model is trained with balanced class weights to handle class imbalance.
- **LightGBM**: A LightGBM model is trained with default parameters.

### Model Evaluation

- **Accuracy**: The accuracy of the models is calculated.
- **Classification Report**: Precision, recall, and F1-score are computed for each class.
- **ROC AUC**: The Area Under the Receiver Operating Characteristic Curve (ROC AUC) is calculated for the models.

## Results

- **Random Forest Accuracy**: 99%
- **LightGBM Accuracy**: 7%

The Random Forest model performed significantly better than the LightGBM model in this case.

## Conclusion

This project demonstrates the application of machine learning techniques to predict customer purchase behavior. The Random Forest model showed promising results and can be further tuned for better performance.

## Future Work

- **Hyperparameter Tuning**: Further tuning of model hyperparameters to improve performance.
- **Feature Selection**: Identifying and selecting the most important features for the model.
- **Model Deployment**: Deploying the model to a production environment for real-time predictions.

## Acknowledgments

I would like to thank my internship supervisor and team members for their guidance and support throughout this project.
