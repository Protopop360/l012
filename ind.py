def index():
	height =float(input("ваш рост"))
	weight =int(input("ваш вес"))

	i= weight/(height**2)
	print(i)
	if i<15:
		print("дефецит массы тела")
	elif 15<=i<20:
		print("Нехватка массы тела")
	elif 20<=i<25:
		print("Норма")
	elif 25<=i<30:
		print("небольшой перевес")
	elif i>30:
		print("Ожирение")