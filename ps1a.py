# House hunting
annual_salary = int(input('Enter your salary:'))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal:'))
total_cost = int(input('Enter the cost of your dream home:'))

current_savings = 0
portion_down_payment = 0.25
monthly_salary = annual_salary/12
i = 0
while current_savings < total_cost*portion_down_payment:
    # 每个月的收入的增加值
    monthly_increased = monthly_salary*portion_saved + current_savings*0.04/12
    current_savings = current_savings + monthly_increased
    i += 1

print('Number of months:', i)
