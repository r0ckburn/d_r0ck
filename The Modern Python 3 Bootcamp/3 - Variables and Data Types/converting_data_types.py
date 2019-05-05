# when using string interpolation, data types are implicitly converted into string form
# you can also explicitly convert variables by using the name of the builtin type as a function

# converting a float to an int

decimal = 12.56345634534
integer = int(decimal) 
print(integer) # 12

# converting a list to a string

my_list = [1, 2, 3]
my_list_as_a_string = str(my_list)
print(my_list_as_a_string) # [1, 2, 3]

# changing the data type from int to float

num = 12
type(num) # will show that 12 is an int
num = float(num)
type(num) # after converting, will show that 12 is a float and display "12.0"