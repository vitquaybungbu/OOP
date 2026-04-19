import pickle
import os
from abc import ABC, abstractmethod


class GiaKhongHopLe(Exception):
    def __init__(self, message="Lỗi: Giá sản phẩm không hợp lệ (phải >= 0)!"):
        super().__init__(message)

class MaHangTrungLap(Exception):
    def __init__(self, ma_hang):
        super().__init__(f"Lỗi: Mã hàng '{ma_hang}' đã tồn tại trong danh sách!")


class HangHoa(ABC):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self._ma_hang = ma_hang
        self._ten_hang = ten_hang
        self.nha_sx = nha_sx
        self.gia = gia  

    @property
    def ma_hang(self):
        return self._ma_hang  

    @property
    def ten_hang(self):
        return self._ten_hang 

    @property
    def gia(self):
        return self._gia

    @gia.setter
    def gia(self, gia_tri):
        if gia_tri < 0:
            raise GiaKhongHopLe()
        self._gia = gia_tri

    @abstractmethod
    def loai_hang(self):
        pass

    @abstractmethod
    def inTTin(self):
        pass

    def __str__(self):
        gia_format = f"{self.gia:,.0f}"
        return f"| {self.ma_hang:<8} | {self.ten_hang:<22} | {self.nha_sx:<15} | {gia_format:>15} | {self.loai_hang():<12}"

    def __eq__(self, other):
        if isinstance(other, HangHoa):
            return self.ma_hang == other.ma_hang
        return False

    def __lt__(self, other):
        return self.gia < other.gia

    def __hash__(self):
        return hash(self.ma_hang)


class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, tg_baohanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.tg_baohanh = tg_baohanh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat

    def loai_hang(self):
        return "Điện Máy"

    def inTTin(self):
        chi_tiet = f"BH: {self.tg_baohanh} tháng, {self.dien_ap}V, {self.cong_suat}W"
        return f"{super().__str__()} | {chi_tiet:<38} |"


class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyenlieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.loai_nguyenlieu = loai_nguyenlieu

    def loai_hang(self):
        return "Sành Sứ"

    def inTTin(self):
        chi_tiet = f"Chất liệu: {self.loai_nguyenlieu}"
        return f"{super().__str__()} | {chi_tiet:<38} |"


class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_hethan):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.ngay_sx = ngay_sx
        self.ngay_hethan = ngay_hethan

    def loai_hang(self):
        return "Thực Phẩm"

    def inTTin(self):
        chi_tiet = f"HSD: {self.ngay_sx} -> {self.ngay_hethan}"
        return f"{super().__str__()} | {chi_tiet:<38} |"



class QuanLyHangHoa:
    def __init__(self):
        self.danh_sach = set()

    def them_hang(self, sp: HangHoa):
        if sp in self.danh_sach:
            raise MaHangTrungLap(sp.ma_hang)
        self.danh_sach.add(sp)

    def in_bang(self):
        header = f"| {'Mã Hàng':<8} | {'Tên Sản Phẩm':<22} | {'Nhà SX':<15} | {'Giá Bán (VNĐ)':>15} | {'Loại':<12} | {'Thông Tin Đặc Thù':<38} |"
        print("-" * len(header))
        print(header)
        print("-" * len(header))

     
        for sp in sorted(self.danh_sach):
            print(sp.inTTin())
            
        print("-" * len(header))

    def luu_file(self, ten_file="data_hanghoa.pkl"):
        with open(ten_file, "wb") as f:
            pickle.dump(self.danh_sach, f)
        print(f"[+] Đã lưu {len(self.danh_sach)} mặt hàng vào '{ten_file}'")

    def doc_file(self, ten_file="data_hanghoa.pkl"):
        if os.path.exists(ten_file):
            with open(ten_file, "rb") as f:
                self.danh_sach = pickle.load(f)
            print(f"[+] Đã khôi phục {len(self.danh_sach)} mặt hàng từ '{ten_file}'")
        else:
            print(f"[!] File '{ten_file}' không tồn tại.")


# Main
if __name__ == "__main__":
    ql = QuanLyHangHoa()

    print("\n[1] TEST THÊM HÀNG VÀ BẮT NGOẠI LỆ (EXCEPTIONS)")

    ql.them_hang(HangDienMay("DM001", "Máy lạnh Daikin", "Daikin", 12500000, 24, 220, 1500))
    ql.them_hang(HangDienMay("DM002", "Tủ lạnh Aqua", "Aqua", 6500000, 12, 220, 180))
    ql.them_hang(HangSanhSu("SS001", "Bộ ấm trà Bát Tràng", "Bát Tràng", 850000, "Men rạn"))
    ql.them_hang(HangThucPham("TP001", "Sữa tươi tiệt trùng", "Vinamilk", 35000, "10/04/2026", "10/10/2026"))

    # Bắt lỗi giá âm
    try:
        sp_loi = HangDienMay("DM003", "Quạt hỏng", "Senko", -100, 12, 220, 45)
    except GiaKhongHopLe as e:
        print(e)

    # Bắt lỗi trùng mã
    try:
        ql.them_hang(HangSanhSu("SS001", "Bình hoa", "Bát Tràng", 150000, "Gốm"))
    except MaHangTrungLap as e:
        print(e)

    print("\n[2] BẢNG HÀNG HÓA (Đã sắp xếp giá tăng dần nhờ __lt__)")
    ql.in_bang()

    print("\n[3] TEST LƯU/ĐỌC FILE (CONTEXT MANAGER)")
    ql.luu_file()
    ql.danh_sach.clear() # Xóa sạch RAM
    ql.doc_file()        # Khôi phục từ ổ cứng