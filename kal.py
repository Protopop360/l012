def kalk():
    pass
    print("Ноль в качестве знака операции завершит работу программы")
    while True:
      s = input("Знак:(+,-,*,/): ")
      if s == '0': break
      if s in ('+','-','*','/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
          print(x+y)
        elif s == '-':
          print(x-y)
        elif s == '*':
          print(x*y)
        elif s == '/':
          if y != 0:
            print(x/y)
          else:
            print("Деление на ноль!")
      else:
        print("Неверный знак операции!")
        input()