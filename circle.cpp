#include <iostream>
#include <cmath>
using namespace std;

class Point {
public:
    double x, y;
    Point(double x = 0, double y = 0) : x(x), y(y) {}
};

class Rectangle {
public:
    Point  corner;    // góc dưới-trái
    double width, height;
    Rectangle(Point corner, double w, double h)
        : corner(corner), width(w), height(h) {}
};

class Circle {
public:
    Point  center;
    double radius;
    Circle(Point center, double radius)
        : center(center), radius(radius) {}
};

// Khoảng cách 2 điểm
double distance(const Point& a, const Point& b) {
    return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}

// Điểm trong/trên vòng tròn?
bool point_in_circle(const Circle& c, const Point& p) {
    return distance(c.center, p) <= c.radius;
}

// HCN nằm hoàn toàn trong vòng tròn?
bool rect_in_circle(const Circle& c, const Rectangle& r) {
    double x0 = r.corner.x, y0 = r.corner.y;
    double w  = r.width,     h  = r.height;
    // Kiểm tra 4 góc
    return point_in_circle(c, Point(x0,   y0))   &&
           point_in_circle(c, Point(x0+w, y0))   &&
           point_in_circle(c, Point(x0,   y0+h)) &&
           point_in_circle(c, Point(x0+w, y0+h));
}

// Bất kỳ góc nào của HCN giao với vòng tròn?
bool rect_circle_overlap(const Circle& c, const Rectangle& r) {
    double x0 = r.corner.x, y0 = r.corner.y;
    double w  = r.width,     h  = r.height;
    return point_in_circle(c, Point(x0,   y0))   ||
           point_in_circle(c, Point(x0+w, y0))   ||
           point_in_circle(c, Point(x0,   y0+h)) ||
           point_in_circle(c, Point(x0+w, y0+h));
}

int main() {
    Circle circle(Point(150, 100), 75);

    Point p1(150, 100);  // tâm → trong
    Point p2(300, 300);  // xa → ngoài
    cout << "p1 trong vong tron: "
         << (point_in_circle(circle, p1) ? "true" : "false") << "\n";
    cout << "p2 trong vong tron: "
         << (point_in_circle(circle, p2) ? "true" : "false") << "\n";

    Rectangle rSmall(Point(140, 90),  10,  10);
    Rectangle rLarge(Point(100, 50), 300, 200);
    cout << "rSmall trong circle:   "
         << (rect_in_circle(circle, rSmall) ? "true" : "false") << "\n";
    cout << "rLarge overlap circle: "
         << (rect_circle_overlap(circle, rLarge) ? "true" : "false") << "\n";

    return 0;
}
