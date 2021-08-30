class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i,n in enumerate(numbers):
            if n in d:
                d[n][0] += 1
                d[n][1].append(i)
            else:
                d[n] = [1,[i]]
        print (d)
        
        for i,n in enumerate(numbers):
            leftover = target - n
            if leftover in d:
                if leftover == n:
                    if d[n][0] > 1:
                        return [i+1,d[n][1][1]+1]
                else:
                    return [i+1,d[leftover][1][0]+1]
