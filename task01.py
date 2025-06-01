temalate = "Salom  maning ismim {name} va yoshim {age} da"


name = input()
age = int(input())


result = temalate.format(name=name, age=age)

print(result)

