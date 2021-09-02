class Solution:
    def countAndSay(self, n: int) -> str:
        def recurse(cur_str: string, num: string) -> str:
            next_str = ''
            i = 0
            while i < len(cur_str):
                num_count = 1
                next_num = cur_str[i]
                #print(i, len(num) - 1)
                while i < len(cur_str) - 1 and cur_str[i + 1] == cur_str[i]:
                    num_count += 1
                    i += 1
                i += 1
                next_str += str(num_count) + str(next_num)
            #print(next_str)
            num = int(num) + 1
            if int(num) >= n:
                #rint('here')
                return next_str
            else:
                return recurse(next_str,num)
        if n == 1:
            return '1'
        return recurse('1','1')
        #print('here')
