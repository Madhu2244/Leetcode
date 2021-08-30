class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        arr = list(map(int,list(digits)))
        d = {
            2: ['a','b','c'],
            3: ['d','e','f'],
            4: ['g','h','i'],
            5: ['j','k','l'],
            6: ['m','n','o'],
            7: ['p','q','r','s'],
            8: ['t','u','v'],
            9: ['w','x','y','z']
        }
        letters = []
        for num in arr:
            letters.append(d[num])
        output = []
        index = [0 for i in range(len(digits))]
        print(letters,index)
        while True:
            result = ''
            
            for i,lists in enumerate(letters):
                result += lists[index[i]]
            output.append(result)
            index[-1] += 1
            
            while True:
                flag = False
                for i in range(1,len(index)+1):
                    print(i,index[-i], len(letters[-i]))
                    if index[-i] >= len(letters[-i]):
                        index[-i] = 0
                        if i == len(index):
                            return output
                        else:
                            index[-i-1] += 1
                    else:
                        flag = True
                        break
                if flag:
                    break
            
