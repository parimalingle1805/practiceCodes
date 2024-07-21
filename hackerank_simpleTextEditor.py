def Append(s,w):
    s+=w
    return s

def Delete(s,k):
    k=int(k)
    t=s[0:len(s)-k]
    return t


q=int(input())
s=""
edit_stack=[]
for operation in range(q):
    command=list(map(str,input().split()))
    if command[0]=='1':#append characters
        beforeEdit=s
        edit_stack.append(beforeEdit)
        s=Append(s,command[1])
    elif command[0]=='2':#delete k characters
        beforeEdit=s
        edit_stack.append(beforeEdit)
        s=Delete(s,command[1])
    elif command[0]=='3': #print k th character
        print(s[int(command[1])-1])
    else:
        s=edit_stack.pop() #undo
    #print(s)
    #print(beforeEdit)
    #print(edit_stack)