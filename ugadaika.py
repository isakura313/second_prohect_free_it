import random
rand = random.randint(1, 30)
count = 0
while True:
    predict = input("Попробуйте угадать число от 1 до 30:\n")
    if int(predict) == rand:
        print("Отлично, вы угадали!")
        break
    elif count == 9:
        print("game over", "Настоящие число было", rand)
        break
    else:
        print("Видимо нет... попробуйте еще раз")
        count += 1