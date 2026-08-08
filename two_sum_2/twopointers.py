"""
Two Sum II — Two Pointers (Sorted Input)

Complexity:
    Time  : O(n)
    Space : O(1)   ← meets the problem's constant-space requirement

See solution.md for a detailed walkthrough.
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # left starts at the smallest value, right starts at the largest
        i, j = 0, len(numbers) - 1

        while i < j:
            # sum of the current pair
            current_sum = numbers[i] + numbers[j]

            if current_sum == target:
                # found the pair of 1-indexed positions
                # return indices incremented by one as required by the problem
                return [i + 1, j + 1]
            elif current_sum < target:
                # sum too small, bump the left pointer to a larger value
                i += 1
            else:
                # sum too large, bring the right pointer to a smaller value
                j -= 1

        # per the problem's guarantee, this line is unreachable
        raise ValueError("No two-sum solution found")


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))   # [1, 2]
    print(solution.twoSum([2, 3, 4], 6))       # [1, 3]
    print(solution.twoSum([-1, 0], -1))        # [1, 2]
