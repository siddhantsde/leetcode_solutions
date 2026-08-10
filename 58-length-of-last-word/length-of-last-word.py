class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split1 = s.split()
        return len(split1[-1])