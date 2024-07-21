from math import *
def row_col_calc(s):
    no_of_char=len(s)
    rows=floor(sqrt(no_of_char))
    columns=ceil(sqrt(no_of_char))
    return rows,columns

def result(s):
    rows,columns=row_col_calc(s)
    x=0
    i=0
    j=0
    z=0
    #while i<=range(len(s)):
    while i<columns:
        while j<len(s):
            if x%columns==z:
                print(s[x],end="")
            x+=1
            j+=1
        i+=1
        z+=1
        j=0
        x=0
        print(" ",end="")


s=input()
s=s.replace(' ','')
result(s)