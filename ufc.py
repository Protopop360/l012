import random 
def  ufcc():
	def creat_fighter():
		person = {"Сила": 100, "Выносливость": 1000}
		person["Имя"] = input("Введи имя, боец ")
		choose = input("""
1- прирост к силе
2-прирост к выносливости
3.кидать снежок 
4.Бросить на прогиб
			""")
		if choose == 1 :
			person["Сила"] = random.randint(10,100)
		elif choose == 2 :
			person["Выносливость"] = random.randint(400,500)
		elif choose == 3 :
			person["Сила"] = 1000
		else:
			person["Сила"] = random.randint(10,500)

		return person

	def attack(attacker, defender):
		print("Игрок", attacker["Имя"], "Нанес", attacker["Сила"], "урона")
		defender["Выносливость"] -= attacker["Сила"]

	person1 = creat_fighter()
	person2 = creat_fighter()

	print(person1)
	print(person2)

	while True:
		attack(person1,person2)
		attack(person2,person1)
		print("У игрока", person1["Имя"], "осталось", person1["Выносливость"])
		print("У игрока", person2["Имя"], "осталось", person2["Выносливость"])
		input()
		if person1["Выносливость"] <= 0:
			print( person1["Имя"], "Ты проиграл")
			break
		elif person1["Выносливость"] == person2["Выносливость"]:
			print("У вас ничья")
		elif person2["Выносливость"] <= 0 :
			print(person2["Имя"], "Ты проиграл")
			break