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