def balance_check(string):
    List=[]
    for i in range(len(string)):
        List.append(string[i])
    for x in List:
        if x=='(' or '[' or '{':
            open_normal=List.count('(')
            close_normal=List.count(')')
            open_square = List.count('[')
            close_square = List.count(']')
            open_curly = List.count('{')
            close_curly = List.count('}')
            if open_normal==close_normal and open_square==close_square and open_curly==close_curly:
                return True
            else:
                return False
string=input()
print(balance_check(string))