# Longest substring without repeating chars
def longest_substring(s):
    seen, start, max_length = {}, 0, 0
    for end, char in enumerate(s):
        if char in seen:
            start = max(start, seen[char] + 1)
        seen[char] = end
        max_length = max(max_length, end - start + 1)
    return max_length
print(longest_substring("abcabcbb"))
