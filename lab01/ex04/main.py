from quanlysinhvien import QuanLySinhVien

qlsv = QuanLySinhVien()
l = 1
while (l == 1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("*************************MENU*************************")
    print("1. Them sinh vien.")
    print("2. Cap nhat thong tin sinh vien boi  ID")
    print("3. Xoa sinh vien boi ID")
    print("4. Tim kiem sinh vien boi ten")
    print("5. Sap xep sinh vien theo diem trung binh")
    print("6. Sap xep sinh vien theo ten chuyen nganh")
    print("7. Hien thi danh sach sinh vien")
    print("0. Thoat chuong trinh")
    print("*******************************************************")
    key = int(input("Nhap tuy chon cua ban:"))
    if ( key == 1):
        print ("\n 1. Them sinh vien")
        qlsv.nhapSinhVien()
        print("\n Them sinh vien thanh cong!")
    elif ( key == 2):
        if (qlsv.soLuonghSinhVien() > 0):
            print("\n 2. Cap nhat thong tin sinh vien.")
            print("\nNhap ID:")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh sach sinh vien rong!")
    elif ( key == 3):
        if(qlsv.soLuonghSinhVien() > 0):
            print("\n 3. Xoa sinh vien")
            print("\nNhap ID:")
            ID = int(input())
            if (qlsv.deleteByID(ID)):
                print("\nSinh vien co id =", ID,"Da bi xoa!")
            else:
                print("\nSinh vien co id =", ID, "Khong ton tai!")
        else: 
            print("\nDanh sach sinh vien rong!")
    elif ( key == 4):
        if(qlsv.soLuonghSinhVien() >0):
            print("\n 4. Tim kiem sinh vien theo ten.")
            print("\nNhap ten de tim kiem:")
            name = input()
            searchResult = qlsv.findByMajor(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sach sinh vien rong!")
    elif ( key == 5):
        if(qlsv.soLuonghSinhVien() >0):
            print("\n 5. Sap xep sinh vien theo diem trung binh (GPA).")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien rong!")
    elif ( key == 6):
        if(qlsv.soLuonghSinhVien() > 0):
            print("\n 6. Sap xep sinh vien theo ten chuyen nganh.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien rong!")
    elif ( key == 7):
        if(qlsv.soLuonghSinhVien() > 0):
            print("\n 7. Hien thi danh sach sinh vien.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien rong!")
    elif ( key == 0):
        print("\nBan da chon thoat chuong trinh!")
        break
    else: 
        print("\nKhong co chuc nang nay!")
        print("\nHay chon chuc nang co trong menu!!!")
            
   

