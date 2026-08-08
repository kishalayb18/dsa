# Two Sum

## Problem Source
LeetCode #1 — [Two Sum](https://leetcode.com/problems/two-sum/)

how to solve [video two sum](https://www.youtube.com/watch?v=KLlXCFG5TnA&list=PLPe9IkX86X3y5m_MvtNu2ughxsvkqUNKr&index=3&pp=iAQB)

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers such that they add up to `target`.

- Each input has exactly one solution.
- The same element cannot be used twice.
- The answer may be returned in any order.

### Examples

```
Input:  nums = [2, 7, 11, 15], target = 9   →  Output: [0, 1]
         (Because nums[0] + nums[1] == 9, we return [0, 1].)

Input:  nums = [3, 2, 4],      target = 6   →  Output: [1, 2]

Input:  nums = [3, 3],         target = 6   →  Output: [0, 1]
```

### Constraints

```
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target  <= 10^9
```

## Where to Find What

| You want... | Go to |
|-------------|-------|
| Problem source / statement | this file (`twosum.md`) |
| Strategy, complexity, walkthroughs, flow diagrams | `solution.md` |
| Index of all approaches in this folder | `INDEX.md` |
| Recommended solution (hash map, one pass) | `two_sum_hash_map.py` |

## Solutions in This Folder

| Approach | File | Time | Space |
|----------|------|------|-------|
| Hash Map (one pass) | `two_sum_hash_map.py` | **O(n)** | O(n) |
| Sort + Two Pointers | `two_sum_sort_two_pointers.py` | O(n log n) | O(n) |
| Brute Force (nested loops) | `two_sum_brute_force.py` | O(n²) | O(1) |

## Recommendation
Use the **hash map (one pass)** approach — optimal in time and the most
common interview answer. See `solution.md` for the full writeup.