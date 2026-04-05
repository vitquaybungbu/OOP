class HangHoa:
    def __init__(self, id, name, busi):
        self.__id  = id
        self.__name = name
        self.__busi  = busi
    def getid(self):   return self.__id
    def getname(self):  return self.__name
    def getbusi(self):    return self.__busi
    def view(self):
        print(f" Mã hàng  : {self.__id}")
        print(f" Tên hàng : {self.__name}")
        print(f" Nhà SX   : {self.__busi}")
class HangDienMay(HangHoa):
    def __init__(self, id, name, busi, price, maint, dien_ap, cong_suat):
        super().__init__( id, name, busi)
        self.__price        = price
        self.__maint = maint 
        self.__dien_ap    = dien_ap      
        self.__cong_suat  = cong_suat    
    def show(self):
        print("═══ HÀNG ĐIỆN MÁY ═══")
        super().view()          
        print(f"  Giá      : {self.__price:,.0f} VNĐ")
        print(f"  Bảo hành : {self.__maint} tháng")
        print(f"  Điện áp  : {self.__dien_ap} V")
        print(f"  Công suất: {self.__cong_suat} W")
class HangSanhSu(HangHoa):
    def __init__(self, id, name, busi,
                 price, ingr):
        super().__init__(id, name, busi)
        self.__price              = price
        self.__ingr = ingr
    def hien_thi(self):
        print("═══ HÀNG SÀNH SỨ ═══")
        super().view()
        print(f"  Giá         : {self.__price:,.0f} VNĐ")
        print(f"  Nguyên liệu : {self.__ingr}")
class HangThucPham(HangHoa):
    def __init__(self, id, name, busi, price, date1, date2):
        super().__init__(id, name, busi)
        self.__gia   = price
        self.__date1 = date1
        self.__date2 = date2 
    def hien_thi(self):
        print("═══ HÀNG THỰC PHẨM ═══")
        super().view()
        print(f"  Giá        : {self.__price:,.0f} VNĐ")
        print(f"  Ngày SX    : {self.__date1}")
        print(f"  Hết hạn    : {self.__date2}")
dm = HangDienMay(
    "DM001", "Tủ lạnh Inverter 360L", "Samsung",
    12_500_000, 24, 220, 150
)

ss = HangSanhSu(
    "SS001", "Bộ chén sứ Minh Long", "Minh Long",
    850_000, "Sứ cao cấp"
)

tp = HangThucPham(
    "TP001", "Cà phê rang xay Aura Brew", "Aura Brew",
    185_000, "01/03/2026", "01/03/2027"
)
dm.view()
print()
ss.view()
print()
tp.view()