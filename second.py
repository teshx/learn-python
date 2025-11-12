print("Welcome to the table")
x = 5
y = 2
result = x // y
print("The result of", x, "*", y, "is", result)
print("Thank you for using the table program")

fruits = ["apple", "banana", "cherry"]
print("Available fruits:" , fruits[0], fruits[1], fruits[2])
fruits.insert(0,"date")
print("length of fruits list:", len(fruits))

print(dir(fruits))
print(fruits.count("apple"))

x = {
'name': 'Alice',
'age': 30,
'city': 'New York'
}
print(x)

c= "name" in x
print(c)

x = {1,2,3,4,5,3,2}
print(x)
# condtions
if 5 > 6:
    print("Five is greater than two!")
else:
    print("Two is greater than five!")
# loops


v=15
if v < 2:
    print("Value is less than 2")
elif v == 5:
    print("Value is equal to 5")
else:
    print("Value is greater than or equal to 2 and not equal to 5")


#check even odd
# num = int(input("Enter a number: "))
# print("You entered:", num)
# if num % 2 == 0:
#     print("The number is even.")
# elif num%2==1:
#     print("num is odd")
# else:
#     print("num is zero")

# for loop
for i in range(10, 50):
    print(i)
for i in range(100, 50 ,-1):
    print(i)

#combine for loop and if

for i in range(1 , 100):
    if i%3==0 and i%5==0:
        print(i,"fizzbuzz")
    elif i%5==0:
        print(i, "buzz")
    elif i%3==0:
        print(i,"fizz") 
    else: print("number", i)


    # while loop
x = input("Enter a number less than 10: ")
while x != "exit":
    print(x)
    x = input("Enter a number less than 10: ")