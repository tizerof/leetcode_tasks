from time_of_function import benchmark


@benchmark
def maxSlidingWindow(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        count = 0
        while count < len(nums)-k+1:
            print()
            arr = nums[count:count+k*2-1]
            max_num = max(arr[:k])
            index_max_num = nums.index(max_num, count, count+k)
            index_big_max_num = nums.index(max(arr), count, count+k*2)
            print(index_max_num, index_big_max_num)
            if index_max_num == index_big_max_num:
                for i in range(count, index_max_num + 1):
                    result.append(max_num)
                    print("sda")
                count = index_max_num + 1
            else: 
                for i in range(count, index_big_max_num - k + 1):
                    result.append(max_num)
                count = index_max_num
        #for i in range(len(nums)-k+1):
        #    arr = nums[i:i+k]
        #    result.append(max(arr))
        return result

nums, k = [1,3,-1,-3,5,3,6,7], 3 

print(maxSlidingWindow(nums,k))
