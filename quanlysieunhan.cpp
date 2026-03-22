
#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
using namespace std;

class SieuNhan {
public:
    string ten, vuKhi, mauSac;
    int    sucManh;

    SieuNhan(string ten, string vuKhi,
             string mauSac, int sucManh)
        : ten(ten), vuKhi(vuKhi),
          mauSac(mauSac), sucManh(sucManh) {}

    void inThongTin(int stt) const {
        cout << setw(2) << stt << ". "
             << "[" << left << setw(10) << ten << "]"
             << " Vu khi: " << setw(8) << vuKhi
             << " Mau: "    << setw(8) << mauSac
             << " Suc manh: " << sucManh << endl;
    }
};

int main() {
    vector<SieuNhan> danhSach;
    string ten, vuKhi, mauSac;
    int sucManh;

    cout << "=== NHAP DANH SACH SIEU NHAN ===\n";
    cout << "(Nhan Enter de ket thuc)\n\n";

    // Dùng while để nhập danh sách
    while (true) {
        cout << "Ten sieu nhan: ";
        getline(cin, ten);
        if (ten.empty()) break;

        cout << "Vu khi: ";   getline(cin, vuKhi);
        cout << "Mau sac: ";  getline(cin, mauSac);
        cout << "Suc manh: "; cin >> sucManh;
        cin.ignore();

        danhSach.emplace_back(ten, vuKhi, mauSac, sucManh);
        cout << "  --> Da them " << ten << "!\n\n";
    }

    // Dùng for in danh sách kèm thuộc tính
    cout << "\n=== DANH SACH " << danhSach.size() << " SIEU NHAN ===\n";
    int i = 1;
    for (const auto& sn : danhSach) {
        sn.inThongTin(i++);
    }

    return 0;
}
