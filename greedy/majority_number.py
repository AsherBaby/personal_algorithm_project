def majorityNumber(self, nums):
        maj = nums[0]
        cnt = 1
        for val in nums[1:]:
            if val == maj:
                cnt += 1
            else:
                if cnt == 1:
                    maj = val
                else:
                    cnt -= 1
        cnt = nums.count(maj)
        return maj if cnt > len(nums) // 2 else None
