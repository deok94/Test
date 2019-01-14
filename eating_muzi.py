food_times = [1,2,3,2,1]#[3,1,2]#[1,2,3,2,1]#
k = 7
food_count = len(food_times)
# print(food_count)
print(0, food_times)
count = 0
for i in range(0,k):

    while True:
        idx = (i + count) % food_count
        if food_times[idx] == 0 :
            count +=1
            # idx = (i +1) % food_count
        # elif food_times[idx] !=0 :
        else :
            food_times[idx] -= 1
            break
    print(i,idx+1,food_times)
print(((idx+1)%food_count)+1)
    # print(str(i)+ '~'+ str(i+1),idx+1,food_times )
# print(idx,i,food_count)
#
# print((idx+2)%food_count)

# print(food_times)



