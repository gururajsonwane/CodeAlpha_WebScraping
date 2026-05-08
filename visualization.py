import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read csv file
df = pd.read_csv("books_data.csv")

# remove pound symbol
df["Price"] = df["Price"].str.replace("Â£", "")

# convert into float
df["Price"] = df["Price"].astype(float)

# rating count graph
sns.countplot(x="Rating", data=df)

# graph title
plt.title("Book Rating Count")

plt.savefig("rating_graph.png")
# show graph
plt.show()