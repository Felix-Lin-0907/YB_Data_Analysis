
################ Data cleaning the Iris dataset #################
from sklearn import datasets
import pandas as pd

# load iris dataset
iris = datasets.load_iris()
# Since this is a bunch, create a dataframe
iris_df=pd.DataFrame(iris.data)
iris_df['class']=iris.target

iris_df.columns=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
#### ===> TASK 1: here - add two more lines of the code to find the number and mean of missing data
# Check for missing data in the dataset
missing_count = iris_df.isnull().sum()  # Count the number of missing values per column
missing_mean = iris_df.isnull().mean()  # Calculate the mean of missing values per column

# Print the results for missing data
print("Missing count per column:\n", missing_count)
print("\nMissing mean per column:\n", missing_mean)

cleaned_data = iris_df.dropna(how="all", inplace=True) # remove any empty lines


iris_X=iris_df.iloc[:5,[0,1,2,3]]
print(iris_X)

### TASK2: Here - Write a short readme to explain above code and how we can calculate the corrolation amoung featuers with description

"""
README:

1. Code Explanation:
   - This code loads the Iris dataset using the sklearn library.
   - The dataset is converted into a pandas DataFrame for easier data manipulation.
   - Missing data is checked using `isnull().sum()` (count of missing values) and `isnull().mean()` (proportion of missing values).
   - Any fully empty rows are removed using `dropna(how="all")`.
   - The first 5 rows of feature data ('sepal_len', 'sepal_wid', 'petal_len', 'petal_wid') are extracted for demonstration.

2. How to Calculate Correlation Among Features:
   - To calculate the correlation between features, use the pandas `.corr()` method.
   - Example:
     ```python
     correlation_matrix = iris_df.iloc[:, :4].corr()
     print("\nFeature Correlation Matrix:\n", correlation_matrix)
     ```
   - This calculates the pairwise correlation coefficients between the numerical feature columns.
   - The result is a symmetric matrix where:
       - Values close to **1** indicate a strong positive correlation.
       - Values close to **-1** indicate a strong negative correlation.
       - Values close to **0** indicate no linear correlation.

3. Importance of Correlation Analysis:
   - Helps identify relationships between features.
   - Useful for feature selection, dimensionality reduction, and data understanding in machine learning tasks.
"""