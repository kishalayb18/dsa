# Two Sum II — Input Array Is Sorted

## Problem Source
LeetCode #167 — [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

how to solve [video two sum 2](https://www.youtube.com/watch?v=cQ1Oz4ckceM&list=PLPe9IkX86X3y5m_MvtNu2ughxsvkqUNKr&index=11)

## Problem Statement
Given a **1-indexed** array of integers `numbers` that is **already sorted in
non-decreasing order**, find two numbers such that they add up to a specific
target number. Let these two numbers be `numbers[index1]` and `numbers[index2]`
where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, **each incremented by one**, as an
integer array `[index1, index2]` of length 2.

- The tests are generated such that there is exactly one solution.
- You may not use the same element twice.
- Your solution must use only **constant extra space**.

### Examples

```
Input:  numbers = [2, 7, 11, 15], target = 9   →  Output: [1, 2]
        (2 + 7 = 9, so we return [1, 2].)

Input:  numbers = [2, 3, 4],      target = 6   →  Output: [1, 3]
        (2 + 4 = 6, so we return [1, 3].)

Input:  numbers = [-1, 0],        target = -1  →  Output: [1, 2]
        (-1 + 0 = -1, so we return [1, 2].)
```

### Constraints

```
2     <= numbers.length <= 3 * 10^4
-1000 <= numbers[i]    <= 1000
numbers is sorted in non-decreasing order.
```

## Key Difference vs. Two Sum (#1)
- The input is **pre-sorted** → enables the O(1) extra-space two-pointer approach.
- Output is **1-indexed** (not 0-indexed).
- The O(n log n) sort is unnecessary because the input is already sorted.

## Where to Find What

| You want... | Go to |
|-------------|-------|
| Problem source / statement | this file (`two_sum_2.md`) |
| Strategy, complexity, walkthroughs, flow diagrams | `solution.md` |
| Recommended solution (two pointers, O(1) space) | `twopointers.py` |
| Alternative solution (hash map, O(n) space) | `hash_map.py` |

## Solutions in This Folder

| Approach | File | Time | Space | Notes |
|----------|------|------|-------|-------|
| Two Pointers (sorted) | `twopointers.py` | **O(n)** | **O(1)** | Optimal — exploits pre-sorted input. |
| Hash Map | `hash_map.py` | O(n) | O(n) | Works on unsorted input too; fails the "constant space" constraint. |

## Recommendation
Use the **two pointers** approach — it's optimal in both time and space,
and LeetCode marks this as the intended solution for the "constant extra
space" requirement.
## Solution Video
Place to provide a solution video (walkthrough / explanation). Add a YouTube
link or embed an iframe below when available.

- **Video (link):** [Add video title and URL here]

- **Embed (example):**

  <iframe width="560" height="315" src="https://www.youtube.com/embed/VIDEO_ID" title="Solution Video" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

