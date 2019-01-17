food_times = [1, 2, 3, 4, 5, 6]#[3,1,2]#[1,2,3,2,1]#
k = 10
food_count = len(food_times)
# print(food_count)
print(0, food_times)
count = 0
for i in range(0,k+1):

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
print(type(idx+1))
# print((idx+1)%food_times)
    # print(str(i)+ '~'+ str(i+1),idx+1,food_times )
# print(idx,i,food_count)
#
# print((idx+2)%food_count)

# print(food_times)



