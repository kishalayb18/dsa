# Two Sum — Detailed Walkthroughs

Each `.py` file in this folder is intentionally minimal. This document is the
home for the **strategy, complexity, edge cases, and step-by-step walkthroughs**
for every approach.

---

## 1. Hash Map (One Pass) — `two_sum_hash_map.py`

### Strategy
Maintain a hash map of `value -> index` for every number we've seen so far.
For each new number `num`, check whether its complement (`target - num`) is
already in the map. If yes, we have the answer; otherwise, store `num`.

### Complexity
- **Time:** `O(n)` — single pass, each hash lookup is `O(1)` average.
- **Space:** `O(n)` — hash map holds up to `n` entries.

### Why It Works
At step `i`, the map contains exactly `nums[0..i-1]`. So if any earlier
number is the complement of `nums[i]`, the pair `(earlier_index, i)` is the
answer. We look up *before* inserting, which prevents using the same element
twice.

### Pseudocode
```
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
```

### Flow Diagram
```
                  ┌───────────────┐
                  │     START     │
                  └───────┬───────┘
                          ▼
              ┌───────────────────────┐
              │  seen = {} (empty)    │
              └───────────┬───────────┘
                          ▼
        ┌──────────────────────────────────────┐
        │  for i, num in enumerate(nums):     │
        └─────────────────┬────────────────────┘
                          ▼
              ┌───────────────────────┐
              │  complement = target  │
              │             - num     │
              └───────────┬───────────┘
                          ▼
                  ┌───────────────┐
                  │ complement in │
                  │     seen ?    │
                  └───┬───────┬───┘
                 Yes  │       │  No
                      ▼       ▼
       ┌────────────────────┐  ┌──────────────────────┐
       │  return            │  │  seen[num] = i       │
       │  [seen[complement],│  │  (store for future   │
       │         i]         │  │   lookups)           │
       └─────────┬──────────┘  └──────────┬───────────┘
                 │                        ▼
                 │              ┌───────────────────┐
                 │              │  next iteration   │
                 │              └───────────────────┘
                 ▼
           ┌───────────┐
           │   DONE    │
           └───────────┘
```

### Walkthrough — `nums = [2, 7, 11, 15]`, target `9`
```
  i  num  complement  seen (before)        action
  -- ----  ----------  -----------------   ------------------------------
  0   2        7      {}                  not in seen → seen[2] = 0
  1   7        2      {2: 0}              in seen!  → return [0, 1]
```

### Walkthrough — duplicates `nums = [3, 3]`, target `6`
```
  i  num  complement  seen (before)        action
  -- ----  ----------  -----------------   ------------------------------
  0   3        3      {}                  not in seen → seen[3] = 0
  1   3        3      {3: 0}              in seen!  → return [0, 1]
```

### Edge Cases
- **Duplicates** — indices are stored alongside values, so `[3, 3]` works.
- **Negatives** — hash map keys can be negative with no extra care.
- **Two-element array** — returns on the very first complement check.

---

## 2. Brute Force (Nested Loops) — `two_sum_brute_force.py`

### Strategy
Try every possible pair `(i, j)` with `i < j`. Return the first pair whose
sum equals the target.

### Complexity
- **Time:** `O(n²)` — roughly `n*(n-1)/2` pair checks.
- **Space:** `O(1)` — no extra data structures.

### Why It Works
The problem guarantees exactly one valid pair, so exhaustive search is
guaranteed to find it.

### Pseudocode
```
for i in range(n):
    for j in range(i + 1, n):
        if nums[i] + nums[j] == target:
            return [i, j]
```

### Flow Diagram
```
  ┌───────────────┐
  │     START     │
  └───────┬───────┘
          ▼
  ┌───────────────────────┐
  │ i = 0                │
  │ for i < n:           │
  │   j = i + 1          │
  │   for j < n:         │
  └───────────┬───────────┘
              ▼
  ┌───────────────────────┐
  │ nums[i] + nums[j]    │
  │   == target ?        │
  └───┬───────────────┬───┘
    YES              NO
     │                │
     ▼                ▼
  ┌──────────┐   ┌──────────┐
  │ return   │   │  j += 1  │
  │ [i, j]   │   │ (next j) │
  └────┬─────┘   └────┬─────┘
       │              │
       ▼              └──► (loop back to inner loop)
  ┌───────────┐
  │   DONE    │
  └───────────┘
```

### When To Use
Use only as a baseline or when `n` is tiny. Too slow on the constraint
`n ≤ 10⁴`.

---

## 3. Sort + Two Pointers — `two_sum_sort_two_pointers.py`

### Strategy
1. Pair each value with its original index: `(index, value)`.
2. Sort those pairs by value.
3. Walk inward from both ends with two pointers. Adjust the pointer based on
   whether the current sum is too small, too large, or exactly the target.
4. When found, return the **original** indices (sorted ascending).

### Complexity
- **Time:** `O(n log n)` — dominated by the sort.
- **Space:** `O(n)` — the `(index, value)` pairs.

### Why It Works
After sorting by value, the sum is monovariant: moving `left` up always
increases the sum, moving `right` down always decreases it. Each comparison
rules out half the remaining candidates.

### Pseudocode
```
indexed = sorted(enumerate(nums), key=lambda p: p[1])
left, right = 0, len(indexed) - 1
while left < right:
    s = indexed[left][1] + indexed[right][1]
    if s == target: return sorted pair of original indices
    elif s < target: left += 1
    else:            right -= 1
```

### Walkthrough — `nums = [2, 7, 11, 15]`, target `9`
```
indexed = [(0,2), (1,7), (2,11), (3,15)]   # already sorted

left=0, right=3  →  2 + 15 = 17  > 9   → right -= 1
left=0, right=2  →  2 + 11 = 13  > 9   → right -= 1
left=0, right=1  →  2 +  7 =  9  = 9   → return [0, 1]
```

### Walkthrough — `nums = [3, 2, 4]`, target `6`
```
indexed = [(1,2), (0,3), (2,4)]            # sorted by value

left=0, right=2  →  2 + 4 = 6 = 6 → return [min(1,2), max(1,2)] = [1, 2]
```

### Trade-offs
- Slower than the hash map on average (`n log n` vs `n`).
- Useful when you want to avoid a hash map (e.g., to keep memory
  allocations simple) or when the array is already mostly sorted.

---

## Quick Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Hash Map (one pass) | **O(n)** | O(n) | Optimal time; the standard answer. |
| Sort + Two Pointers | O(n log n) | O(n) | No hash map; needs index annotation. |
| Brute Force | O(n²) | O(1) | Simplest; only for tiny `n`. |