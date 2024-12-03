import sys

f = open(sys.argv[1], "r")

left_list = []
right_list = []
for x in f:
    x.strip()
    nums = x.split()
    right_list.append(int(nums[0]))
    left_list.append(int(nums[1]))
    
right_list.sort()
left_list.sort()   

similarity_score = 0
for i in range(len(right_list)):
    similarity_score += right_list[i] * left_list.count(right_list[i])
print(similarity_score)