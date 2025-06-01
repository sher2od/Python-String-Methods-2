temaplate = "{n1} + {n2} = {calculation}"

n1 = int(input("1-son"))
n2 = int(input("2-son"))

calculation = n1 + n2

result = temaplate.format(n1 = n1,n2 = n2,calculation = calculation) 

print(result)
