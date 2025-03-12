import pandas as pd  # Import  pandas library for handling data
import statsmodels.api as sm  # Import statsmodels for regression analysis

# Define file path to the dataset
file_path = 'setadv.csv'  

#  to load the dataset into a DataFrame
try:
   df = pd.read_csv(file_path)  # Read  CSV file into a pandas DataFrame
except Exception as e:
    print(f"Error reading the Excel file: {e}")  # Print an error message if file reading fails
    exit()  # Exit the script 

# Display some basic information about the dataset
print("First few rows of the dataset:")
print(df.head())  # Show  first five rows to get an idea of the data
print("Column names:", df.columns)  # Print all column names to verify structure

# Define the independent variables (TV, radio, newspaper) that might influence sales
X = df[['TV', 'radio', 'newspaper']]  

# Define the dependent variable (sales), which we are trying to predict
y = df['sales']  

# Add  constant term to the independent variables 
X = sm.add_constant(X)

# Fit a multiple linear regression model using Ordinary Least Squares (OLS)
model = sm.OLS(y, X).fit()

# Print out the summary of the regression results, including coefficients, R-squared value, and p-values
print("\nRegression Results:")
print(model.summary())  # Explains how well the model explains the sales data
