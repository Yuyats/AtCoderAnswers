#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <deque>
#include <math.h>
#include <cstring>
#include <string.h>
#include <iomanip>
#include <stdlib.h>
#include <queue>
#include <stack>
#include<cassert>
#include <cfloat>
#include <list>
using namespace std ;
#define ll long long
#define submitStage int TCF = 1 ;
#define testStage int TCF = 1000 ;
#define testMyStupedCode TCF--
void FastInputOutput(){
    ios_base :: sync_with_stdio( 0 ) ;
    cin.tie( 0 ) ;
    cout.tie( 0 ) ;
}
void ReadFromFile( string name , string extention ){
    string fullPath = name + "." + extention ;
    freopen( fullPath.c_str() , "r" , stdin ) ;
}
inline int D(){
    int t ;
    scanf( "%d" , &t ) ;
    return t ;
}
inline ll LLD(){
    ll t ;
    scanf( "%lld" , &t ) ;
    return t ;
}
inline char C(){
    char c ;
    scanf( "%c" , &c ) ;
    return c ;
}
inline ll power(ll x, ll p, ll m){
    ll res = 1;
    while(p){
        if(p & 1)
            res = (res * x) % m;
        x = (x * x) % m;
        p >>= 1;
    }
    return res;
}
long double ModLog(long double base, long double x) {
    return (logl(x) / logl(base));
}

const int N = 3e3 + 5;
int dp[N][N], n, m;
char a[N], b[N];

void print(int i, int j){
     if(!i || !j)
          return;
     int ret = dp[i][j];
     if(ret == dp[i - 1][j])
          print(i - 1, j);
     else if(ret == dp[i][j - 1])
          print(i, j - 1);
     else{
          print(i - 1, j - 1);
          printf("%c", a[i - 1]);
     }
}
int main(){
     scanf("%s %s", a, b);
     n = strlen(a);
     m = strlen(b);
     for(int i = 1; i <= n; ++i)
          for(int j = 1; j <= m; ++j)
               if(a[i - 1] == b[j - 1])
                    dp[i][j] = dp[i - 1][j - 1] + 1;
               else
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
     print(n, m);
     return 0;
}

