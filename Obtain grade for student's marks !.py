#Obtain grade for student's marks

def obtain_grade(mark):
    if 84.5<=mark<=100:
        grade="A+"
    elif 79.5<=mark<84.5:
        grade="A"
    elif 74.5<=mark<79.5:
        grade="B+"
    elif 69.5<=mark<74.5:
        grade="B"
    elif 64.5<=mark<69.5:
        grade="C+"
    elif 59.5<=mark<64.5:
        grade="C"
    elif 54.5<=mark<59.5:
        grade="D+"
    elif 49.5<=mark<54.5:
        grade="D"
    elif mark<49.5:
        grade="F"
    return grade

#function for displaying students marks in tabular format

def tabled_marks(student_marks):
    print("Student Name\tMarks\tGrade")
    for i in range(len(student_marks)):
        if len(student_marks[i][0])<7:
            print(student_marks[i][0],"\t\t",student_marks[i][1],"\t",obtain_grade(student_marks[i][1]))
        else:
            print(student_marks[i][0],"\t",student_marks[i][1],"\t",obtain_grade(student_marks[i][1]))
