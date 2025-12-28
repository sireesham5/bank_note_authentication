# bank_note_authentication
Bank Note Authentication using Machine Learning

📌 Project Overview
This project aims to authenticate bank notes as either genuine (0) or forged (1) using features extracted from images of various notes. A robust Random Forest Classifier was employed to build an accurate and reliable prediction model.

📊 Dataset Information:

The data used for training and testing is assumed to contain several numerical features derived from wavelet transforms and image analysis.
Features: Variance, Skewness, Curtosis, Entropy
Target Variable: Class (0 for Authentic, 1 for Forged)

🛠️ Technical Workflow

To achieve maximum accuracy and model stability, the following techniques were implemented:

The approach used in the code focuses on effective data preprocessing and leveraging the power of ensemble learning:
Data Preprocessing: Handled potential missing values (dropna()) and ensured categorical data was correctly encoded where necessary (though this specific dataset is likely all numerical).
Model Selection: The Random Forest Classifier was chosen because it inherently handles non-linear data relationships, is robust to outliers, and requires less explicit feature scaling than linear models like Ridge or Lasso.
Training: The model was trained on the processed features (X_train) and target labels (y_train) using model.fit().
Evaluation: Performance was measured using standard classification metrics (Accuracy Score, Classification Report).

🚀 Key FeaturesHigh Accuracy: 

Ensemble Learning: Utilizes the strength of multiple decision trees to make highly accurate predictions.
High Performance: Random Forests consistently provide high accuracy scores on structured data like this.
Scalability: The model can efficiently classify new bank note data inputs.

💻 Installation & Usage
Prerequisites:
Python 3.8+
Pandas, NumPy, Scikit-Learn

Install dependencies:
pip install pandas numpy scikit-learn


Run the main script:
python model.py

📈 Results
Using the Random Forest Classifier typically yields very high results for this specific dataset.
Accuracy Score: 98%+

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

Author: MIDDE SIREESHA

