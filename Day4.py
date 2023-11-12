# Make variables, long and samll
x=(2,3,4,5,6,9,0)
fruit_baskit=("Apple", "Mango", "Orange","Strawberries", "Kivi")
print(x)
print(fruit_baskit)

# in normal mathematic equation when we have a number with small bracket without any arithmatic sign it mean there will be multipication, but in Python we have to add "Multipication sign" otherwise function will not work or show an error.i.e
# b=(2+3-5*5(5+6)) this equation will not work becoz we didn't add multply sign between five and small bracket "5(5+6)" so correct mathod is as under;

b=(2+3-5*5*(5+6))
print(b)

num=(i for i in range (1-11))
print(num)

# to check data typr in python use this format/code
# print(type(variable name))
print(type(x))
print(type(fruit_baskit))
print(type(b))
print(type(num))

# Type Cast means to change the DATA type of a varible from one type to another, for exapmle X="15"is a string type variable but we want to change the String type to Int type, so we haveto use this code/formula
# x="5" is a string no multiply "x" to the required data type
x="5"
print(type(x))

x=int(x)
print(type(x))

# why to use Typecast ,mostly we use typecast to cahnge the float numbers "15.7" to Int numbers "15
a = (15.7)
print(type(a))
a = int(a)
print(type(a))

