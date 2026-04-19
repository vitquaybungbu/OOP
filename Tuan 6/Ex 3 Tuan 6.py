import math

class MauSoBangKhong(Exception):
    """Ngoại lệ riêng được ném ra khi mẫu số bằng 0."""
    pass

class PhanSo:
    def __init__(self, tu, mau):
        self.tu_so = tu
        self.mau_so = mau

    @property
    def tu_so(self):
        return self._tu_so

    @tu_so.setter
    def tu_so(self, value):
        self._tu_so = value

    @property
    def mau_so(self):
        return self._mau_so

    @mau_so.setter
    def mau_so(self, value):
        if value == 0:
            raise MauSoBangKhong("Lỗi: Mẫu số không được phép bằng 0!")
        self._mau_so = value


    def is_toi_gian(self):
        #Kiểm tra xem phân số đã tối giản chưa
        return math.gcd(abs(self.tu_so), abs(self.mau_so)) == 1

    def toi_gian(self):
        #Trả về một đối tượng PhanSo mới là dạng tối giản của phân số hiện tại
        ucln = math.gcd(abs(self.tu_so), abs(self.mau_so))
        new_tu = self.tu_so // ucln
        new_mau = self.mau_so // ucln
        

        if new_mau < 0:
            new_tu = -new_tu
            new_mau = -new_mau
            
        return PhanSo(new_tu, new_mau)


    def __add__(self, other):
        tu = self.tu_so * other.mau_so + other.tu_so * self.mau_so
        mau = self.mau_so * other.mau_so
        return PhanSo(tu, mau).toi_gian()

    def __sub__(self, other):
        tu = self.tu_so * other.mau_so - other.tu_so * self.mau_so
        mau = self.mau_so * other.mau_so
        return PhanSo(tu, mau).toi_gian()

    def __mul__(self, other):
        tu = self.tu_so * other.tu_so
        mau = self.mau_so * other.mau_so
        return PhanSo(tu, mau).toi_gian()

    def __truediv__(self, other):
        if other.tu_so == 0:
            raise ZeroDivisionError("Không thể chia cho phân số có tử số bằng 0.")
        tu = self.tu_so * other.mau_so
        mau = self.mau_so * other.tu_so
        return PhanSo(tu, mau).toi_gian()


    def __eq__(self, other):
        ps1 = self.toi_gian()
        ps2 = other.toi_gian()
        return ps1.tu_so == ps2.tu_so and ps1.mau_so == ps2.mau_so

    def __lt__(self, other):
        return (self.tu_so / self.mau_so) < (other.tu_so / other.mau_so)

    def __gt__(self, other):
        return (self.tu_so / self.mau_so) > (other.tu_so / other.mau_so)

    def __str__(self):
        ps = self.toi_gian()
        if ps.mau_so == 1:
            return str(ps.tu_so)
        if ps.tu_so == 0:
            return "0"
        return f"{ps.tu_so}/{ps.mau_so}"

    def __repr__(self):
        return f"PhanSo({self.tu_so}, {self.mau_so})"

    def __hash__(self):
        ps = self.toi_gian()
        return hash((ps.tu_so, ps.mau_so))

# Main

def main():
    danh_sach_ps = []
    
    print("--- NHẬP DANH SÁCH PHÂN SỐ ---")
    try:
        n = int(input("Bạn muốn nhập bao nhiêu phân số? "))
        for i in range(n):
            print(f"\nPhân số thứ {i+1}:")
            tu = int(input("  Nhập tử số: "))
            mau = int(input("  Nhập mẫu số: "))
            
            try:
                ps = PhanSo(tu, mau)
                danh_sach_ps.append(ps)
            except MauSoBangKhong as e:
                print(e)
                print("  -> Bỏ qua phân số này do lỗi mẫu số.")
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ!")
        return

    if not danh_sach_ps:
        print("\nDanh sách phân số trống!")
        return


    print("\n--- KẾT QUẢ ---")
    print("1. Dãy phân số (dạng tối giản):")
    # Sử dụng comprehension để lấy danh sách string đẹp
    print(", ".join(str(ps) for ps in danh_sach_ps))


    print("\n2. Dãy phân số sắp xếp tăng dần:")
    danh_sach_sorted = sorted(danh_sach_ps)
    print(", ".join(str(ps) for ps in danh_sach_sorted))


    print("\n3. Dãy phân số sau khi loại bỏ trùng lặp (Set):")
    danh_sach_set = set(danh_sach_ps)
    print(", ".join(str(ps) for ps in danh_sach_set))
    

    if len(danh_sach_ps) >= 2:
        ps1 = danh_sach_ps[0]
        ps2 = danh_sach_ps[1]
        print(f"\n4. Thử nghiệm phép toán với 2 phân số đầu ({ps1} và {ps2}):")
        print(f"  {ps1} + {ps2} = {ps1 + ps2}")
        print(f"  {ps1} * {ps2} = {ps1 * ps2}")

if __name__ == "__main__":
    main()