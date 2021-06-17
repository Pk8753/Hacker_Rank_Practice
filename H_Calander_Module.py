# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import calendar
def findDay(m,d,y):
    day = {0:'MONDAY', 1:'TUESDAY', 2:'WEDNESDAY', 3:'THURSDAY', 4:'FRIDAY', 5:'SATURDAY', 6:'SUNDAY'}
    return day[calendar.weekday(y, m, d)]




if __name__ == '__main__':
    m,d,y = map(int,input().split(" "))
    print(findDay(m,d,y))

