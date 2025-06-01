template = "Fayil: {fayil}.{format}"

fayil = input()
format = input()

result = template.format(fayil=fayil,format=format)

print(result)