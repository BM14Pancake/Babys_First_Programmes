#Primary school calculator math game 04/12/20
import random as r

while True:
    
    Qno=int(input("How many questions would you like to do?"))

    #list of correct or wrong answers
    mark_list= []

    while len(mark_list)<Qno:
        num1=r.randint(0,100)
        num2=r.randint(0,100)
        actans=num1+num2
        print(num1, "+", num2, "= ?")
        givans=int(input())

        if givans==actans:
            print("That's right!")
            mark_list.append("C")
        else:
            print("Incorrect! Next question: ")
            mark_list.append("W")

    print("You got", mark_list.count("C"), "out of", Qno, "correct!")

    while True:
        answer = str(input("Play again? (y/n): "))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break
