############### funckje ############################
def zadanie1(a_list = [], b_list = []):
    list = []
    for index, x in enumerate(a_list):
        if (index%2 == 0):
            list.append(x)
    for index, x in enumerate(b_list):
        if (index%2 != 0):
            list.append(x)
    return list

def zadanie2(data_text = ""):
    letters = []
    for i in data_text:
        letters.append(i)
    result = {}
    result = dict([("lenght", len(data_text)), ("letters", letters), ("big letters", data_text.upper()), ("small letters", data_text.lower())])
    return result

def zadanie3(text = "", letter = ''):
    result = ""
    for i in text:
        if not (i == letter):
            result += i
    return result

def zadanie4(temp, temperature_type):
    if (temperature_type == 'C'):
        print(temp, "*C = ", temp, "*C")
    elif (temperature_type == 'F'):
        print(temp, "*C = ", 32+(9*temp)/5, "*F")
    elif (temperature_type == 'R'):
        print(temp, "*C = ", (9*(temp+273))/5, "*R")
    elif (temperature_type == 'K'):
        print(temp, "*C = ", temp+273, "*K")
    else: print("Błędny parametr, prawidłowe to: C, F, R lub K")

def zadanie7(text = ""):
    result = text[::-1]
    print(result)



####################################################
# definicje
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

# realizacjia
#print("zadanie 1: ", zadanie1(list1, list2))
#print(zadanie2("Karol Kulesza"))
#print(zadanie3("Karol Kulesza", 'a'))
#zadanie4(110, 'F')
#zadanie7("Karol")