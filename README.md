# Final Project - Operational Margin Calculator
## Overview
This program allows you to upload files in csv format, read them and calculate indicators based on the data found in the tables

From the added additional features:
- added function to normalize column names, because some of them have spaces, confusing registers, etc.
- the program clears the console, which makes using it more pleasant
- added function for automatic search of necessary columns, if the program doesn't find them, it asks for their names.
- added validation for loading existing files to avoid errors

## Functions
### 1. main_menu()
After starting the program the user can choose between three options: check existing information, Add a new data source and calculate metric. 
- Added by Zaianchukovska
### 2. check_existing_information()
The application shows the names of the last three added data sources and their metrics.
- Added by Zaianchukovska 
### 3. add_new_data_source()
Allows files to be uploaded to the program and validates for the correct file path and whether the file has already been uploaded
- Added by Tsiupko
### 4. norm_column_name(column_name):
"normalizes" table column names, removes extra spaces and allows you to ignore upper / lower case
- Added by Anpilogov 
### 5. find_column(columns, column_name):
Automatic search for required columns in the table for auto-calculation
- Added by Anpilogov
### 6. select_data_source(stdscr): // print_menu(stdscr, current_index):
Allows you to use the keyboard arrows to make a selection in the file selection menu for processing
- Added by Tsiupko
### 7. calculate_metric():
Pulls the necessary data from the spreadsheets and calculates Operational margin
- Added by Anpilogov
### 8. main():
Responsible for menu selections
- Added by Zaianchukovska


## Test Plan
### Normal flow
/Users/alien_vladimir/Downloads/final project.py

Select action:
1. Check existing information
2. Add a new data source (file)
3. Calculate metric
4. Exit
Choose your action: 2

Enter data source: /Users/alien_vladimir/Downloads/GOOG annual income statement.csv
Datasource structure:
date | symbol | reportedCurrency | cik | fillingDate | acceptedDate | calendarYear | period | revenue | costOfRevenue | grossProfit | grossProfitRatio | researchAndDevelopmentExpenses | generalAndAdministrativeExpenses | sellingAndMarketingExpenses | sellingGeneralAndAdministrativeExpenses | otherExpenses | operatingExpenses | costAndExpenses | interestIncome | interestExpense | depreciationAndAmortization | ebitda | ebitdaratio | operatingIncome | operatingIncomeRatio | totalOtherIncomeExpensesNet | incomeBeforeTax | incomeBeforeTaxRatio | incomeTaxExpense | netIncome | netIncomeRatio | eps | epsdiluted | weightedAverageShsOut | weightedAverageShsOutDil | link | finalLink | lastRetainedEarnings | stockRepurchases | dividendsPaid | otherDistributions | retainedEarnings | grossPPE | annualDepreciation | capitalExpenditure | netPPE | lastGoodwill | acquisitionsAndAdjustments | goodwill
Total records: 4

Select action:
1. Check existing information
2. Add a new data source (file)
3. Calculate metric
4. Exit
Choose your action: 1

Existing Data Sources:
1) Datasource: GOOG annual income statement.csv | Metric: Not calculated

Select action:
1. Check existing information
2. Add a new data source (file)
3. Calculate metric
4. Exit
Choose your action: 3

Select data source to calculate metric:
> GOOG annual income statement.csv

Enter the name of the revenue column: Revenue
Found revenue column: Revenue

Enter the name of the operating income column: operatingIncome
Found operating income column: operatingIncome

Selected data source: GOOG annual income statement.csv | Total records: 4
Congratulations! Your operational margin was calculated. Value is: 27.08%

Select action:
1. Check existing information
2. Add a new data source (file)
3. Calculate metric
4. Exit
Choose your action: 4

Thank you for using me!
Authors: Zaianchukovska S. // Anpilogov V. // Tsiupko Y.

### Validation
- Menu Choice Validation
- File Path Validation
- Duplicate File Validation
- Column Name Validation

### Example Outputs
- Menu
<img width="479" alt="Screenshot 2024-07-08 at 05 28 10" src="https://github.com/vanpilogov13/Final-Project-Zaianchukovska-S-Anpilogov-V-Tsiupko-Y/assets/169614450/e56da747-990e-47f2-aaf0-42b7e7e049c2">

- Checking Existing Information
<img width="620" alt="Screenshot 2024-07-08 at 05 31 53" src="https://github.com/vanpilogov13/Final-Project-Zaianchukovska-S-Anpilogov-V-Tsiupko-Y/assets/169614450/8a02e1fc-7433-42cf-bb22-804e6f50eb15">

- Adding a New Data Source
<img width="563" alt="Screenshot 2024-07-08 at 05 29 26" src="https://github.com/vanpilogov13/Final-Project-Zaianchukovska-S-Anpilogov-V-Tsiupko-Y/assets/169614450/ce44c463-c9ac-4a80-93dd-445945afaf96">

- Сalculating Metric
<img width="309" alt="Screenshot 2024-07-08 at 05 30 22" src="https://github.com/vanpilogov13/Final-Project-Zaianchukovska-S-Anpilogov-V-Tsiupko-Y/assets/169614450/21a369ac-4490-47b0-944f-292bdadb85ed">
<img width="533" alt="Screenshot 2024-07-08 at 05 30 36" src="https://github.com/vanpilogov13/Final-Project-Zaianchukovska-S-Anpilogov-V-Tsiupko-Y/assets/169614450/6f74f112-2d8f-4c0c-888d-ecc4b68218c0">

## Conclusion
This version of the program is quite stable and optimized for comfortable user-friendly work with files and auto-calculation of operational margin, which makes our team happy with the result :)
