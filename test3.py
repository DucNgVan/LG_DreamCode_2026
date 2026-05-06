def find_2_num(n, m):
    # Tạo danh sách chuẩn chứa các số từ 1 đến m
    a = []
    for i in range(1, m + 1):
        a.append(i)
        
    missing_nums = []

    for num in a:
        if num not in n:
            missing_nums.append(num)
            

    print("Các số bị thiếu là:", missing_nums)

if __name__ == '__main__':

    m = int(input("Nhập m: "))
    

    n = list(map(int, input("Nhập mảng n: ").split()))
    

    find_2_num(n, m)