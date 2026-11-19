class Solution:
    def isPalindrome(self, s: str) -> bool:
        list1 = []
        list2 = []
        for letter in s:
            if letter.isalpha() or letter.isnumeric():
                list1.append(letter.lower())
            else:
                continue
        list2 = list1.copy()
        list2.reverse()
        print(f"List1: {list1}")
        print(f"List2: {list2}")
        if list1 == list2:
            return True
        else:
            return False
