# Add Two Numbers — Detailed Walkthroughs

---

## 1. Digit-by-digit Linked List Addition — `solution.md`  ← RECOMMENDED

### Strategy
Traverse the two linked lists simultaneously, adding corresponding digits and a carry value at each step.

- Use `carry = 0` initially.
- While either list has nodes:
  - sum = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
  - carry = sum // 10
  - node.val = sum % 10
  - append node to result list
  - move l1 and l2 forward if available
- If `carry` remains after traversal, append one more node.

### Complexity
- **Time:** `O(max(n, m))`
- **Space:** `O(max(n, m))` for the result list.

### Why It Works
Because the digits are stored in reverse order, the least significant digits are aligned at the start of the lists. This allows a single pass with carry propagation exactly like manual addition.

### Pseudocode
```
dummy = ListNode(0)
current = dummy
carry = 0
while l1 or l2 or carry:
    x = l1.val if l1 else 0
    y = l2.val if l2 else 0
    total = x + y + carry
    carry = total // 10
    current.next = ListNode(total % 10)
    current = current.next
    if l1: l1 = l1.next
    if l2: l2 = l2.next
if carry:
    current.next = ListNode(carry)
return dummy.next
```

### Notes
- This is the standard LeetCode solution for `Add Two Numbers`.
- It handles different lengths and leftover carry naturally.

---

## 2. Convert to Integers and Back — `solution.md`

### Strategy
Convert each linked list into its integer value, add the integers, then convert the sum back to a linked list.

### Complexity
- **Time:** `O(n + m)` for conversion and reconstruction
- **Space:** `O(n + m)` for the integer/string representation

### When To Use
- Only as a conceptual alternative or for languages with safe arbitrary-precision integers.
- Avoid in production if list lengths can exceed the language’s integer limits.

### Why It Works
The linked lists represent reversed digits, so converting them to integers and back preserves the same numerical addition logic.

---

## 3. Stack-based Addition — `solution.md`

### Strategy
Push digits from each list onto a stack, then pop and add them with carry. This is more useful when the digits are given in forward order, but it can still be applied after reversing the lists.

### Complexity
- **Time:** `O(n + m)`
- **Space:** `O(n + m)`

### Why It Works
Stacks allow you to process digits from least significant to most significant when the natural input order is reversed or when the input is hard to mutate.

---

## Comparison

| Approach | Time | Space | Best Use |
|----------|------|-------|----------|
| Digit-by-digit linked list | **O(max(n, m))** | **O(max(n, m))** | Recommended for this problem |
| Convert to integers | O(n + m) | O(n + m) | Conceptual / small inputs only |
| Stack-based addition | O(n + m) | O(n + m) | When the input order is not convenient |

## Recommendation
Use the **digit-by-digit linked list addition** approach as the primary solution.
