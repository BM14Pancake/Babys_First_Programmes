#Temperature Sensor nested loop

list1=[20, 21, 23, 25, 22]
list2=[27, 23, 25, 20, 30, 24]
list3=[22, 23, 24, 22]

total1=0
total2=0
total3=0

for i in range(3):
    if i==0:
        m=5
        n=list1
        x=total1
    elif i==1:
        m=6
        n=list2
        x=total2
    elif i==2:
        m=4
        n=list3
        x=total3
    for j in range(m):
        x=x+n[j]
        average=x/len(n)
    print("Average temperature in room", n, "is {:.1f}".format(average))
