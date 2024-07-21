def anagram_check(string1,string2):
    for i in string1:
        for j in string2:
            if string1.count(i)==string2.count(j):
                return True






string1=input()
string2=input()

string1 = string1.replace(' ','')
string2 = string2.replace(' ','')
bool=anagram_check(string1,string2)
if bool==True:
    print("yes")
else:
    print("no")