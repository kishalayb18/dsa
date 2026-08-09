# Valid Anagram — Solution Approaches

## Problem
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

## Approach 1: Frequency count with Hashmaps (best)
- Count letters in `s` and subtract counts using `t`.
- If every count returns to zero, `t` is an anagram.

Time: O(n)
Space: O(1) if only lowercase English letters are used (fixed-size array of 26).

## Approach 2: Sort and compare
- Sort both strings and compare the sorted results.
- This works because two anagrams will produce the same sorted string.

Time: O(n log n)
Space: O(n)

## Approach 3: One-pass hash map
- Use a hash map to count letters in `s`.
- Decrement counts while scanning `t`.
- If any count becomes negative or leftover counts remain, return `false`.

Time: O(n)
Space: O(k), where `k` is the number of distinct characters.

## Notes
- Prefer the frequency-count approach for lowercase English-letter anagrams.
- Use the sorting approach when simplicity is more important than constant time.
