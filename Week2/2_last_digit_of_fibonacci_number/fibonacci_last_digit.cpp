#include <iostream>

using namespace std;

long fibonacci_last_digit(long long n){

    int first = 0;
    int second = 1;
    int i;
    int res;

    for (i = 2; i <=n ; i++) {
        res = (first + second) % 10;
        first = second;
        second =res;

    }
    return res;
}

int main(){
    int n;
    cout <<"Enter the nth number you want to calculate for Fibonacci ";
    cin >> n;

   cout << fibonacci_last_digit(n);

}