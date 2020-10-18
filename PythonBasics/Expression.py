x = 4
y = 7
z = 10
# Below line is expression how expression works
equation = x + y / z ** x / z * x * x + 4 - 2 / 3
print('The equation value : ', equation)

equation = x + y / z ** x / (z * x * x + 4) - (2 / 3)
print('After parenthesis equation value : ', equation)

fruit = 'banana'
print(len(fruit))
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index += 1
s = print(fruit[0:5])
print(fruit[3:3])
s = print(fruit[:])
