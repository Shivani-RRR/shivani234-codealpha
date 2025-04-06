import requests
from bs4 import BeautifulSoup

# Step 1: Get the content of the webpage
url = 'https://www.example.com'
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Page retrieved successfully!")
else:
    print("Failed to retrieve page.")
# Step 2: Parse the page content
soup = BeautifulSoup(response.content, 'html.parser')

# Print the parsed HTML to inspect the structure
print(soup.prettify())
# Step 3: Find specific elements (e.g., extract all the headings)
headings = soup.find_all('h2')  # Finds all <h2> tags

# Extract text from each heading
for heading in headings:
    print(heading.get_text())

import csv

# Step 4: Save data to CSV
with open('D:\python\students_details.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Heading'])
    for heading in headings:
        writer.writerow([heading.get_text()])

