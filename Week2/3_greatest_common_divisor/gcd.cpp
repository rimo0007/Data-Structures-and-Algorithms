#include <iostream>

using namespace std;

int gcd_naive(int a, int b){
    int current_gcd =1;

    for (int d = 2; d <= a && d<=b; d++){
        if (a % d == 0 && b % d == 0){
            if ( d > current_gcd)
                current_gcd = d;
        }

    }
    return current_gcd;

}

int euclidGCD(int a, int b){

    if (b==0) return a;
    return euclidGCD(b, a%b);

}

int main(){
    int a, b;
    cin >> a >> b;
    cout << "GCD: ";
    cout << "GCD using Naive approach: ";
    cout << gcd_naive(a, b) << '\n';
    cout << "GCD using Euclidean: ";
    cout << euclidGCD(a, b);

    return 0;

}

