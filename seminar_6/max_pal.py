def longest_palindromic_substring(s: str) -> str:
    if not s:
        return ""

    n = len(s)
    dp = [[False] * n for _ in range(n)]

    max_len = 1
    start = 0

    for i in range(n):
        dp[i][i] = True

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            max_len = 2
            start = i

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_len:
                    max_len = length
                    start = i

    return s[start:start + max_len]

print(longest_palindromic_substring("babad"))
print(longest_palindromic_substring("cbbd"))
print(longest_palindromic_substring("a"))
print(longest_palindromic_substring(""))
