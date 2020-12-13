temp_list= []
total=float(0)

while len(temp_list)<24:
    newtemp=float(input("Enter the room temperature for this interval: "))
    temp_list.append(newtemp)
    total=sum(temp_list)
    print(len(temp_list))
    average=total/(len(temp_list))
    print("Current average temperature for the day is: {:.2f} degrees Celsius.".format(average))

average=total/24

print("The average temperature for the day is: {:.2f} degrees celsius.".format(average))
