def FindMaxCrossingSubarray(A, low, mid, high):
    left_sum = -1000000000
    _sum = 0
    for i in range(mid, low - 1, -1):
        _sum = _sum + A[i]
        if _sum > left_sum:
            left_sum = _sum
            max_left = i
    right_sum = -1000000000
    _sum = 0
    for j in range(mid + 1, high + 1, 1):
        _sum = _sum + A[j]
        if _sum > right_sum:
            right_sum = _sum
            max_right = j
    return max_left, max_right, left_sum + right_sum

def FindMaximumSubarray(A, low, high):
    if high == low:
        return low, high, A[low]
    else:
        mid = int((low + high) / 2)
        left_low, left_high, left_sum = FindMaximumSubarray(A, low, mid)
        right_low, right_high, right_sum = FindMaximumSubarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = FindMaxCrossingSubarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

if __name__ == '__main__':
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 14, -4, 7]
    print(FindMaximumSubarray(A, 0, 15))
