"""
Two Sum — Brute Force (Nested Loops)

See solution.md for a detailed walkthrough.
"""

from typing import List


def solve(nums: List[int], target: int) -> List[int]:
    n = len(nums)

    for i in range(n): # outer index
        for j in range(i + 1, n): # inner index, must be after i
            if nums[i] + nums[j] == target:
                # found the pair of indices that sum up to the target
                # return the indices of nums[i] and nums[j]
                return [i, j]

    # if no pair of indices is found that sum up to the target, raise an error
    # though the problem statement guarantees a solution must be there
    raise ValueError("No two-sum solution found")

if __name__ == "__main__":
    print(solve([2, 7, 11, 15], 9))   # [0, 1]
    print(solve([3, 2, 4], 6))       # [1, 2]
    print(solve([3, 3], 6))          # [0, 1]