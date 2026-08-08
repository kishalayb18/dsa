"""
Two Sum II — Hash Map (One Pass)

Complexity:
    Time  : O(n)
    Space : O(n)   ← does NOT meet the problem's constant-space requirement

See solution.md for a detailed walkthrough.
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # map each value we've already seen to its 1-indexed position
        seen: dict[int, int] = {}

        for i, num in enumerate(numbers):
            # the number we'd need to pair with `num` to reach the target
            diff = target - num

            if diff in seen:
                # found the pair of 1-indexed positions
                # return them in ascending order as required by the problem
                return [seen[diff], i + 1]

            # not found yet, store `num` with its 1-indexed position for future lookups
            seen[num] = i + 1

        # per the problem's guarantee, this line is unreachable
        raise ValueError("No two-sum solution found")


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))   # [1, 2]
    print(solution.twoSum([2, 3, 4], 6))       # [1, 3]
    print(solution.twoSum([-1, 0], -1))        # [1, 2]
