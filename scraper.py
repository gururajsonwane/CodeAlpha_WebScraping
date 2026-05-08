# Import requests library
# This library helps us connect to websites
import requests

# Import BeautifulSoup from bs4
# BeautifulSoup helps us read and understand website HTML code
from bs4 import BeautifulSoup

# Import pandas library
# Pandas helps us create tables and CSV files
import pandas as pd


# Create an empty list
# We will store all scraped book data inside this list
data = []


# Loop through pages from 1 to 5
# This means the scraper will visit 5 pages
for page in range(1, 6):

    # Create website URL dynamically
    # Example:
    # page 1 -> page-1.html
    # page 2 -> page-2.html
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    # Send request to website
    # This downloads the webpage content
    response = requests.get(url)

    # Parse the website HTML using lxml parser
    # BeautifulSoup helps us read website structure
    soup = BeautifulSoup(response.text, "lxml")

    # Find all book sections from the webpage
    # Each book is inside:
    # <article class="product_pod">
    books = soup.find_all("article", class_="product_pod")

    # Loop through every book found on the page
    for book in books:

        # Get book title
        # Example: "Sapiens"
        title = book.h3.a["title"]

        # Get book price
        # Example: £51.77
        price = book.find("p", class_="price_color").text

        # Get book rating
        # Example: One, Two, Three, Four, Five
        rating = book.p["class"][1]

        # Store book data inside dictionary format
        # Then add it to the data list
        data.append({
            "Title": title,
            "Price": price,
            "Rating": rating
        })


# Convert list data into table format
# DataFrame works like Excel table
df = pd.DataFrame(data)

# Save table into CSV file
# index=False removes extra numbering column
df.to_csv("books_data.csv", index=False)

# Print success message
print("Scraping Completed!")

# Print total number of books scraped
print("Total Books:", len(df))

# Print first 5 rows of data
print(df.head())