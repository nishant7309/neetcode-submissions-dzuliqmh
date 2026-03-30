class Solution:
    def isPalindrome(self, s: str) -> bool:
        fs = "".join(char.lower() for char in s if char.isalnum())

        for i in range(len(fs)//2):
            if fs[i] != fs[-(i+1)]:
                return False
        return True