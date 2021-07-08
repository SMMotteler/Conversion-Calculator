# 3 parameter (value,original unit, desired unit)
# dictionary of the units and the conversion values ={}
# value*desired unit/original unit
# return value
conversions_length = {
    "inches" : 1,
    "feet" : 1/12,
    "yards" : 1/36,
    "miles" : 1/63360,
    "meters" : 1/39.3701,
    "kilometers": 1/39370.1
}
conversions_weight = {
    "ounces" : 1,
    "pounds" : 1/16, 
    "tons" : 1/32000,
    "kilograms" : 1/35.274,
    "grams": 28.3495
}
def convert (value, start_unit, end_unit, kind):
    if kind.lower()=="length":
        end = conversions_length[end_unit.lower()]
        start = conversions_length[start_unit.lower()]
    else: 
        end = conversions_weight[end_unit.lower()]
        start = conversions_weight[start_unit.lower()]
    r_value = int(value) * end/start
    return "The value of "+value+" "+start_unit+" in "+end_unit+" is "+str(r_value)+" "+end_unit

kind = ""
while kind.lower()!="weight" and kind.lower()!="length":
    kind = input("Would you like to convert between weight or length? ")
    if kind.lower()!="weight" and kind.lower()!="length":
        print("Invalid input, try again.")
start_unit = input("What is the starting unit? (put in plural form) ")
value = input("How many "+start_unit+" do you have? ")
end_unit = input("What unit do you want to convert to? (put in plural form) ")
print(convert(value, start_unit, end_unit, kind))