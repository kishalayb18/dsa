"""
Two Sum — Sort + Two Pointers

See solution.md for a detailed walkthrough.
"""

from typing import List


def solve(nums: List[int], target: int) -> List[int]:
    # annotate each value with its original index, then sort by value
    # after sorting: indexed[i] = (original_index, value)
    indexed: List[tuple[int, int]] = sorted(
        enumerate(nums), key=lambda pair: pair[1]
    )

    # left starts at the smallest value, right starts at the largest
    left, right = 0, len(indexed) - 1

    while left < right:
        # sum of the current values (not the original indices)
        current_sum = indexed[left][1] + indexed[right][1]

        if current_sum == target:
            # found the pair of indices that sum up to the target
            # return the original indices in ascending order
            i, j = indexed[left][0], indexed[right][0]
            return [min(i, j), max(i, j)]
        elif current_sum < target:
            # sum too small, bump the left pointer to a larger value
            left += 1
        else:
            # sum too large, bring the right pointer to a smaller value
            right -= 1

    # if no pair of indices is found that sum up to the target, raise an error
    # though the problem statement guarantees a solution must be there
    raise ValueError("No two-sum solution found")

if __name__ == "__main__":
    print(solve([2, 7, 11, 15], 9))   # [0, 1]
    print(solve([3, 2, 4], 6))       # [1, 2]
    print(solve([3, 3], 6))          # [0, 1]