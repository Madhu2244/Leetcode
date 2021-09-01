class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest_length = 0
        stack = [-1]
        for i,char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    longest_length = max(longest_length, i - stack[-1])                    
        print(stack)
        return longest_length
        # for i in range (len(stack)):
        #     temp = 0
        #     if i == len(stack) - 1:
        #         temp = len(s) - stack[i] - 1
        #     else:
        #         temp = stack[i+1] - stack[i] - 1
        #     longest_length = max(temp,longest_length)
        # return longest_length
    
        #sliding window approach
        #set a max to 0
        #for i in range len(s):
        #look for the longest valid parenthesis from index i
        #if longest valid parenthesis is longer than max, change the max
        #to look for the longest valid praenthesis, if s[i] == ')', continue
        #otherwise add one to the counter of '('
        #substract the counter of '(' everytime a ')' is found
        #if there are 0 '(' when a ')' is found, change max accordingly
