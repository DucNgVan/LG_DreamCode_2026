a = [1,2,4,6,3]
def find_missing_num(a):
    n = len(a) + 1
    total_sum = n * (n + 1) // 2
    actual_sum = sum(a)
    missing_num = total_sum - actual_sum
    return missing_num

print (find_missing_num(a))