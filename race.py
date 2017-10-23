import random
def gonki():
	def easy(car):
		car["distance"]+= car["speed"]
		car["fuel"]-=car["expen"]


	def nitro(car):
		car["distance"] += car["nitro"]
		car["fuel"]-= car["expen"] * 2

	def tport(car):
		car["tport"] = random.randint(5,25)
		car["distance"] += car["tport"]
		car["fuel"]-= car["expen"] * 4



	def stats(car):
		print("\nТекущее состояние"+ car["name"]+
			" У тебя осталось оплива: "+ str(car["fuel"])+
			" Ты проехал"+ str(car["distance"]) + "/" + str(track),
			sep = "\n"
			)


	def step(car):
		choose = input("Твой ход, "+ car["name"]+ ". Выбирай с умом\n"
				"1- просто едем \n"
				"2- топим \n"
				"3-телепортируемся "
				)

		if choose == "1":
			easy(car)
		elif choose == "2":
			nitro(car)
		elif choose == "3":
			tport(car)
		else:
			print("Ты совершил ошибку")

		stats(car)


	track = 50




	car1 = {
		"name": "Бетмобиль",
		"speed": 6,
		"fuel": 30,
		"expen": 3,
		"nitro": 9,
		"distance":0
	}
	car2 = {
		"name": "Черная молния",
		"speed": 8,
		"fuel": 25,
		"expen": 4,
		"nitro":13,
		"distance":0
	}


	while True:
		step(car1)
		step(car2)
		if car1["distance"] >= track:
			print(car1["name"], "Ты выиграл")
		elif car2["distance"] >= track:
			print(car2["name"], "Ты выиграл")
		elif car1["fuel"] <= 0:
			print(car1["name"], "Кончилось топливо")
		elif car2["fuel"] <= 0:
			print(car2["name"], "Кончилось топливо")
			break

		input()