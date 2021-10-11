#Home Work №9
#https://www.codewars.com/kata/sum-of-odd-numbers/train/python
def row_sum_odd_numbers(n):
    return n ** 3

#https://www.codewars.com/kata/array-plus-array/train/python
def array_plus_array(arr1,arr2):
    pass
    return sum(arr1) + sum(arr2)

#https://www.codewars.com/kata/students-final-grade/train/python
def final_grade(exam, projects):
    if exam > 90 and projects >= 10:
        return 100
    if exam > 75 and projects >= 5:
        return 90
    if exam > 50 and projects >= 2:
        return 75
    else:
        return 0


#https://www.codewars.com/kata/beginner-series-number-3-sum-of-numbers/train/python
def get_sum(a, b):
    return sum(xrange(min(a,b), max(a,b)+1))


#https://www.codewars.com/kata/beginner-series-number-4-cockroach/train/python
def cockroach_speed(s):
    return int(s * 27.7778)


#Home Work №8
#https://www.codewars.com/kata/57eae20f5500ad98e50002c5/train/python
def no_space(x):
    for i in range(len(x)-1, -1, -1): # loop in reverse order
        if x[i] == " ":
            x = x[:i] + x[i+1:]
    return x
def no_space(x):
    return x.replace(' ' ,'')

#https://www.codewars.com/kata/563a631f7cbbc236cf0000c2/solutions/python
def move(position, roll):
    positionNew = position + (2*roll)
    return(positionNew)


#https://www.codewars.com/kata/591588d49f4056e13f000001/train/python
def HQ9(code):
    if code == "H":
        return "Hello World!"
    if code == "Q":
        return "Q"
    if code == "9":
        result = ""
        for n in range(99,2,-1):
            result += f"{n} bottles of beer on the wall, {n} bottles of beer.\nTake one down and pass it around, {n-1} bottles of beer on the wall.\n"
        result += "2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall."
        return result
    return None


#https://www.codewars.com/kata/101-dalmatians-squash-the-bugs-not-the-dogs/train/python
def how_many_dalmatians(n):
  dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
  if n <= 10: return dogs[0] 
  if n <= 50: return dogs[1] 
  if n == 101: return dogs[3]
  return dogs[2]


#https://www.codewars.com/kata/5a023c426975981341000014/train/python
def other_angle(a, b):
    return 180 - (a + b)
