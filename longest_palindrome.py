def longest_palindrome(s: str):
    N = len(s)
    max_len = 0
    longest_palindrome = None
#     steps = []
    # Time complexity O(n)
    for i, c in enumerate(s):
        # Time complexity worst case: O(N/2) avg case: O(N/k)
#         steps.append(min(i, N - i))
        for j in range(1, min(i, N - i) + 1):
            # O(1)
            before_centered = s[i - j: i]
            before_non_centered = s[i - j: i + 1]
            after_centered = s[i + 1: i + j + 1]
            after_non_centered = s[i + 1: i + j + 2]
            if before_centered == after_centered[::-1]:  # O(j)
                palindrome = before_centered + c + after_centered
                length = len(palindrome)
                if length > max_len:
                    max_len = length
                    longest_palindrome = palindrome
            if before_non_centered == after_non_centered[::-1]:  # O(j)
                palindrome = before_non_centered + after_non_centered
                length = len(palindrome)
                if length > max_len:
                    max_len = length
                    longest_palindrome = palindrome
#     print('Average inner loop:\t', sum(steps) / len(steps))
#     print('Worst case inner loop:\t', max(steps))
#     print('Total running time:\t', sum(steps) / len(steps) * N)
    return longest_palindrome, max_len

longest_palindrome('malayalam abcdefedcba')
