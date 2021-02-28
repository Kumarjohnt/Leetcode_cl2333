class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = str(n)
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i-1]:
                idx, start = i, i
                while idx < len(nums) and nums[idx] > nums[i-1]: 
                    if nums[idx] < nums[start]:
                        start = idx
                    idx += 1
                prefix = nums[:i-1] + nums[start]
                res = int(prefix + "".join(sorted(list(nums[i-1:start] + nums[start+1:]))))
                return res if res < 2**31  else -1
        return -1