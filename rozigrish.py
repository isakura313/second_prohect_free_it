import random
spisok = ['bmw', 'audi', 'jigul', "suzuki"]

while True:
    print("Примите участие в розыгрыше")
    flag = input("y/n - y чтобы принять, n - отказаться:\n")
    if flag == "n":
        break
    if flag == "y":
        print(random.choice(spisok))