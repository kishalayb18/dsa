"""
Two Sum — Hash Map (One Pass)

See solution.md for a detailed walkthrough.
"""

from typing import List


def solve(nums: List[int], target: int) -> List[int]:
    mapList: dict[int, int] = {}

    for i, num in enumerate(nums): # index, value
        diff = target - num

        if diff in mapList:
            # found the pair of indices that sum up to the target
            # return the indices of the difference mapList[diff] and the current number's indices i
            return [mapList[diff], i]
        else:
            # if the difference is not found, store the current number and its index in the mapList
            mapList[num] = i

    # if no pair of indices is found that sum up to the target, raise an error
    # though the problem statement guarantees a solution must be there
    raise ValueError("No two-sum solution found")

if __name__ == "__main__":
    print(solve([2, 7, 11, 15], 9))   # [0, 1]
    print(solve([3, 2, 4], 6))       # [1, 2]
    print(solve([3, 3], 6))          # [0, 1]