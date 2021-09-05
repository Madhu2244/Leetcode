from collections import deque
import sys

def main():
    q = int(sys.stdin.readline()) #amount of queries we need to run
    queue = deque() #create the queue
    running_sum = 0
    for i in range (q): #loop through all queries
        temp = list(map(int, sys.stdin.readline().split()))
        if temp[0] == 5: #"5"  : print the sum of the elements currently in the list
            sys.stdout.write(str(running_sum) + '\n')
        elif temp[0] == 1: #"1 n": add n to the start of the list
            running_sum += temp[1]
            queue.appendleft(temp[1])
        elif temp[0] == 2: # "2 n": add n to the end of the list
            running_sum += temp[1]
            queue.append(temp[1])
        elif temp[0] == 3: #"3 n": remove the first occurrence of n from the list(n is always in the list)
            running_sum -= temp[1]
            queue.remove(temp[1])
        else: # "4 n": remove the last occurrence of n from the list(n is always in the list)
            #queue.rotate(-length +1)
            queue.reverse()
            running_sum -= temp[1]
            queue.remove(temp[1])
            queue.reverse()
            #queue.rotate(-length + 1)
    sys.stdout.write(" ".join(map(str,queue)) + "\n") 
    
if __name__ == '__main__':
    main()
