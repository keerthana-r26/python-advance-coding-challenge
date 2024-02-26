print("hello")
# a= int(input("enter a number"))
# b= int(input("enter b number"))
# print("the sum is:", a+b)
# print("the remainder is:",a-b)
# print("multiple is:",a*b)
# print("the solution after division is:", a/b)

# c= int(input("enter c number"))
# print("the sum of three number is ",a+b+c)
# print("the multiple  of the 3 number is",a*b*c)
"""n = int(input('enter a num of ur choice:'))
i = 0
for i in range(0, n):
    if n % 2 == 0:
        print('nice')
    else:
        print('good')"""

"""array = list(
    map(int, input("Enter elements of the array separated by spaces: ").split()))
array.sort()
print("Sorted Array:", array)"""

arr = [10, 5, 9, 45, 782, 1, 10]
arr.sort()
print(arr)
arr.reverse()
print(arr)

x = 5
y = "John"
print(type(x))
print(type(y))

"""
# Get input from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")"""

"""
# slicing
a = [10, 20, 15, 6, 4, 5]
print(a[:3])

arr = [10, 20, 3, 2, 15]  # using slice function
a = slice(0, 3)
print(arr[a])

# append() function
li = [2, 5, 6]
li.append(5)
print(li)
li.append("hithere!")
print(li)
li1 = (5, 7, 8)
li.append(li1)
print(li)
"""

"""
def add_even_number(lst):
    even_number = []
    for i in lst:
        if i % 2 == 0:
            even_number.append(i)
    return even_number


inp = input("enter elem")
lst1 = list(map(int, inp.split()))
result = add_even_number(lst1)
print(result)
"""

"""
def filter_and_append(lst):
    new_string = []
    for i in lst:
        if len(i) > 5:
            new_string.append(i)
    return new_string


strng = input("enter the string")
input_string = strng.split()
new_list = filter_and_append(input_string)
print(new_list) """


def square_and_append(lst):
    squared_nums = []
    for i in lst:
        squared_nums.append(i ** 2)
    return squared_nums


inp = input("enter elem")
lst1 = list(map(float, inp.split()))
result = square_and_append(lst1)
print(result)
