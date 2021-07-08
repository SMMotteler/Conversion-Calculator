#dictionary of conversions between lengths
conversions_length = {
    "inches" : 1,
    "feet" : 1/12,
    "yards" : 1/36,
    "miles" : 1/63360,
    "meters" : 1/39.3701,
    "kilometers": 1/39370.1
}
#dictionary of conversions between weights
conversions_weight = {
    "ounces" : 1,
    "pounds" : 1/16, 
    "tons" : 1/32000,
    "kilograms" : 1/35.274,
    "grams": 28.3495
}
#conversion function
def convert (value, start_unit, end_unit, kind):
    #gets the conversion values for the starting and ending units
    if kind.lower()=="length":
        end = conversions_length[end_unit.lower()]
        start = conversions_length[start_unit.lower()]
    else: 
        end = conversions_weight[end_unit.lower()]
        start = conversions_weight[start_unit.lower()]
    #calculates the converted value
    r_value = int(value) * end/start
    #returns a string listing the starting value and the ending value, as well as their units
    return "The value of "+value+" "+start_unit+" in "+end_unit+" is "+str(r_value)+" "+end_unit

kind = ""
#determines if the conversions are using weight or length units
while kind.lower()!="weight" and kind.lower()!="length":
    kind = input("Would you like to convert between weight or length? ")
    if kind.lower()!="weight" and kind.lower()!="length":
        print("Invalid input, try again.")
#asks for starting unit
start_unit = input("What is the starting unit? (put in plural form) ")
#asks for number of starting unit
value = input("How many "+start_unit+" do you have? ")
#asks for ending unit
end_unit = input("What unit do you want to convert to? (put in plural form) ")
#prints the converted value using the conversion function
print(convert(value, start_unit, end_unit, kind))