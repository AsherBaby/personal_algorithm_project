class Candidate:
    def __init__(self):
        self.val = 0
        self.cnt = 0

def majorityNumber(nums):
    if len(nums) == 0:
        raise ValueError

    c1 = Candidate()
    c2 = Candidate()

    for i in range(len(nums)):
        if nums[i] == c1.val:
            c1.cnt += 1
        elif nums[i] == c2.val:
            c2.cnt += 1
        elif c1.cnt == 0:
            c1.val = nums[i]
            c1.cnt = 1
        elif c2.cnt == 0:
            c2.val = nums[i]
            c2.cnt = 1
        else:
            c1.cnt -= 1  # double veto
            c2.cnt -= 1

    return c1.val if nums.count(c1.val) > nums.count(c2.val) else c2.val

if majorityNumber([10,2,2,1,2]) != 2:
    raise AssertionError