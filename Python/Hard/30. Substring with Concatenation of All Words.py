from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n_words, word_len = len(words), len(words[0])    
        result = []
        
        for i in range(len(s) - n_words * word_len + 1):
            count = n_words
            
            counter = Counter(words)
            for j in range(n_words):
                word = s[i + j * word_len : i + (j+1) * word_len]
                if word not in counter:
                    break
                counter[word] -= 1
                if counter[word] >= 0:
                    count -= 1
           
            if count == 0:
                result.append(i)
                
      
        return result
            
            
        