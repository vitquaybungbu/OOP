#include <bits/stdc++.h>
using namespace std;
class Point{
    private:
        int x,y;
    public:
        Point(int x,int y): x(x), y(y) {}
        int getx() {return x;}
        int gety() {return y;}
        void setx(int a) {x=a;}
        void sety(int b) {y=b;}
        void pp() {
            cout<<"Point("<<x<<","<<y<<")";
        }
};
class LineSegment{
    private:
        Point d1,d2;
    public:
        Point get1() {return d1;}
        Point get2() {return d2;}
        LineSegment(): d1(Point(8,5)), d2(Point(1,0)){}
        LineSegment(Point a,Point b): d1(a), d2(b) {}
        LineSegment(int a, int b, int c, int d):
            d1(Point(a,b)),d2(Point(c,d)) {}
        LineSegment(const LineSegment& other):
            d1(other.d1), d2(other.d2) {}
        double dis()
        {
            int dx = d1.getx() - d2.getx();
            int dy = d1.gety() - d2.gety();
            return sqrt(dx*dx+dy*dy);
        }
        void hienthi() {
            cout << "LineSegment[";d1.pp();
            cout << " -> ";d2.pp();cout << "]";
            cout << "\nDo dai: "<<dis()<<endl;
        }
};
LineSegment a[100];
int b[100];
int maxx,c;
int main()
{
    cout<<fixed<< setprecision(2);
    LineSegment Line1;
    cout<<"Line1(Mac dinh): ";Line1.hienthi();
    a[1] = Line1;maxx = Line1.dis(); c=1;
    Point p1(3,6); Point p2(6,7);
    LineSegment Line2(p1,p2);
    cout<<"Line2(2 Points): ";Line2.hienthi();
    a[2] = Line2;
    if (Line2.dis()>maxx) {maxx = Line2.dis(); c=2;}
    LineSegment Line3(1,2,3,4);
    cout<<"Line3(4 toa do): ";Line3.hienthi();
    if (Line3.dis()>maxx) {maxx = Line3.dis(); c=3;}
    LineSegment Line4(Line2);
    cout<<"Line4(copy Line2): ";Line4.hienthi();
    cout<<"Longest line is: ";a[c].hienthi();
    return 0;
}
