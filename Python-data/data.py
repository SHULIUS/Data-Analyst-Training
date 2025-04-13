import pandas as pd


# Create a DataFrame with some sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],}


new_data = pd.DataFrame(data)

# Display the DataFrame

print("data:" ,  new_data)
print("------------------------------")
print("headData", new_data.head(2))