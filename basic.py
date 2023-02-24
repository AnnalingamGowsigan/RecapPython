# variables
student_count = 10
rating = 12.97
isMale = True
msg = "Hello world"
print(type(rating))

# string related function
print(len(msg))
print(msg[1])

# concatinate
first = "Annalingam"
last = "Gowsigan"
full = first + " "+last
print(f"My fullname is {full}")
print("numerical representation of A is " + str(ord("A")))

# conditional statements
num = 5
if (num == 5):
    print("It is equal to 5")
elif (num == 3):
    print("It is equal to 3")
else:
    print("not")

print(5 and 5 or not 4)

# loop
for number in range(2, 18, 2):
    print("number is ", number)

for char in "python":
    print("character is ", char)

for n in [1, 2, 3, 4, 5]:
    print("n is ", n)

print(type(range(3)))  # complex type

i = 0
while i <= 5:
    print("Hi")
    i = i + 1
