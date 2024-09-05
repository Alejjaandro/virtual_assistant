import pandas as pd

# Extract information from NASDAQ-100
url_nasdaq = "https://en.wikipedia.org/wiki/NASDAQ-100"
# Create a table of pandas with the information from the page
nasdaq_tables = pd.read_html(url_nasdaq)
# Select the table with the names of the companies
nasdaq_companies = nasdaq_tables[4]
# Create a dictionary with the names of the companies and their codes
stocks_info = nasdaq_companies.set_index('Company')['Ticker'].to_dict()
# Change the names of the keys of the dictionary to lower case
stocks_info = {key.lower(): value for key, value in stocks_info.items()}
# Change the name of the key of Alphabet to google
stocks_info['google'] = stocks_info.pop('alphabet inc. (class a)')
stocks_info.pop('alphabet inc. (class c)')