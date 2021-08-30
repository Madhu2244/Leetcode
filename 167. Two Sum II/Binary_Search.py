def twoSum(numbers, target):
    for i in range(0, len(numbers)):
        curIndexNumber = numbers[i]
        arr = numbers[0:i] + numbers[i + 1:]
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] + curIndexNumber == target:
                return [i+1, mid+2]
            elif arr[mid] + curIndexNumber > target:
                r = mid - 1
            else:
                l = mid + 1

if __name__ == '__main__':
    print(twoSum([2,7,11,15],9))
