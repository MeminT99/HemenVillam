# Villa Rental Scraping Project

## Project Overview

This project focuses on scraping rental villa data from multiple websites to address the problem of duplicate listings across different rental firms. These duplicates lead to inefficiencies and confusion for renters and firms alike. By collecting and analyzing this data, the project helps identify duplicate villas across different platforms, giving firms insights into how many of their listings are redundant across websites. 

The project consists of 15 Jupyter Notebooks, each dedicated to scraping data from one of the 15 websites, and several supporting scripts for processing and analyzing the data.

# Project documentation

### Notebooks
- **15 Notebooks**: Each notebook is dedicated to scraping data from a specific website. These notebooks extract villa information such as villa features, rental prices, and availability.

### Data
- **`database.xlsx`**: This is the master file containing all the scraped villa data from the 15 websites, including duplicates (17,860 records).
- **Website-specific Excel files**: Each website's scraped data is stored in separate Excel files.
- **`report.xlsx`**: This report provides insights into the number of duplicate villa listings and which firms have the most duplicates.

### Scripts
- **`analysis.py`**: This Python script analyzes the villa data to:
  - Identify duplicate villas across different firms.
  - Generate a report showing how many villas each firm has and how many are duplicates.

### Requirements
- **`requirements.txt`**: A text file containing the libraries required for running the project (such as BeautifulSoup for web scraping, Pandas for data analysis, etc.).

## Usage

### Scraping Villa Data
1. Open any of the Jupyter Notebooks in the **notebooks/** folder.
2. Each notebook is dedicated to scraping data from a specific website. Follow the instructions inside the notebook to collect the data.
3. The output will be an Excel file containing the scraped villa data for that particular website.

### Data Analysis
1. After collecting the data, navigate to the **scripts/** folder.
2. Run the `analysis.py` script to analyze the scraped villa data and identify duplicates.
3. This script will generate a report.xlsx file located in the data/ folder, which will provide insights into duplicate villas across different firms.

### View the Results
1. After running the `analysis.py` script, open the **report.xlsx** file located in the **data/** folder.
2. The report will provide the following insights:
   - **Number of Duplicate Villas**: Displays how many villas are listed by multiple firms.
   - **Percentage of Duplicates for Each Firm**: Shows the proportion of a firm's villas that are duplicated across other platforms.
   - **Firm Performance Insights**: Highlights the performance of each firm, including how many of their villas are listed elsewhere and the extent of duplication.



