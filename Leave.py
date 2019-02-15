import sys

n = sys.stdin.readline()

s = {} # schedule

for i in range(int(n)):
     p = sys.stdin.readline().split()

     if  i+1 + int(p[0]) <= int(n) :
        s[i+1] = p

print(s)
print()
work_check = []
count = 0
for i in s:
    T = 1  # Today
    work = []
    work.append(i)
    while work :
        count +=1
        w = work.pop()
        print(w)
        work_check.append(w)
        able = T + int(s[w][0])
        print('A-' + str(work))
        # print('able'+ str(able))
        for y in s:
            if able <= y:
                work.append(y)
        print('B-' + str(work))
        print()
        if count == 5:
            quit()

        # break
        #         if y >= able  :
        #             # print(int(s[i][0]))
        #             # print(str(i) +str('-')+ str(y))
        #             work.append(y)
        #     T += int(s[w][0])
        # print()





