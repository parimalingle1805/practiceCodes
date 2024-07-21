inp = input()
f = open(inp, 'r')
l = f.read()
l = l.split(",")
l[-1] = l[-1][:-1]
printed = []
for i in range(len(l)):
    if l[i] not in printed:
        print(f'{l[i]} - {l.count(l[i])}')
        printed.append(l[i])

##############################

import sys
sys.stdout=open(r'report.txt','wt')


midterm1 = 0
midterm2 = 0
finals = 0
cnt = 0
      
# TODO: Read a file name from the user and read the tsv file here. 
fileName = input()
f = open(fileName, 'r')
studentInfo = f.read()
l = studentInfo.split("\n")
l.pop()
for i in l:
    j = i.split('\t')    
    
    cnt += 1
    midterm1 += int(j[2])
    midterm2 += int(j[3])
    finals += int(j[4])
    avg = (int(j[2]) + int(j[3]) + int(j[4])) / 3
    if avg >= 90:
        grade = 'A'
    elif avg >= 80:
        grade = 'B'
    elif avg >= 70:
        grade = 'C'
    elif avg >= 60:
        grade ='D'
    else:
        grade = 'F'

    for k in j:
        print(k, end = "\t")
    print(grade)
    #print(i, end="-")
print()
print(f'Averages: midterm1 {(midterm1 / cnt):.2f}, midterm2 {(midterm2 / cnt):.2f}, final {(finals / cnt):.2f}')


#####################################

synonyms = {}   # Define dictionary

# Type your code here
inp = input()
letter = input()
f = open(f'{inp}.txt', 'r')
words = f.read()
words = words.split("\n")
words.pop()
for i in words:
    synonyms[i[0]] = i.split(" ")
    # print(i)
#print(synonyms)
try:
    res = synonyms[letter]
    for i in res:
        print(i)
except:
    print(f'No synonyms for {inp} begin with {letter}.')
    