import sys

# with open(r'score.txt', 'wt') as out_file:
#     sys.stdout = out_file
sys.stdout = open(r'score.txt', 'wt')



def signature(firstname_lastname):
    sum = 0
    for char in firstname_lastname:
        sum += ord(char)
    start_line = 7 + sum % 17
    return (start_line, start_line + 30, start_line + 60)


sign = signature("Parimal Ingle")
#print(sign)
with open('data.txt','r') as inp_file:
    inp = inp_file.read()
    #print(inp)

inp_data = inp.split("\n")

heading = True
#line_num = 0
#sign = [20, 50, 80]
is300_avg = 0
is310_avg = 0
is340_avg = 0
total_valid_300 = 0
total_valid_310 = 0
total_valid_340 = 0
res = {}
for l, i in enumerate(inp_data):
    #print(l, end= "")
    # if l in sign:
    #     content = "-" * 20 + "Parimal Ingle" + "-" * 20



    if len(i) > 0: #to check if blank line is there in file
        #line_num += 1
        if heading == True:
            contents = i.split(",")
            contents.append("Average")
            heading = False
            for j in contents:
                print(j, end= " ")
            print()
        else:
            name, is300, is310, is340 = i.split(",")
            scores = [is300, is310, is340]
            #print(name, is300, is310, is340)
            #scores = []
            curr_sum = 0
            curr_valid_scores = 0
            out_content = []

            for k,score in enumerate(scores):
                if score.isdigit() and 0 <= int(score) <= 100:
                    if k == 0:
                        is300_avg += int(score)
                        total_valid_300 += 1
                    elif k == 1:
                        is310_avg += int(score)
                        total_valid_310 += 1
                    else:
                        is340_avg += int(score)
                        total_valid_340 += 1
                    #print(k) 
                    #total_valid += 1
                    curr_sum += int(score)
                    curr_valid_scores += 1
                    out_content.append(score)
                else:
                    out_content.append("Error")
            if curr_valid_scores > 0:
                out_content.append(f'{(curr_sum / curr_valid_scores):.2f}')
            else:
                out_content.append("Error")
            # for j in out_content:
            #     print(j, end=" ")
            # print()
            res[name] = out_content

final_row = f'Class Average,{is300_avg/total_valid_300:.2f}({total_valid_300}),{is310_avg/total_valid_310:.2f}({total_valid_310}),{is340_avg/total_valid_340:.2f}({total_valid_340})'
#print(final_row)
myKeys = list(res.keys())
myKeys.sort()
sorted_dict = {i: res[i] for i in myKeys}
#.update({"Class Average": final_row})


content = "-" * 20 + "Parimal Ingle" + "-" * 20
for ind, i in enumerate(sorted_dict):
    #print(ind, end="")
    if ind in sign:
        print(content)
    else:
        print(f'{i},{",".join(sorted_dict[i])}')
print(final_row)
inp_file.close()
sys.stdout.close()