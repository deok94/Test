block = []
Virus = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]

pre_count = 0

a = input()
ay = int(a.split()[0])
ax = int(a.split()[1])
array = []

def array_reset() :
    array2 = []
    for i in range(len(array)):
        ary2_list =[]
        for y in range(len(array[i])):
            ary2_list.append(int(array[i][y]))
        array2.append(ary2_list)
    return array2

for i in range(int(ay)):
    c = input()
    idx = []
    for y in c.split():
        idx.append(int(y))
    array.append(idx)

array2 = array

for i in range(len(array2)):
    for y in range(len(array2[i])):
        b_location = []
        v_location = []
        if array2[i][y] == 0:
            b_location.append(i)
            b_location.append(y)
            block.append(b_location)
        elif array2[i][y] ==2:
            v_location.append(i)
            v_location.append(y)
            Virus.append(v_location)

answer = 0
v_stack = []
print(Virus[0][0],Virus[0][1])
for a in range(0,len(block)):
    for b in range(a+1,len(block)):
        for c in range(b+1,len(block)):
            b_array2 = array_reset()
            b_array2[block[a][0]][block[a][1]] = 1
            b_array2[block[b][0]][block[b][1]] = 1
            b_array2[block[c][0]][block[c][1]] = 1

            while True :
                count = 0
                Virus[0][0]

                for y in range(len(Virus)):
                    for x in range(len(Virus[y])):
                        z_count = 0
                        for i in range(0,4):
                            bx = x+dx[i]
                            by = y+dy[i]
                            if bx >= 0 and by <= ay-1  and bx <=ax-1  and by >= 0:
                                ppp = b_array2[by][bx]
                                if ppp == 0:

                                    nv_location = []
                                    nv_location.append(by)
                                    nv_location.append(bx)
                                    b_array2[by][bx] = 2
                                    v_stack.append(nv_location)
                for i in b_array2:
                    for y in i:
                        if y == 0:
                            count +=1


                if count == pre_count:
                    if answer < count:
                        answer = count
                    break
                pre_count = count

print(answer)





