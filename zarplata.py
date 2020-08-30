# справшивает, сколько людей в семье
# потом по очереди спрашивает, сколько зарабатывает кто
# после этого у нас происходит подсчет
how = input("Сколько у вас членов семьи, которые работают?")
how_not_working = int(input("Сколько у вас членов семьи, которые не работают?"))
how = int(how)
spisok_salary = []
amount = 0

for i in range(1, how+1):
    sum = int(input(f'Сколько у вас зарабатывает {i} член семьи? '))
    spisok_salary.append(sum)
print(spisok_salary)

for zarplata in spisok_salary:
    amount += zarplata

print(f"В итоге каждый член семьи может тратить {amount/how_not_working}")
