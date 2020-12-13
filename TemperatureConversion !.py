#Temperature Conversion 13/12/20

def fahr_to_cel(fahr):
    cel = (5.0/9.0)*(fahr-32)
    return cel

def cel_to_fahr(cels):
    heit = ((9.0/5.0)*cels)+32
    return heit

print("Temperature Conversion \n[1] Fahrenheit to Celsius conversion \n[2] Celsius to Fahrenheit conversion\n[3] Exit")
conv=int(input("Please enter your option: "))
if conv==1:
    fahr=float(input("Input Fahrenheit temperature: "))
    cels=fahr_to_cel(fahr)
    print("This temperature in Celsius is {:.2f}.".format(cels))
elif conv==2:
    cels=float(input("Input Celsius temperature: "))
    heit=cel_to_fahr(cels)
    print("This temperature in Fahrenheit is {:.2f}.".format(heit))
elif conv==3:
    print("Goodbye!")
