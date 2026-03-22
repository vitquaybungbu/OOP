#include <bits/stdc++.h>;
using namespace std;
void pp(int n)
{
    for (int i=1;i<=n;i++){
    for (int j=1;j<=9;j++) cout<<" ";
    cout<<"|";
    }
}
void ve(int row, int col)
{
    for (int i=1;i<row;i++)
    {
        cout<<"+ ";
        int dem = 1;
        while (dem!=col)
        {
            for (int j=1;j<=4;j++) cout<<"- ";
            cout<<"+ "; dem++;
        }
        for (int i=1;i<=4;i++)
        {
            cout<<"\n|";pp(col-1);
        }
        cout<<endl;
    }
    cout<<"+ ";
    for (int i=1;i<col;i++)
    {
        for (int j=1;j<=4;j++) cout<<"- ";
        cout<<"+ ";
    }
    cout<<endl;
}
int main()
{
    ve(3,3);
    ve(4,4);
    ve(10,10);
    return 0;
    // biết thế gán xâu cho nhanh :))
}
