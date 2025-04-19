Here's an enhanced and detailed version of your README file:

---

# COVID-19 Diagnosis Using CT Scans and Symptoms Data

This project leverages two datasets—CT scan images and symptom details—to predict COVID-19 status using a logistic regression model. The model aims to classify patients as COVID-positive or COVID-negative based on the provided features.

## Datasets

The datasets used in this project are as follows:

1. **CT Scans Dataset**  
   - Source: [Kaggle - COVID-19 Lung CT Scans](https://www.kaggle.com/datasets/mehradaria/covid19-lung-ct-scans?resource=download-directory)  
   - Description: Contains CT scan images categorized into two folders:
     - **COVID**: CT scans of patients diagnosed with COVID-19.
     - **Non-COVID**: CT scans of patients without COVID-19.

2. **Symptoms Dataset**  
   - Source: [Kaggle - COVID-19 Symptoms Checker](https://www.kaggle.com/datasets/iamhungundji/covid19-symptoms-checker/data)  
   - Description: Tabular data containing details of patients' symptoms, including features such as:
     - Age
     - Gender
     - Fever
     - Severity
     - Other symptoms

## Data Preprocessing

### CT Scans
- CT scan images were preprocessed for feature extraction, normalized, and prepared for model training.

### Symptoms Data
- The tabular dataset was cleaned, and irrelevant or redundant features were removed.
- Columns such as **Age**, **Gender**, and **Severity** were merged for enhanced analysis.

### Output Column
- A new column, **Status**, was created in the symptoms dataset to indicate whether a patient is COVID-positive or COVID-negative based on their severity and other factors.

## Model

- **Model Used**: Logistic Regression
- **Approach**:  
  - Combined insights from CT scans and symptoms data to create a comprehensive dataset.
  - Used logistic regression to predict the **Status** column based on features like **Severity**, **Age**, **Gender**, and other symptoms.
  - The model provides a binary classification:
    - `1`: COVID-positive
    - `0`: COVID-negative

## Results and Analysis

- The model's performance was evaluated using metrics like accuracy, precision, recall, and F1-score.
- Initial results indicate that combining CT scan data with symptom details improves the prediction accuracy.

## Usage

To replicate this project:
1. Download the datasets from the provided links.
2. Ensure Python 3.x and necessary libraries (like `numpy`, `pandas`, `scikit-learn`, and `matplotlib`) are installed.
3. Run the preprocessing and logistic regression script to train and evaluate the model.

Future Improvements

- Create database and add data encryption
- Integrate advanced machine learning models (e.g., Random Forest, Gradient Boosting) for better performance.
- Explore other datasets to add more diversity and robustness to the model.
