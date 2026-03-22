#include <iostream>
#include <string>
#include <stdexcept>
#include <iomanip>
using namespace std;

class NhanVien {
private:
    string tenNhanVien;
    double luongCoBan;
    double heSoLuong;

public:
    // Static member — dùng chung cho tất cả đối tượng
    static constexpr double LUONG_MAX = 50000000.0;

    // Constructor
    NhanVien(const string& ten, double luong, double heSo)
        : tenNhanVien(ten), luongCoBan(luong), heSoLuong(heSo) {}

    // ── Getter ──────────────────────────────────────
    string getTenNhanVien() const { return tenNhanVien; }
    double getLuongCoBan()  const { return luongCoBan;  }
    double getHeSoLuong()   const { return heSoLuong;   }

    // ── Setter có validation ─────────────────────────
    void setTenNhanVien(const string& ten) {
        if (ten.empty())
            throw invalid_argument("Ten khong duoc rong!");
        tenNhanVien = ten;
    }
    void setLuongCoBan(double luong) {
        if (luong < 0)
            throw invalid_argument("Luong khong duoc am!");
        luongCoBan = luong;
    }
    void setHeSoLuong(double heSo) {
        if (heSo <= 0)
            throw invalid_argument("He so phai > 0!");
        heSoLuong = heSo;
    }

    // ── Phương thức nghiệp vụ ────────────────────────
    double tinhLuong() const {
        return luongCoBan * heSoLuong;
    }

    void inTTin() const {
        cout << fixed << setprecision(0);
        cout << "\n+--------------------------------------+\n"
             << "|      THONG TIN NHAN VIEN             |\n"
             << "+--------------------------------------+\n";
        cout << "| Ten       : " << left << setw(24) << tenNhanVien << "|\n";
        cout << "| Luong CB  : " << right << setw(18) << luongCoBan  << " VND |\n";
        cout << "| He so     : " << setw(21) << heSoLuong << ".0   |\n";
        cout << "| Luong TT  : " << setw(18) << tinhLuong() << " VND |\n";
        cout << "+--------------------------------------+\n";
    }

    bool tangLuong(double delta) {
        double luongMoi = (luongCoBan + delta) * heSoLuong;
        if (luongMoi > LUONG_MAX) {
            cout << "[!] Luong moi (" << luongMoi
                 << ") vuot LUONG_MAX. Khong tang!\n";
            return false;
        }
        luongCoBan += delta;
        cout << "[OK] Tang luong thanh cong! Luong moi: "
             << tinhLuong() << " VND\n";
        return true;
    }
};

int main() {
    NhanVien nv("Nguyen Van A", 10000000, 3.0);
    nv.inTTin();

    nv.tangLuong(5000000);   // 45M < 50M → OK
    nv.tangLuong(10000000);  // 75M > 50M → Cảnh báo

    return 0;
}
