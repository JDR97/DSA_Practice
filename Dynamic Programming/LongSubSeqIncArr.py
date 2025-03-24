####Have some issue with this code, need to checkw####
def get_longest_ss(arr, n, idx, prev_idx, dp, parent):
    if idx == n:
        return 0

    if dp[idx][prev_idx + 1] != -1:
        return dp[idx][prev_idx + 1]

    # Case 1: Do not take the current element
    not_take = get_longest_ss(arr, n, idx + 1, prev_idx, dp, parent)

    # Case 2: Take the current element (if valid)
    take = 0
    if prev_idx == -1 or arr[idx] > arr[prev_idx]:
        take = 1 + get_longest_ss(arr, n, idx + 1, idx, dp, parent)

    # Store the max length
    if take > not_take:
        dp[idx][prev_idx + 1] = take
        parent[idx] = prev_idx  # Store the previous index
    else:
        dp[idx][prev_idx + 1] = not_take

    return dp[idx][prev_idx + 1]


def reconstruct_lis(arr, parent, best_start):
    lis = []
    while best_start != -1:
        lis.append(arr[best_start])
        best_start = parent[best_start]
    print(lis)
    return lis[::-1]  # Reverse to get the correct order


def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [[-1 for _ in range(n + 1)] for _ in range(n)]
    parent = [-1] * n  # Track previous indices

    get_longest_ss(arr, n, 0, -1, dp, parent)

    # Find the index where LIS starts
    max_length = max(dp[i][-1] for i in range(n))
    best_start = -1
    for i in range(n):
        if dp[i][-1] == max_length:
            best_start = i
            break

    return reconstruct_lis(arr, parent, best_start)


# Example Usage:
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(longest_increasing_subsequence(arr))