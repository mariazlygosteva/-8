sum_income = 0
num_citizens = 0
income = float(input())

while income != 0:
    sum_income += income
    num_citizens += 1
    income = float(input())

if num_citizens == 0:
    print("Нет данных о доходах жителей")
else:
    average_income = sum_income / num_citizens
    print(average_income)