# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
k = int(input("Введите количество долек, которое нужно отломить: "))

if k <= n * m and (k % n == 0 or k % m == 0):
 print("Можно отломить указанное количество долек")
else:
 print("Нельзя отломить указанное количество долек")