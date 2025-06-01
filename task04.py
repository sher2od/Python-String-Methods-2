template = "Bugun {day} kuni, dars soati {hour} da."

day = input()
hour = int(input())

result = template.format(day = day,hour = hour)

print(result)