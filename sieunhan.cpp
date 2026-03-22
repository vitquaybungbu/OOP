#include <iostream>
#include <string>
using namespace std;

class SieuNhan {
private:
    string ten;
    string vuKhi;
    string mauSac;

public:
    // Constructor
    SieuNhan(string ten, string vuKhi, string mauSac)
        : ten(ten), vuKhi(vuKhi), mauSac(mauSac) {}

    // Getter
    string getTen()    const { return ten;    }
    string getVuKhi()  const { return vuKhi;  }
    string getMauSac() const { return mauSac; }

    // In thông tin — operator overload
    friend ostream& operator<<(ostream& os, const SieuNhan& sn) {
        os << "Sieu nhan " << sn.ten
           << " | Vu khi: " << sn.vuKhi
           << " | Mau sac: " << sn.mauSac;
        return os;
    }
};

int main() {
    SieuNhan sieu_nhan_A("A", "kiem", "do");
    SieuNhan sieu_nhan_B("B", "khien", "xanh");

    cout << sieu_nhan_A << endl;
    cout << sieu_nhan_B << endl;

    return 0;
}
