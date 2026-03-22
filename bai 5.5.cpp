#include <bits/stdc++.h>
using namespace std;
int main()
{
    time_t t = time(NULL);
    int day= t/86400;
    t=t%86400;
    int hour= t/3600;
    t=t%3600;
    int minute= t/60;
    t=t%60;
    cout<<day<<" days "<<hour<<" hours "<<minute<<" minutes "<<t<<" seconds since the epouch.";
    return 0;
}
