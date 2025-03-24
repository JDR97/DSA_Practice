def get_longest_ss_length(arr, n, idx, prev_idx, dp):
    if n == idx:
        return 0
    
    if dp[idx][prev_idx+1] != -1:
        return dp[idx][prev_idx+1]
    
    not_take = 0 + get_longest_ss_length(arr, n, idx+1, prev_idx, dp)

    take = 0

    if prev_idx == -1 or arr[idx] > arr[prev_idx]:
        take = 1 + get_longest_ss_length(arr, n, idx+1, idx, dp)

    dp[idx][prev_idx+1] = max(not_take, take)

    return dp[idx][prev_idx+1]


def longest_increasing_subsequence_length(arr):
    n = len(arr)
    dp = [[-1 for _ in range(n+1)] for _ in range(n)]
    return get_longest_ss_length(arr, n, 0, -1, dp)


if __name__ == "__main__":
    arr = [10, 9, 2, 5, 3, 7, 101, 18]

    result = longest_increasing_subsequence_length(arr)
    print("The length of the longest increasing subsequence is", result)