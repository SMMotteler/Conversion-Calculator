# 3 parameter (value,original unit, desired unit)
# dictionary of the units and the conversion values ={}
# value*desired unit/original unit
# return value
conversions = {
    "inches" : 1,
    "feet" : 1/12,
    "yards" : 1/36,
    "miles" : 1/63360,
    "meters" : 1/39.3701,
    "kilometers": 1/39370.1
}
def convert (value, start_unit, end_unit):
    end = conversions[end_unit.lower()]
    start = conversions[start_unit.lower()]
    r_value = int(value) * end/start
    return "The value of "+value+" "+start_unit+" in "+end_unit+" is "+str(r_value)+" "+end_unit
start_unit = input("What is the starting unit? (put in plural form) ")
value = input("How many "+start_unit+" do you have? ")
end_unit = input("What unit do you want to convert to? (put in plural form) ")
print(convert(value, start_unit, end_unit))