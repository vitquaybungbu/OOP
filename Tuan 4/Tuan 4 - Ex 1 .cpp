#include <bits/stdc++.h>
using namespace std;
class NhanVien{
private:
    string Ten;
    double luong;
    double heso;
public:
    static double MaxLuong;
    NhanVien(string a,double b, double c)
    {
        Ten = a;
        luong = b;
        heso = c;
    }
    string getN() {return Ten;}
    double getL() {return luong;}
    double geth() {return heso;}
    void setN(string s) {Ten = s;}
    void setl(double l) {luong = l;}
    void seth(double h) {heso = h;}
    double tl(){return luong*heso;}
    void inTTin()
    {
        cout<<"-----------THONG TIN NHAN VIEN----------\n";
        cout<<"Ten nhan vien: "<<Ten;
        cout<<fixed<<setprecision(0);
        cout<<"\nLuong co ban : "<<luong;
        cout<<setprecision(1);
        cout<<"\nHe so luong  : "<<heso;
        cout<<setprecision(0);
        cout<<"\nLuong thuc te: "<< tl();
        cout<<"\n----------------------------------------\n";
    }
    bool tangl(double p)
    {
        int heso2 = heso+p;
        int luongm = luong*heso2;
        if (luongm>MaxLuong) {
            cout<<"Luong moi vuot qua luong toi da.\nKhong tang luong.";
            return false;
        }
        else {
            luong=luongm;
            cout<<"Da tang he so luong. Luong moi: "
                <<fixed<<setprecision(0)<<tl();
                return true;
        }
    }
};
double NhanVien::MaxLuong = 5000000;
int main()
{
    NhanVien A("Duong Hoang An", 2000000, 2);
    A.inTTin();
    A.tangl(0.5);
    cout<<"\n";
    A.inTTin();
    A.tangl(1);
    cout<<"\n";
    cout<<"~~~~~~~~~~~~~GETTER/SETTER~~~~~~~~~~~~~~";
    cout<<"\nTen :"<<A.getN()<<endl;
    A.setl(50000000);
    cout<<fixed<<setprecision(0);
    cout<<"Luong co ban moi: "<<A.getL()<<endl;
    cout<<"Luong thuc te moi: "<<A.tl();
    return 0;
}
