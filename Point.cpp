#include <bits/stdc++.h>
using namespace std;
class Point {
    private:
        int x, y;
    public:
        Point() : x(0), y(0) {}
        Point(int x, int y) : x(x), y(y) {}
        int getX() const { return x; }
        int getY() const { return y; }
        void setX(int x) { this->x = x; }
        void setY(int y) { this->y = y; }
        void hienThi() const { cout << "(" << x << ", " << y << ")" << endl;}
        Point doiXungQuaO() const {
             return Point(-x, -y);
        }
        double khoangCachDenO() const {
            return sqrt(x*x + y*y);
        }
        double khoangCachDen(const Point& other) const {
            int dx = x - other.x;
            int dy = y - other.y;
            return sqrt(dx*dx + dy*dy);
        }
};

int main() {
    Point A(3, 4);
    cout << "Diem A: "; A.hienThi();
    int xb, yb;
    cout << "Nhap x cua B: "; cin >> xb;
    cout << "Nhap y cua B: "; cin >> yb;
    Point B(xb, yb);
    cout << "Diem B: "; B.hienThi();
    Point C = B.doiXungQuaO();
    cout << "Diem C (doi xung B qua O): "; C.hienThi();
    cout << fixed << setprecision(2);
    cout << "d(B, O) = " << B.khoangCachDenO() << endl;
    cout << "d(A, B) = " << A.khoangCachDen(B) << endl;

    return 0;
}
