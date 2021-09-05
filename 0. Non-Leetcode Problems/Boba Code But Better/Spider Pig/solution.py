def main():
    params = list(map(int,input().split()))
    maxJump = params[1]
    arr = list(map(int,input().split()))
    cur_index = 0 #which building we are currently on
    total_climbs = 0 #output
    while cur_index < len(arr) - 1: #if we are out of bounds we are done
        #print('new loop')
        localMax = 0
        best_index = 0 #index that is less than arr[cur_index] and the largest from (cur_index to cur_index+jump]
        for i in range (1,maxJump + 1): #check from jump range 1 to max range
            if cur_index + i > len(arr) - 1: #if we are out of bounds then we are done
                break
            if arr[cur_index + i] >= arr[cur_index]: 
                break
            if arr[cur_index + i] >= localMax: #if the next building has a height greater than the local max but is also less than cur_index, then we adjust the localMax.
                localMax = arr[cur_index + i]
                best_index = cur_index + i
            #print(arr[cur_index + i], localMax, cur_index+i)
        if localMax == 0:
            cur_index += 1
            total_climbs += 1
        else:
            cur_index = best_index
    print(total_climbs)
        
    
if __name__ == '__main__':
    main()
