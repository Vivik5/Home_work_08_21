#1.
for x in range(5,57):
            if (x == 57): break
            if (x == 34): continue
            if (x == 46): continue
            if (x == 52): continue
            print(x)

#2.
summ = 0
a = 1
while a <= 100:
    if a % 4 == 0:
        summ += a
    a += 1
print(summ)

#3.
decrypted_characters = ['13, 12, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1']
decrypted_word = ' ,'.join(decrypted_characters)
print(decrypted_word)

#4.
n = int(5)
count = 1
while count <= 10:
    print(f"{count} x {n} = {n * count}")
    count = count + 1
#5.
i = 34
while i <= 67:
	if i % 2 != 1:
		print (i)
	i += 1

#6.
a = 10
while True:
	a -= 1
	if a == 0:
		break

#7.
for x2 in range(1,100):
     if (x2 == 100): break
     if (x2 == 50): continue
     if (x2 == 99): continue
     print(x2)
