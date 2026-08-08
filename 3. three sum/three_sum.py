from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) -2):
            if i>0 and nums[i-1] == nums[i]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum <0:
                    l = l+1
                elif three_sum >0:
                    r = r-1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l = l+1
                    while nums[l] == nums[l-1] and l<r:
                        l = l+1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
    print(solution.threeSum([0, 0, 0]))               # [[0, 0, 0]]
    print(solution.threeSum([3, 0, -2, -1, 1, 2]))   # [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]