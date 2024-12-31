<<<<<<< HEAD
# Credit Card Fraud Detection Project

## Introduction
This project aims to predict fraudulent credit card transactions using machine learning. The dataset is highly imbalanced, with fraudulent transactions accounting for only a small percentage of the total. The solution focuses on handling the class imbalance, preprocessing data, training machine learning models, and evaluating their performance.

## Dataset
- **Source**: The dataset contains anonymized transaction data, including:
  - **Time**: Time elapsed since the first transaction.
  - **Amount**: Transaction amount.
  - **V1 to V28**: Features derived from PCA transformation.
  - **Class**: Target variable (1 = Fraud, 0 = Legitimate).

## Project Workflow

### 1. Loading Libraries
- Imported necessary libraries such as pandas, numpy, scikit-learn, and visualization tools (matplotlib, seaborn).

### 2. Loading Dataset
- Read the dataset into a DataFrame and conducted initial inspection.
- Checked:
  - Data types and shape.
  - Missing values and duplicates (removed duplicates where applicable).

### 3. Exploratory Data Analysis (EDA)
- **Descriptive Statistics**:
  - Visualized distributions for Time, Amount, and the target variable (Class).
- **Correlation Analysis**:
  - Generated a correlation matrix heatmap for independent variables.

### 4. Data Preprocessing
- **Feature Transformation**:
  - Converted Time to hours for better interpretability.
- **Outlier Removal**:
  - Used the Interquartile Range (IQR) method to detect and remove outliers.
- **T-Test for Feature Selection**:
  - Conducted a t-test to assess the significance of variables.
  - Features with a p-value < 0.05 were retained for model building, ensuring statistical relevance.
- **Handling Class Imbalance**:
  - Resampled the dataset using SMOTE (Synthetic Minority Oversampling Technique) to address the imbalance between fraudulent and legitimate transactions.
- **Scaling Variables**:
  - Applied Min-Max Scaling to transform Amount and other numerical features into a uniform range, improving model convergence.
  - Scaling was performed after splitting data into training and testing sets to prevent data leakage.

### 5. Model Building
- **Logistic Regression**:
  - Built a baseline model to understand performance.
  - Tuned hyperparameters for improved results.
  - Evaluated the model using:
    - Classification Metrics: Precision, Recall, F1-Score, and Accuracy.
    - ROC AUC Curve: Calculated the Area Under the Curve (AUC) score and plotted the ROC curve to visualize the trade-off between true positive and false positive rates.
- **Decision Tree**:
  - Built a baseline model to understand performance.
  - Tuned hyperparameters for improved results.
  - Evaluated the model using:
    - Classification Metrics: Precision, Recall, F1-Score, and Accuracy.
    - ROC AUC Curve: Computed the AUC score and plotted the ROC curve to assess the model's ability to differentiate between fraudulent and legitimate transactions.

### 6. Model Saving
- Serialized and saved both models (Logistic Regression and Decision Tree) using joblib for deployment and future inference.

## Installation
### Prerequisites
- Python 3.8+

### Install the required libraries
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

### Additional Features
Statistical Feature Selection: The use of a t-test ensures that only statistically significant features contribute to the model, improving performance and interpretability.
Robust Evaluation: The inclusion of ROC AUC curves provides a visual and numerical understanding of model discrimination capabilities.
Scalable Preprocessing: Scaling ensures that features contribute equally to the model, especially for algorithms sensitive to variable magnitudes.

### Conclusion
This comprehensive approach ensures that the models are well-prepared to handle the challenges of fraud detection, including class imbalance and feature scaling.
>>>>>>> end of conflict marker