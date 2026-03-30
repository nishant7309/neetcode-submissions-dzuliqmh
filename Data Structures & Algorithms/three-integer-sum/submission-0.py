class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 1. MUST SORT
        triplets = []
        
        for i in range(len(nums) - 2):
            # 2. Skip duplicate for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # 3. Two pointers: start j after i
            j, k = i + 1, len(nums) - 1
            
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                
                if current_sum == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # 4. Skip duplicates for j and k
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif current_sum < 0:
                    j += 1
                else:
                    k -= 1
        return triplets
