import random
rand = random.randint(1, 30)
count = 0
while True:
    print("У вас только 6 попыток")
    predict = int(input("Попробуйте угадать число от 1 до 30:\n"))
    if predict == rand:
        print("Отлично, вы угадали!")
        break
    elif count == 6:
        print("game over", "Настоящие число было", rand)
        break
    elif predict > rand:
        print("меньше возьми")
        count += 1
    elif predict < rand:
        print("больше возьми")
        count += 1
    else:
        print("Видимо нет... попробуйте еще раз")
        count += 1