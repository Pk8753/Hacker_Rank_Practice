from collections import namedtuple
n=int(input())
marks=0
for j in range(n):
    f=list((input().upper()).split(' '))
    Student=namedtuple('Student',f)
    MARKS, ID, NAME, CLASS = input().split()
    student = Student(MARKS, CLASS, NAME, ID)
    marks += int(student.MARKS)
print('{:.2f}'.format(marks / n))

