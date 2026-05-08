import pandas as pd

# read csv file
df = pd.read_csv("books_data.csv")

# remove pound symbol
df["Price"] = df["Price"].str.replace("Â£", "")

# convert price into float
df["Price"] = df["Price"].astype(float)

# first 5 rows
print(df.head())

# highest price
print("\nHighest Price:")
print(df["Price"].max())

# lowest price
print("\nLowest Price:")
print(df["Price"].min())

# average price
print("\nAverage Price:")
print(df["Price"].mean())

# rating count
print("\nRating Count:")
print(df["Rating"].value_counts())


