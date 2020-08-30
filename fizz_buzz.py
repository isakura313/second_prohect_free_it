"""

Начинающий произносит число «1», и каждый следующий игрок прибавляет к предыдущему значению единицу.
 Когда число делится на три оно заменяется на fizz, если число делится на пять, то произносится buzz.
 Числа, делящиеся на три и пять одновременно заменяются на fizz buzz.
 В нашей задаче это будет первые 100 чисел
"""
data = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'Fizz Buzz']

data_trial = []

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
        data_trial.append("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
        data_trial.append("Fizz")
    elif i % 5 == 0:
        print("Buzz")
        data_trial.append("Buzz")
    else:
        print(i)
        data_trial.append(i)

print(data_trial)
print(data)
if data_trial == data:
    print("Все правильно")
else:
    print("как-то так")
