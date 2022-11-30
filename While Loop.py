a = 1
while a <= 10:
    print(a)
    a = a + 1

a = 1
num = 100  # int(input("Enter a number till where you to print counting and its sum"))
while a <= num:
    print(a)
    a = a + 1
a = 1
sum = 0
num = 5 #nt(input("Enter a number = "))
while a <= num:
    print(a)
    sum = sum + a
    a = a+1
print("sum of number is:",sum)

i = 1
while i < 6:
    print(i)
    #i = 1+i
    if(i==3):
        break
    i += 1
print("Out of the loop")

j = 1
while j < 6:
    print(j)
    if(j==3):
        j += 1
        continue
    j += 1
print("Out of the loop")

k = 1
while k <= 10:
    print(k)
    if(k==9):
        break
    k += 2
print("Out of the loop")

l = 2
while l <= 10:
    print(l)
    if(l==10):
        l += 2
        continue
    l += 2
print("Out of the loop")

a = 75
b = 50
print(a+b)
if((a+b)>100):
    print("To Big")
#For Loop
thesum = 0
for count in range(1,11): #by fault it starts from 1 for loop variable and goes to 10 for 11 and goes to 11 for 12
    thesum +=count
print(thesum)

thesum = 0
for count in range(1,11):
    print(num,"*",count,"=",num*count)
  #  thesum+=count
#print(thesum)
#i = int(input(4))

items = "python"
index = 0
for item in items:
    print(index,item)
    index += 1
    print("\n")

fruit = 'apple'
i = 0
index = 0
while i < len(fruit):
    print(index, fruit[i])
    i = i + 1
    index +=1

num = 12345
reverse_num = 0
while num != 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num //=10
print("Reversed Number: " + str(reverse_num))

last_number = int(input("number of sums: "))
a = 0
b = 1
sums = 0
while sums < last_number:
    print(a)
    nth = a + b
    a = b
    b = nth
    sums += 1

#firstTerm = int(input("Enter the first Term of AP series"))
#commonDifference = int(input("Enter commonDifference for AP series"))
#totalTerms = int(input("Enter total terms"))
#currentvalue = firstnum
#for i in range(0,totalTerms):
 #   print(currentvalue,end=' ')
#currentValue = currentvalue+commonDifference

#nested loop
#outer loop
for i in range(1,5):
    for j in range(1,5):
        print(i,j,end ="\n")

print("Now print table using nested loop","\n")
for i in range(1, 11):
    #to iterate from 1 to 10
    for j in range(1,11):
        #print multiplication
        print(i * j,end=' ')
    print()

lower_value=int(input("Enter the lowwr value"))
upper_value=int(input("Enter the upper value"))
print("The Prime numbers in the range are: ")
for number in range(lower_value,upper_value + 1):
    if number > 1:
        for i in range(2,number):
            if(number%i) == 0:
                break
        else:
            print(number)

import random
for i in range(1):
   # random.randint(1,10)
    a = (random.randint(1,100))
    print(a)
num = 80
if num > a:
    print("Too large")
else:
    print("Too small")
if num == a:
    print("Congrats!_____ In 6th attempt you found it")






