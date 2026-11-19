class Solution:
    def isPalindrome(self, s: str) -> bool:
        list1 = []
        for letter in s:
            if letter.isalnum():
                list1.append(letter.lower())
            else:
                continue
        if list1 == list1[::-1]:
            return True
        else:
            return False
