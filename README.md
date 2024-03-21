# Marvel Mart Data Analysis Project

## Overview

This project was developed as part of a comprehensive data analysis exercise focusing on the sales data of Marvel Mart, a renowned department store chain with global operations. The primary goal was to apply data cleaning techniques, perform exploratory data analysis (EDA), and generate insightful reports and visualizations to aid business decision-making processes. 

## Project Objectives

- **Data Cleaning**: Identify and rectify missing or incorrect entries in the dataset to prepare a clean, reliable dataset for analysis.
- **Exploratory Data Analysis**: Conduct a thorough analysis to uncover trends, patterns, and anomalies within the sales data.
- **Report Generation**: Provide actionable insights through detailed reports and visualizations that support strategic business decisions.

## Tools and Libraries Used

- **Python**: The core programming language for the project.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical computing and array manipulation.
- **Matplotlib & Seaborn**: For data visualization and creating insightful charts and graphs.

## Dataset

The project utilizes `MM_Sales.csv`, a dataset provided by Marvel Mart containing sales records across various countries, including information such as country, item type, sales channel, order priority, unit cost, total revenue, total cost, and total profit.

## Methodology

### Part 1: Cleaning the Data

1. **Identify Missing Data**: Employed Python scripts to detect missing values across multiple columns including 'Country', 'Item Type', 'Order Priority', and 'Order ID'.
2. **Rectify Data Anomalies**: Corrected erroneous entries by replacing invalid text entries with "NULL" and non-numeric values with zeroes or appropriate placeholders.
3. **Dataframe Preparation**: Generated a clean, processed DataFrame, `MM_Sales_clean.csv`, free from inaccuracies and ready for analysis.

### Part 2: Exploratory Data Analysis with Reports & Visualizations

1. **Country Rankings**: Identified the top 10 countries based on sales volume to strategize on new shipping center locations.
2. **Sales Channel Analysis**: Analyzed the distribution of online and offline orders and visualized the data using pie charts.
3. **Item Type Profitability**: Created boxplots to explore the distribution of total profits by item type and ranked the top 3 most profitable item types.
4. **Descriptive Statistics**: Computed and reported sum, average, and maximum values for 'Units Sold', 'Unit Cost', 'Total Revenue', 'Total Cost', and 'Total Profit'.

### Part 3: Cross-Reference Statistics

Compiled a list of regions with corresponding countries to facilitate geographical analysis and strategic planning.

## Results

- **`Marvel_Mart_Rankings.txt`**: Text file summarizing sales rankings, online vs. offline orders, order priorities, and top-selling items.
- **`Marvel_Mart_Calc.txt`**: Text file detailing calculated statistics such as total sales, average unit cost, and total profits by item type.
- **Visualizations**: Produced various charts and plots to visually represent analysis findings, aiding in the interpretation of complex data.

## Running the Project

To execute the analysis:

1. Ensure Python 3.x and necessary libraries (pandas, numpy, matplotlib, seaborn) are installed.
2. Run the script: `python Nguyen_Project2.py`.

## Contributions and Acknowledgments

This project was made possible by the data provided by Marvel Mart and the guidance received from Seattle University's project instructions. It stands as a testament to the power of data analysis in driving business insights and strategic decisions.


