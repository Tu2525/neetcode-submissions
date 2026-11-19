class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ansDicts = {}
        ansDictt = {}
        for letter in s:
            if letter in ansDicts:
                ansDicts[letter] += 1
            else:
                ansDicts[letter] = 1
        for letter in t:
            if letter in ansDictt:
                ansDictt[letter] += 1
            else:
                ansDictt[letter] = 1
        if ansDicts == ansDictt:
            return True
        else:
            return False
        