#include <iostream>

using namespace std;
int fibonacci_naive(int n){
    if (n <=1)
        return n;
    else
        return fibonacci_naive(n - 1) + fibonacci_naive(n - 2);
}

int fibonacci_fast(int n){
int f[n+2];
int i;

f[0] = 0;
f[1] = 1;

for (i = 2; i <= n; i++)
{
    f[i] = f[i-1] + f[i-2];
}
return f[n];

}

int main(){

int n = 0;
cout << "Enter the number you want to calculate fibonacci: ",
cin >> n;

//cout << fibonacci_naive(n) << '\n';
cout << fibonacci_fast(n) << '\n';
return 0;
}