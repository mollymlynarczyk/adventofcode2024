


import sys

def is_safe(report):
    previous_diff = 0
    for i in range(len(report) - 1):
        diff = int(report[i]) - int(report[i + 1])
        # print(diff)
        # print("previous: " + str(previous_diff) + " current: " + str(diff))
        if previous_diff < 0 and diff > 0:
            return False
        elif previous_diff > 0 and diff < 0:
            return False
        elif diff == 0:
            return False
        elif abs(diff) > 3:
            return False
        previous_diff = diff
    return True

f = open(sys.argv[1], "r")

safe = 0

reports = f.readlines()

for report in reports:
    # print(report)
    report.strip()
    report = report.split()
    if is_safe(report):
        safe += 1
print(safe)
# similarity_score = 0
# for i in range(len(right_list)):
#     similarity_score += right_list[i] * left_list.count(right_list[i])
# print(similarity_score)