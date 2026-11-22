# 🏡 House Price Prediction Model using Linear Regression

## 📌 About the Project

Buying or selling a house involves many factors, and estimating the right price can sometimes be difficult.

I built this project to explore how Machine Learning can help predict house prices based on different property features.

Using Python and Linear Regression, I trained a model that learns from housing data and predicts the selling price of a house based on details such as living area, overall quality, number of bedrooms, garage capacity, and year of construction.

This project helped me understand how a basic Machine Learning model works in a practical, real-world scenario.

## 🎯 Project Objectives

- Understand and work with a real-world housing dataset.
- Identify important features that influence house prices.
- Build and train a Linear Regression model.
- Predict house prices using unseen data.
- Evaluate model performance using the R² score.
- Visualize actual house prices against predicted prices.

## 📂 Dataset

**Dataset:** House Prices – Advanced Regression Techniques

**Source:** Kaggle

The dataset contains information about residential properties, including:

- Overall house quality
- Living area
- Garage capacity
- Basement area
- Year built
- Number of bathrooms
- Number of bedrooms
- Lot area

The target variable is `SalePrice`, which represents the actual selling price of a house.

## 🛠️ Technologies Used

- Python
- Pandas – Data handling and analysis
- NumPy – Numerical calculations
- Matplotlib – Data visualization
- Scikit-learn – Machine Learning and model evaluation

## ⚙️ Project Workflow

**1. Data Loading**

Loaded the Kaggle housing dataset using Pandas and explored its structure.

**2. Feature Selection**

Selected eight important features that could help estimate house prices.

**3. Data Splitting**

Divided the dataset into:
- 80% training data
- 20% testing data

**4. Handling Missing Values**

Used median imputation to handle missing numerical values.

**5. Model Training**

Trained a Linear Regression model using Scikit-learn.

**6. Price Prediction**

Used the trained model to predict prices for the testing dataset.

**7. Model Evaluation**

Evaluated the predictions using R² score, Mean Absolute Error, and Root Mean Squared Error.

**8. Visualization**

Created a scatter plot to compare actual house prices with predicted prices.

## 📊 Model Performance

The model achieved the following results:

| Evaluation Metric | Result |
|---|---:|
| R² Score | 0.803 |
| Mean Absolute Error | 24,533.44 |
| Root Mean Squared Error | 38,876.76 |

The R² score of 0.803 indicates that the model explains approximately 80.3% of the variation in house prices on the test dataset.

These results gave me a practical understanding of how prediction models are evaluated and why predictions may differ from actual values.

## 📈 Actual vs Predicted Prices

The project generates a scatter plot comparing actual house prices with the prices predicted by the model.

The closer the points are to the ideal diagonal line, the closer the predictions are to the actual prices.

**Generated visualization:** `outputs/actual_vs_predicted.png`

## 📁 Project Structure

```text
House-Price-Prediction/
│
├── data/
│   └── train.csv
│
├── outputs/
│   ├── actual_vs_predicted.png
│   └── house_price_predictions.csv
│
├── main.py
└── README.md
```

## ▶️ How to Run the Project

**Step 1: Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**Step 2: Open the project folder**

```bash
cd House-Price-Prediction
```

**Step 3: Install the required libraries**

```bash
pip install pandas numpy matplotlib scikit-learn
```

**Step 4: Download the dataset**

Download the Kaggle House Prices dataset and place `train.csv` inside the `data` folder.

**Step 5: Run the Python program**

```bash
python main.py
```

The prediction results and visualization will be generated inside the `outputs` folder.

## 💡 What I Learned

Working on this project helped me understand how Machine Learning moves from theory to practical implementation.

Some of the important things I learned include:

- How to load and explore a real-world dataset using Pandas.
- How to select relevant features for prediction.
- Why training and testing data are separated.
- How Linear Regression learns relationships between variables.
- How to handle missing numerical values.
- How to evaluate a model using the R² score and error metrics.
- How to visualize model predictions using Matplotlib.

One of my biggest takeaways was understanding that a model's performance is not judged only by its predictions, but also by how closely those predictions match actual values.

## 🚀 Future Improvements

I would like to improve this project further by:

- Exploring additional housing features.
- Comparing Linear Regression with other regression algorithms.
- Improving prediction accuracy through feature engineering.
- Building a simple interface where users can enter house details and receive predicted prices.

## 🙌 Conclusion

This was a valuable beginner Machine Learning project that gave me hands-on experience with data handling, model training, prediction, evaluation, and visualization.

I'm looking forward to building more projects and improving my understanding of Artificial Intelligence and Machine Learning.

**Thanks for checking out my project!**

---

**Created by:** Lakshitha