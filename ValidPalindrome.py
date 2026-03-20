def isPalindrome1(self, s: str) -> bool:
        if len(s) == 0:
            return True
        left = 0
        right = len(s) - 1
        while left <= right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

def isPalindrome2(self, s: str) -> bool:
    back = len(s) - 1
    front = 0
    while front <= back:
        if not s[front].isalnum():
            front += 1
            continue
        if not s[back].isalnum():
            back -= 1
            continue
        if s[front].lower() != s[back].lower():
            return False
        front += 1
        back -=1
    return True