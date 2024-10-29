# Constants for Sales Manager Position
MIN_YRS_SALES = 2
MIN_YRS_TOP_AWD = 1

years_sales = int(input('Enter your years of sales experience: '))
yrs_top_awd = int(input('Enter how many years you have been salesperson of the year: '))

if years_sales >= MIN_YRS_SALES and yrs_top_awd >= MIN_YRS_TOP_AWD:
    print('Congratulations! You are eligible for the Sales Manager Position.')
else:
# Multi-line with f-string.
    print(f'''
Sorry, you do not meet the requirements for the Sales Manager Position.

You need at least:
- {MIN_YRS_SALES} years of sales experience
- {MIN_YRS_TOP_AWD} years as salesperson of the year
''')