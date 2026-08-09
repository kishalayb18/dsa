# 2. Add Two Numbers

## Problem Source
[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

### Examples

```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

```
Input: l1 = [0], l2 = [0]
Output: [0]
```

```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

### Constraints

```
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
```


## Solutions in This Folder

| Approach | File | Time | Space |
|----------|------|------|-------|
| Digit-by-digit linked-list addition | `solution.md` | O(max(n, m)) | O(max(n, m)) |
| Convert to integers and back | `solution.md` | O(n + m) | O(n + m) |
| Stack-based addition | `solution.md` | O(n + m) | O(n + m) |

## Recommendation
Use the **digit-by-digit linked-list addition** approach — it is the simplest and safest for this problem's constraints.
