#include <bits/stdc++.h>
using namespace std;
int main()
{
    float t = 42*60+42;
    cout<<"42 minutes 42 seconds = "<<t<<" seconds. \n";
    float d = 10/1.61;
    cout<<"10 kilometers = "<<d<<" miles. \n";
    float ap = t/d;
    int m = ap/60;
    cout<<"Average pace: "<<m<<" minutes "<<ap-60*m<<" seconds per mile. \n";
    cout<<"Average speed: "<<d/(t/3600)<< " miles per hour.";
    return 0;
}
