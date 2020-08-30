#программа приветствует человека
#спрашивает имя и фамилию, и привествует по имени
#и фамилии

print("Привет, как у тебя дела? Представься ")
name = input("Введите ваше имя: \n")
surname = input("Введите вашу фамилию: \n")
name = name.strip()
surname = surname.strip()
print(f'Привет {name.capitalize()} {surname.capitalize()}, рад вас видеть')