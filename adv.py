import pandas as pd
import statsmodels.api as sm

# Load the data from an Excel file
file_path = 'setadv.csv'  # Replace with your actual file path

try:
   df = pd.read_csv(file_path)
  # For .xlsx files
except Exception as e:
    print(f"Error reading the Excel file: {e}")
    exit()

# Display the first few rows of the DataFrame and its columns
print("First few rows of the dataset:")
print(df.head())
print("Column names:", df.columns)  # Check actual column names

# Define independent variables (TV, radio, newspaper) and dependent variable (sales)
X = df[['TV', 'radio', 'newspaper']]  # Use lowercase 'radio' and 'newspaper'
y = df['sales']  # Use lowercase 'sales'

# Add a constant term to the predictor variables (for the intercept)
X = sm.add_constant(X)

# Fit the multiple linear regression model
model = sm.OLS(y, X).fit()

# Print out the summary of the regression results
print("\nRegression Results:")
print(model.summary())




