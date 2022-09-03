# this code changes even numbers of giving string value's letters to make upper,
# odd number of values to make lower

def func1(statement):
    last_string=""
    for index in range(len(statement)):
        if index %2 == 0:
            last_string += statement[index].upper()
        else:
            last_string += statement[index].lower()
    return print(last_string)
# or we could write this code differantly #


func1("ömer ali uygun")

def func2(string):
    last_string = ""
    for index, letter in enumerate(string):
        if index % 2 == 0:
            last_string += letter.upper()
        else:
            last_string += letter.lower()
    print(last_string)

func2("ömer ali uygun")

