#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
user_shet = 0
computer_shet = 0
choices = ["К", "Б", "Н"]

while True:
    user_choice = input("Выберите Камень[К] или Ножницы[Н] или Бумага[Б]: ")
    if user_choice not in choices:
        print("Некорректный выбор. Пожалуйста, выберите Камень[К], Ножницы[Н] или Бумага[Б].")
        continue
    computer_choice = random.choice(choices)
    print("Выбор компьютера:",computer_choice)
    if user_choice == computer_choice:
        print("Ничья")
    elif (user_choice == "К" and computer_choice == "Н") or (user_choice == "Н" and computer_choice == "Б") or (user_choice == "Б" and computer_choice == "К"):
        print("Вы выиграли")
        user_shet+=1
    else:
        print("Вы проиграли")
        computer_shet+=1
    print(f"Счет:\nПользователь - {user_shet}\nКомпьютер - {computer_shet}")
    if user_shet == 3:
        print("Поздравляем! Вы выиграли")
        break
    elif computer_shet == 3:
        print("К сожалению, Вы проиграли")
        break

