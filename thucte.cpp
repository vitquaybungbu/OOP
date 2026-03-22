#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// ====================================================
// LỚP 1: CON CHÓ
// ====================================================
class ConCho {
private:
    string ten, mauSac, giong, camXuc;

public:
    ConCho(string ten, string mauSac,
           string giong, string camXuc = "vui")
        : ten(ten), mauSac(mauSac),
          giong(giong), camXuc(camXuc) {}

    void sua() const {
        cout << ten << ": Gau gau!\n";
    }
    void vayDuoi() const {
        cout << ten << " vay duoi vi " << camXuc << "!\n";
    }
    void an(string thucAn) const {
        cout << ten << " dang an " << thucAn << ". Ngon!\n";
    }
    void chay(int tocDo) const {
        cout << ten << " chay " << tocDo << " km/h!\n";
    }
};

// ====================================================
// LỚP 2: Ô TÔ
// ====================================================
class OTo {
private:
    string hang, kichThuoc, mau;
    double gia;
    int    tocDo = 0;

public:
    OTo(string hang, string kichThuoc,
        string mau, double gia)
        : hang(hang), kichThuoc(kichThuoc),
          mau(mau), gia(gia) {}

    void tangToc(int them) {
        tocDo += them;
        cout << "Tang toc! Toc do: " << tocDo << " km/h\n";
    }
    void giamToc(int bot) {
        tocDo = max(0, tocDo - bot);
        cout << "Giam toc! Toc do: " << tocDo << " km/h\n";
    }
    void dam() {
        cout << "[!] Xe " << hang << " bi dam! Dung khán cap.\n";
        tocDo = 0;
    }
};

// ====================================================
// LỚP 3: TÀI KHOẢN
// ====================================================
class TaiKhoan {
private:
    string tenTK, soTK, nganHang;
    double soDu;

public:
    TaiKhoan(string tenTK, string soTK,
             string nganHang, double soDu = 0)
        : tenTK(tenTK), soTK(soTK),
          nganHang(nganHang), soDu(soDu) {}

    void rut(double soTien) {
        if (soTien > soDu)
            cout << "[X] So du khong du!\n";
        else {
            soDu -= soTien;
            cout << "[OK] Rut " << soTien
                 << " VND. Con lai: " << soDu << "\n";
        }
    }
    void gui(double soTien) {
        soDu += soTien;
        cout << "[OK] Gui " << soTien
             << " VND. So du: " << soDu << "\n";
    }
    void kiemTraSoDu() const {
        cout << "[TK: " << tenTK << "] So du: "
             << soDu << " VND\n";
    }
};

int main() {
    // Con chó
    ConCho cho("Milo", "vang", "Golden Retriever");
    cho.sua(); cho.an("xuong"); cho.chay(30);

    cout << endl;

    // Ô tô
    OTo xe("Toyota", "sedan", "trang", 800000000);
    xe.tangToc(60); xe.tangToc(40); xe.giamToc(30);

    cout << endl;

    // Tài khoản
    TaiKhoan tk("Nguyen Van A", "123456", "Vietcombank", 5000000);
    tk.gui(2000000); tk.rut(3000000); tk.kiemTraSoDu();

    return 0;
}
