""" Partition Equal Subset Sum """
def canPartition(nums):
        n = len(nums)
        k = sum(nums)
        if k % 2 != 0:
            return False
        p = [[0 for i in range(n+1)] for j in range(k//2+1)]
        for i in range(k//2+1):
            p[0][i] = True
        for i in range(n+1):
            p[i][0] = True

        for i in range(1, k//2):
            for j in range(1, n):
                p[i]
                if i - nums[j-1] >= 0:
                    p[i][j] = (p[i][j-1] or p[i-nums[j-1],j-1])
                else:
                    p[i][j] = p[i][j-1]
        return p[k//2,n]

nums = [1,5,11,5]
print(canPartition(nums))
