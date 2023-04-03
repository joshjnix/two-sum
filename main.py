class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_list = []
        for i in range(len(nums)):
            if num_list == []:
                for j in range (len(nums)):
                    if (nums[i] + nums[j] == target) and (i != j):
                        num_list.append(i)
                        num_list.append(j)
                        break
                    else: continue
            else: break        
        return num_list
