import os
from abc import ABC, abstractmethod

class TuoiKhongHopLe(Exception):
    def __init__(self, tuoi):
        super().__init__(f"Lỗi: Tuổi {tuoi} không hợp lệ (Phải từ 18 - 65).")

class BacKhongHopLe(Exception):
    def __init__(self, bac):
        super().__init__(f"Lỗi: Bậc {bac} không hợp lệ (Phải từ 1 - 10).")


class CanBo(ABC):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi  
        self.gioi_tinh = gioi_tinh 
        self.dia_chi = dia_chi

    @property
    def tuoi(self):
        return self._tuoi

    @tuoi.setter
    def tuoi(self, gia_tri):
        if not (18 <= gia_tri <= 65):
            raise TuoiKhongHopLe(gia_tri)
        self._tuoi = gia_tri

    @property
    def gioi_tinh(self):
        return self._gioi_tinh

    @gioi_tinh.setter
    def gioi_tinh(self, gia_tri):
        gt_chuan = gia_tri.strip().lower()
        if gt_chuan in ["nam", "nữ", "nu", "khác", "khac"]:
            self._gioi_tinh = gia_tri.capitalize()
        else:
            self._gioi_tinh = "Khác"

    @abstractmethod
    def mo_ta(self):
        pass

    @abstractmethod
    def lay_thong_tin_rieng(self):
        pass

    def __str__(self):
        return f"{self.ho_ten:<20} | {self.tuoi:<4} | {self.gioi_tinh:<9} | {self.dia_chi:<15}"

    def __eq__(self, other):
        if isinstance(other, CanBo):
            return self.ho_ten == other.ho_ten and self.tuoi == other.tuoi
        return False

    def __lt__(self, other):
        return self.ho_ten < other.ho_ten


class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac  

    @property
    def bac(self):
        return self._bac

    @bac.setter
    def bac(self, gia_tri):
        if not (1 <= int(gia_tri) <= 10):
            raise BacKhongHopLe(gia_tri)
        self._bac = int(gia_tri)

    def mo_ta(self):
        return "Công Nhân"

    def lay_thong_tin_rieng(self):
        return f"Bậc: {self.bac}/10"

    def __str__(self):
        return f"{super().__str__()} | {self.mo_ta():<12} | {self.lay_thong_tin_rieng():<30}"

    def __repr__(self):
        return f"CongNhan('{self.ho_ten}', {self.tuoi}, '{self.gioi_tinh}', '{self.dia_chi}', {self.bac})"

class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh_dao_tao = nganh_dao_tao

    def mo_ta(self):
        return "Kỹ Sư"

    def lay_thong_tin_rieng(self):
        return f"Ngành: {self.nganh_dao_tao}"

    def __str__(self):
        return f"{super().__str__()} | {self.mo_ta():<12} | {self.lay_thong_tin_rieng():<30}"

    def __repr__(self):
        return f"KySu('{self.ho_ten}', {self.tuoi}, '{self.gioi_tinh}', '{self.dia_chi}', '{self.nganh_dao_tao}')"

class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

    def mo_ta(self):
        return "Nhân Viên"

    def lay_thong_tin_rieng(self):
        return f"Công việc: {self.cong_viec}"

    def __str__(self):
        return f"{super().__str__()} | {self.mo_ta():<12} | {self.lay_thong_tin_rieng():<30}"

    def __repr__(self):
        return f"NhanVien('{self.ho_ten}', {self.tuoi}, '{self.gioi_tinh}', '{self.dia_chi}', '{self.cong_viec}')"


class QLCB:
    def __init__(self):
        self.danh_sach_cb = []

    def them_can_bo(self, can_bo):
        self.danh_sach_cb.append(can_bo)
        print(f"[*] Đã thêm thành công: {can_bo.ho_ten} ({can_bo.mo_ta()})")

    def tim_kiem_theo_ten(self, tu_khoa):
        return [cb for cb in self.danh_sach_cb if tu_khoa.lower() in str(cb).lower()]

    def hien_thi_danh_sach(self, danh_sach=None):
        ds_can_in = self.danh_sach_cb if danh_sach is None else danh_sach
        
        if len(ds_can_in) == 0:
            print("\n[!] Danh sách hiện tại đang trống. Không có dữ liệu để hiển thị.")
            return

        header = f"| {'STT':<3} | {'Họ Tên':<20} | {'Tuổi':<4} | {'Giới Tính':<9} | {'Địa Chỉ':<15} | {'Vai Trò':<12} | {'Thông Tin Đặc Thù':<30} |"
        print("\n" + "-" * len(header))
        print(header)
        print("-" * len(header))

        for stt, cb in enumerate(sorted(ds_can_in), start=1):
            print(f"| {stt:<3} | {cb} |") 
            
        print("-" * len(header))

    def luu_file(self, ten_file="canbo.txt"):
        with open(ten_file, "w", encoding="utf-8") as f:
            for cb in self.danh_sach_cb:
                f.write(repr(cb) + "\n")
        print(f"[+] Đã lưu {len(self.danh_sach_cb)} cán bộ vào '{ten_file}'")

    def doc_file(self, ten_file="canbo.txt"):
        if not os.path.exists(ten_file):
            print(f"[!] File '{ten_file}' không tồn tại.")
            return
        self.danh_sach_cb.clear()
        with open(ten_file, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip(): 
                    cb = eval(line.strip()) 
                    self.danh_sach_cb.append(cb)
        print(f"[+] Đã đọc {len(self.danh_sach_cb)} cán bộ từ '{ten_file}'")


def xoa_man_hinh():
    os.system('cls' if os.name == 'nt' else 'clear')


# 6. CHƯƠNG TRÌNH CHÍNH (MENU)

if __name__ == "__main__":
    quan_ly = QLCB()
    quan_ly.them_can_bo(KySu("Nguyễn Văn A", 28, "Nam", "Hà Nội", "CNTT"))
    quan_ly.them_can_bo(CongNhan("Trần Thị B", 35, "Nữ", "Hải Phòng", 5))
    quan_ly.them_can_bo(NhanVien("Lê Văn C", 24, "Nam", "Đà Nẵng", "Lễ tân"))
    

    input("\n[?] Khởi tạo xong dữ liệu mẫu. Nhấn Enter để vào chương trình...")

    while True:
        xoa_man_hinh() 
        
        print("="*45)
        print(" CHƯƠNG TRÌNH QUẢN LÝ CÁN BỘ ".center(45, "="))
        print("1. Thêm mới cán bộ")
        print("2. Tìm kiếm theo họ tên")
        print("3. Hiển thị thông tin (Tự động xếp ABC)")
        print("4. Lưu danh sách vào File (canbo.txt)")
        print("5. Khôi phục danh sách từ File")
        print("6. Thoát khỏi chương trình")
        print("="*45)
        
        chon = input("Nhập lựa chọn của bạn (1-6): ")

        if chon == '1':
            print("\n--- THÊM CÁN BỘ MỚI ---")
            loai = input("Chọn loại (1-Công Nhân, 2-Kỹ Sư, 3-Nhân Viên): ")
            if loai not in ['1', '2', '3']:
                print("[!] Lựa chọn không hợp lệ!")
                input("\n[?] Nhấn Enter để quay lại Menu...")
                continue

            ten = input("Nhập họ tên: ")
            
            try:
                tuoi = int(input("Nhập tuổi (18-65): "))
                gt = input("Nhập giới tính (Nam/Nữ/Khác): ")
                dc = input("Nhập địa chỉ: ")

                if loai == '1':
                    bac = int(input("Nhập bậc công nhân (1-10): "))
                    cb_moi = CongNhan(ten, tuoi, gt, dc, bac) 
                elif loai == '2':
                    nganh = input("Nhập ngành đào tạo: ")
                    cb_moi = KySu(ten, tuoi, gt, dc, nganh)
                elif loai == '3':
                    cv = input("Nhập công việc: ")
                    cb_moi = NhanVien(ten, tuoi, gt, dc, cv)
                
                quan_ly.them_can_bo(cb_moi)
                
            except TuoiKhongHopLe as e:
                print(e)
            except BacKhongHopLe as e:
                print(e)
            except ValueError:
                print("[!] Lỗi: Vui lòng nhập số nguyên hợp lệ cho Tuổi hoặc Bậc.")

            input("\n[?] Nhấn Enter để tiếp tục...") 

        elif chon == '2':
            tu_khoa = input("\nNhập tên cán bộ cần tìm: ")
            kq = quan_ly.tim_kiem_theo_ten(tu_khoa)
            print(f"\n--- KẾT QUẢ TÌM KIẾM CHO '{tu_khoa}' ---")
            quan_ly.hien_thi_danh_sach(kq)
            input("\n[?] Nhấn Enter để tiếp tục...") 

        elif chon == '3':
            print("\n--- DANH SÁCH TOÀN BỘ CÁN BỘ ---")
            quan_ly.hien_thi_danh_sach()
            input("\n[?] Bảng đã hiển thị xong. Nhấn Enter để quay lại Menu...") 

        elif chon == '4':
            quan_ly.luu_file()
            input("\n[?] Nhấn Enter để tiếp tục...")

        elif chon == '5':
            quan_ly.doc_file()
            input("\n[?] Nhấn Enter để tiếp tục...")

        elif chon == '6':
            print("Đã thoát chương trình. Tạm biệt!")
            break
        else:
            print("[!] Lựa chọn không hợp lệ, vui lòng thử lại.")
            input("\n[?] Nhấn Enter để tiếp tục...")