#include <bits/stdc++.h>
using namespace std;
int main()
{
    float V = (4/3)*M_PI*pow(5,3);
    cout<<"The volume of a sphere with radius 5: "<<V;
    float price = 24.95*40/100;
    cout<<"\nThe total whole cost for 60 copies: "<<price*60+3+0.75*59;
    int t1=(8*60+15)*2;
    int t2=(7*60+12)*3;
    int t= (t1+t2)%60;
    int T= (t1+t2-t)/60 + 52;
    cout<<"\nTime "<<6+(T-T%60)/60<<":"<<T%60<<":"<<t;
    return 0;
}
