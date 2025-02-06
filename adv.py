import pandas as pd
import statsmodels.api as sm


file_path = 'setadv.csv'  

try:
   df = pd.read_csv(file_path)
  
except Exception as e:
    print(f"Error reading the Excel file: {e}")
    exit()

# Display the first few rows of the DataFrame and its columns
print("First few rows of the dataset:")
print(df.head())
print("Column names:", df.columns)  

X = df[['TV', 'radio', 'newspaper']]  
y = df['sales']  

# Add a constant term to the predictor variables (for the intercept)
X = sm.add_constant(X)

# Fit the multiple linear regression model
model = sm.OLS(y, X).fit()

# Print out the summary of the regression results
print("\nRegression Results:")
print(model.summary())




