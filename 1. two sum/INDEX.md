# Two Sum — Implementation Index

Each file exposes a standalone `solve(nums, target)` function.

| File | Approach | Time | Space | Best When |
|------|----------|------|-------|-----------|
| `two_sum_hash_map.py`         | One-pass hash map   | **O(n)**   | O(n) | You want the optimal time complexity. |
| `two_sum_sort_two_pointers.py`| Sort + two pointers | O(n log n) | O(n) | You want a non-hash-map route (accepts a sort cost). |
| `two_sum_brute_force.py`      | Nested loops        | O(n²)      | O(1) | `n` is tiny or you want the simplest baseline. |

## Common Usage

```python
from two_sum_hash_map import solve

print(solve([2, 7, 11, 15], 9))   # [0, 1]
```

## Recommendation
**Use the hash map approach** (`two_sum_hash_map.py`) — it is optimal in time
and the most common interview answer.

See `solution.md` for a detailed writeup and flow diagrams.