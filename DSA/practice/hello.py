# def bubble_sort(nums: list[int]) -> list[int]:
#     swap = True
#     end = len(nums) - 1
#     while swap:
#         swap = False
#         for i in range(end):
#             if nums[i] > nums[i+1]:
#                 nums[i], nums[i+1] = nums[i+1], nums[i]
#                 swap = True
#         end -= 1
#     return nums
                  
# # print(bubble_sort([5, 1, 4, 2, 8, 3]))






# def bubble_sort_by(nums: list[int]) -> list[int]:
#     swap = True
#     end = len(nums) - 1    # to access thw last item 
#     while swap: 
#         swap = False
#         for i in range(end):
#             if nums[i] > nums[i+1]:
#                 nums[i], nums[i+1] = nums[i+1], nums[i]
#                 swap = True
#         end -= 1 
#     return nums 

# print(bubble_sort_by([5, 1, 4, 2, 8, 3]))







# def bubble_sort_try(nums: list[int]) -> list[int]:
#     swap = True
#     end = len(nums) - 1
#     while swap: 
#         swap = False
#         for i in range(end):
#             if nums[i] > nums[i + 1]:
#                 nums[i], nums[i + 1] = nums[i + 1], nums[i]
#                 swap = True
#         end -= 1
#     return nums
        
# print(bubble_sort_try([1,4,5,6,7,8,9,0]))














    
