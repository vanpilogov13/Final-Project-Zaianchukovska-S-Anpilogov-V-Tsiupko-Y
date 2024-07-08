# Final Project - Operational Margin Calculator
## Overview

## Functions
### 1. main_menu()
After starting the program the user can choose between three options: check existing information, Add a new data source and calculate metric. 
### 2. check_existing_information()
The application shows the names of the last three added data sources and their metrics.
### 3. add_new_data_source()

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

