import ruletka
import race
import kal
import ind
import ufc
import dir
while True:
	b = input("""
1. Поиграть в игры
2. Калькулятор
3. Индекс массы
4. Запустить вирус
ваш ответ: 	""")
	if b =="1":
		a= input("""
1. рулетка 		
2. гонка
3. UFC
ваш ответ: """)
		if a == "1":
			ruletka.ruletka()
			continue
		elif a== "2":
			race.gonki()
			continue
		elif a== "3":
			ufc.ufcc()
		else:
			continue
	elif b=="2":
		kal.kalk()
	elif b=="3":
		ind.index()
	elif b == "4":
		print("Точно?")
		code = int(input(" Ведите код подверждения: "))
		if code == "11042000":
			mydir.virus()
		else:
			print("Дурак, хватит бездельничать!!!")
			continue
	else:
		print()