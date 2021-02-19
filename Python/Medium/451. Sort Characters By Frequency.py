from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        freq_list = list(zip(freq.keys(), freq.values()))
        return "".join([i[0]*i[1] for i in sorted(freq_list, key = lambda x: x[1], reverse = True)])