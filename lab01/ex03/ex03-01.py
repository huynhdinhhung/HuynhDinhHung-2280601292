def tinh_tong_so_chan (lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong
input_str = input("Nhap danh sach cac so, cach nhau boi dau phay: ")
numbers = list(map(int, input_str.split(',')))
tong_chan = tinh_tong_so_chan(numbers)
print (f"Tong cac so chan trong day la:", tong_chan)