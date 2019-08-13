birth_year = input('Birth year? ')
print(type(birth_year)) ## this will tell you type of variable, this is str right now (optional)
age = 2019 - int(birth_year) ## we cant subtract birth_year from 2019 becuase 2019 is int and birth_year is str ( by default every user input is a string.
print(type(age)) ## Again this will print type of variable which would be converted ad int (optional)
print(age)