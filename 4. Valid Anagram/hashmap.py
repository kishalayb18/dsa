from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # created two hashmaps to store the frequency of each character in both strings
        # the get method is used to return the value for the given key if it exists in the dictionary, otherwise it returns the default value (0 in this case)
        cs, ct = {}, {}
        for i in range(len(s)):
            cs[s[i]] = 1 + cs.get(s[i], 0)
            ct[t[i]] = 1 + ct.get(t[i], 0)
        for ch in cs:
            if cs[ch] != ct.get(ch, 0):
                return False
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaram"))         # True
    print(solution.isAnagram("rat", "car"))                 # False
    print(solution.isAnagram("listen", "silent"))           # True
    print(solution.isAnagram("hi", "world"))                # False
    print(solution.isAnagram("newprogram", "dsaprogram"))   # False


# other solution using sorting
# if the lengths of the two strings are not equal, they cannot be anagrams, so we return False.
# else we sort both strings and compare them. 
# If they are equal, we return True; otherwise, we return False.
# this solution has a time complexity of O(nlogn) due to the sorting step, where n is the length of the strings. 
# The space complexity is O(1) if we ignore the space used for sorting, or O(n) if we consider the space used for the sorted strings.