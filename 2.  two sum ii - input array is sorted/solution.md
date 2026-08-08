# Two Sum II — Detailed Walkthroughs

The `.py` files in this folder are intentionally minimal. This document is
the home for the **strategy, complexity, walkthroughs, and flow diagrams**
for every approach.

---

## 1. Two Pointers (Sorted) — `twopointers.py`  ← RECOMMENDED

### Strategy
The input is already sorted in non-decreasing order. Place one pointer at
the start (`i = 0`) and one at the end (`j = n - 1`). At each step, compare
`numbers[i] + numbers[j]` to the target:

- Too small → move `i` right (need a larger value).
- Too large → move `j` left (need a smaller value).
- Equal → found the answer. Return `[i+1, j+1]` (1-indexed).

### Complexity
- **Time:** `O(n)` — each pointer moves at most `n` steps, total `≤ 2n`.
- **Space:** `O(1)` — only the two indices. **Meets the problem's
  "constant extra space" requirement.**

### Why It Works
After sorting, the sum is monovariant: moving `i` up always increases the
sum, moving `j` down always decreases it. So each comparison eliminates
one element, and we converge in at most `n` steps.

### Pseudocode
```
i, j = 0, n - 1
while i < j:
    s = numbers[i] + numbers[j]
    if s == target: return [i+1, j+1]
    elif s < target: i += 1
    else:            j -= 1
```

### Flow Diagram
```
  ┌───────────────┐
  │     START     │
  └───────┬───────┘
          ▼
  ┌───────────────────────┐
  │ i = 0, j = n - 1      │
  └───────────┬───────────┘
              ▼
  ┌───────────────────────┐
  │ i < j ?               │
  └───┬───────────────┬───┘
    NO               YES
     │                │
     ▼                ▼
  (per problem     ┌───────────────────────┐
   guarantee,     │ s = numbers[i]+numbers[j]
   unreachable)   └───────────┬───────────┘
                              ▼
                ┌───────────────────────────┐
                │  s == target ?            │
                └────┬───────┬───────┬──────┘
              YES    │   <   │   >   │
                     ▼       ▼       ▼
              ┌──────────┐ ┌────┐ ┌────┐
              │ return   │ │ i++│ │ j--│
              │ [i+1,j+1]│ └─┬──┘ └─┬──┘
              └────┬─────┘   │      │
                   │         └──────┴──► (loop back to `i < j` ?)
                   ▼
              ┌───────────┐
              │   DONE    │
              └───────────┘
```

### Walkthrough — `numbers = [2, 7, 11, 15]`, target `9`
```
  i  j  numbers[i]  numbers[j]  sum   action
  -- --  ----------  ----------  ----  -------------------------------
   0  3       2          15       17   sum > 9  →  j -= 1
   0  2       2          11       13   sum > 9  →  j -= 1
   0  1       2           7        9   sum == 9 →  return [1, 2]  ✅
```

### Walkthrough — `numbers = [2, 3, 4]`, target `6`
```
  i  j  numbers[i]  numbers[j]  sum   action
  -- --  ----------  ----------  ----  -------------------------------
   0  2       2           4        6   sum == 6 →  return [1, 3]  ✅
```

### Walkthrough — `numbers = [-1, 0]`, target `-1`
```
  i  j  numbers[i]  numbers[j]  sum   action
  -- --  ----------  ----------  ----  -------------------------------
   0  1      -1           0       -1  sum == -1 → return [1, 2]  ✅
```

### Edge Cases
- **Negative numbers** — work fine; comparison logic is the same.
- **Two-element array** — single iteration, returns immediately.
- **Duplicates** — the algorithm doesn't depend on uniqueness.

---

## 2. Hash Map (One Pass) — `hash_map.py`

### Strategy
Walk the array once. For each number, check if its complement
(`target - num`) was already seen. If yes, return both 1-indexed positions;
otherwise, store the current number with its 1-indexed position.

This is the same approach used for Two Sum (#1) — it works here too,
just with a 1-index offset and without needing to sort.

### Complexity
- **Time:** `O(n)` — single pass, each hash lookup is `O(1)` average.
- **Space:** `O(n)` — hash map holds up to `n` entries.

**⚠️ Does NOT meet the problem's "constant extra space" requirement.**
Use this only if you've decided to trade the space requirement for
implementation simplicity or if the input isn't guaranteed sorted.

### Why It Works
Same as Two Sum (#1): at step `i`, the map contains every earlier number.
If any of them is the complement, the pair is the answer.

### Pseudocode
```
for i, num in enumerate(numbers):
    diff = target - num
    if diff in seen:
        return [seen[diff], i + 1]
    seen[num] = i + 1
```

### Walkthrough — `numbers = [2, 7, 11, 15]`, target `9`
```
  i  num  diff  seen (before)        action
  -- ----  ----  -----------------   ------------------------------
  0    2     7   {}                  not in seen → seen[2] = 1
  1    7     2   {2: 1}              in seen!  → return [1, 2]  ✅
```

### When To Use
- Input might not be sorted.
- The "constant space" constraint is not enforced (interview follow-up,
  homework, or relaxed version of the problem).
- You want a one-liner-style solution.

---

## Quick Comparison

| Approach | Time | Space | Meets "constant space" constraint? |
|----------|------|-------|------------------------------------|
| Two Pointers (sorted) | **O(n)** | **O(1)** | ✅ Yes — the intended answer. |
| Hash Map              | O(n)     | O(n)     | ❌ No — uses extra memory.          |