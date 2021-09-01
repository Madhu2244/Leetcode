class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest_length = 0
        for i in range (len(s)-1):
            if s[i] == ')':
                continue
            localMax = 0
            cur_length = 1
            open_counter = 1
            for j in range (i+1,len(s)):
                if s[j] == '(':
                    cur_length += 1
                    open_counter += 1
                elif open_counter > 0: #s[j] == ')'
                    cur_length += 1
                    open_counter -= 1
                    if open_counter == 0:
                        localMax = max(localMax,cur_length)
                else:
                    break
            longest_length = max(longest_length,localMax)
        return longest_length
    
        #sliding window approach
        #set a max to 0
        #for i in range len(s):
        #look for the longest valid parenthesis from index i
        #if longest valid parenthesis is longer than max, change the max
        #to look for the longest valid praenthesis, if s[i] == ')', continue
        #otherwise add one to the counter of '('
        #substract the counter of '(' everytime a ')' is found
        #if there are 0 '(' when a ')' is found, change max accordingly
