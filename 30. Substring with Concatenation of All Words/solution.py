class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words_combinations = []
        def recurse(word: str, leftover_words: List[str]):
            if len(leftover_words) == 0:
                words_combinations.append(word)
                return
            for i,leftovers in enumerate(leftover_words):
                recurse(word+leftovers,leftover_words[0:i]+leftover_words[i+1:])
            
        for i,word in enumerate(words):
            recurse(word, words[0:i]+words[i+1:])
        maxlen = len(words_combinations[0])
        result = []
        for i in range(0,len(s)-maxlen+1,1):
            for word in words_combinations:
                print(i,s[i:i+maxlen],word)
                if s[i:i+maxlen] == word:
                    result.append(i)
                    break
        return result
