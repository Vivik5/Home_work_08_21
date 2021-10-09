# 1.
string_tuples = [(input("Введите данные: "))]
def join_tuple_string(strings_tuple) -> str:
   return ' ,'.join(strings_tuple)
result = map(join_tuple_string, string_tuples)
print(list(result))

# 2.
p_numbers = [1, 3, 5, 6]
numbers = p_numbers.copy()
print('Copy List:', numbers)

# 3. 
lis = [[2, 5, 6], [5, 7, 1], [3, 6, 7, 34, 7, 0], 5]
for y in range(len(lis)):
    if type(lis[y]) != type([]):
        print(lis[y])
        continue
    for x in range(len(lis[y])):
        print(lis[y][x])

# 4. 
a = [5, 10, 15, 20, 25]
def func(list):
    return [list[0], list[-1]]
print(func(a))

# 5.
list1=[2, 3, 5, 6, 7]
emptyList=[]
emptyList.append(5)
emptyList.append(-6)
emptyList += list1
emptyList.sort()
print(list1)
print(emptyList)

# 6. 
str = input("Введите данные: ")
print(list(str.replace(" ","")))

# 7. 
lis = ["Андрей", "Иван", "Василий", "Петро", "Максим", "Дима"]
for b in lis:
    print(b)
    for c in b:
        print(c)

# 8. 
lis = [1, 34, 8, 0, -5, 7, 32, 74, 59, 92, 41, 10, -2]
minus = min(lis)
lis.remove(minus)
if minus < 0:
    lis.append(minus)
else:
    lis.insert(0, min)
print(lis)

# 9. 
some = [9, "Hi", 23.5, "A"]
N = int(input("Введите число: "))
some.append(N)
print(some)

# 10. 
list = [3.4, 56, "Some", "Hi", 7, 3.8, 44, 45, 46]
print(list[2:len(list)-1:3])

# 11. 
list = [3.4, 56, "Some", "Hi", 7, 3.8, 44]
print(list[-3])
