


import sys

# returns unsafe index or -1 if all are safe
def is_safe(report):
    previous_diff = 0
    for i in range(len(report) - 1):
        diff = int(report[i]) - int(report[i + 1])
        # print(i)
        # print(diff)
        #print("previous: " + str(previous_diff) + " current: " + str(diff))
        if previous_diff < 0 and diff > 0:
            return i + 1 
        elif previous_diff > 0 and diff < 0:
            return i
        elif diff == 0:
            return i
        elif abs(diff) > 3:
            return i + 1
        previous_diff = diff
    return -1

f = open(sys.argv[1], "r")

safe = 0

reports = f.readlines()

for report in reports:
    report.strip()
    original_report = report
    report = report.split()
    unsafe = is_safe(report)
    if unsafe == -1:
        safe += 1
    else:
        # remove bad index & rerun
        popped = report.pop(unsafe)
        # print(popped)
        # print(unsafe)
        unsafe = is_safe(report)
        if unsafe == -1:
            safe += 1
        else:
            print(original_report)

print(safe)
# similarity_score = 0
# for i in range(len(right_list)):
#     similarity_score += right_list[i] * left_list.count(right_list[i])
# print(similarity_score)