class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ansDict1 = {}
        ansDict2 = {}
        for letter in s:
            if letter not in ansDict1:
                ansDict1[letter] = 1
            ansDict1[letter] += 1
        for letter in t:
            if letter not in ansDict2:
                ansDict2[letter] = 1
            ansDict2[letter] += 1
        
        if ansDict1 == ansDict2:
            return True
        else:
            return False