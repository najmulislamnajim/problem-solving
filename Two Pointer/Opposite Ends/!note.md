# 🟢 Opposite Ends (Start From Left + Right)

---

## 🔹 Easy Problems
- Two Sum II (Sorted Array) → [LeetCode 167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
- Palindrome Check
- Reverse String / Reverse Array

---

## 🔸 Medium Problems
- 3Sum → [LeetCode 15](https://leetcode.com/problems/3sum/)
- Container With Most Water → [LeetCode 11](https://leetcode.com/problems/container-with-most-water/)

---

## 🔺 Hard Problems
- Trapping Rain Water → [LeetCode 42](https://leetcode.com/problems/trapping-rain-water/)

---

## ✅ Template (Two Pointer)

```python
left, right = 0, len(arr) - 1

while left < right:
    if condition: 
        # Your Logic
    elif something:
        left += 1
    else:
        right -= 1
