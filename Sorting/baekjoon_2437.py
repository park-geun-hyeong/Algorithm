import sys
read = sys.stdin.readline


def exception(n,nums):
    if nums[0]>1:
        print(1)
        sys.exit()

    if n == 1:
        if nums[0]>1:
            print(1)
        else:
            print(nums[0] + 1)
        sys.exit()

    return

if __name__ == "__main__":
    n = int(read().rstrip())
    nums = list(map(int, read().split()))
    nums.sort()

    exception(n,nums)

    min_temp = 0
    max_temp = 0
    min_range = 0
    max_range = 0

    for i in range(n):
        new = nums[i]
        #print(min_range, max_range)
        if i == 0:
            max_range = new
            continue

        min_temp = min_range + new
        max_temp = max_range + new

        if min_temp <= max_range+1:
            max_range = max_temp
        else:
            print(max_range+1)
            sys.exit()

    print(max_range + 1)

