#include <iostream>

using namespace std;

int euclidGCD(int a, int b){

    if (b==0) return a;
    
    return euclidGCD(b, a%b);
}

long long lcm_naive(long long a, long long b){
    
    return (a*b)/euclidGCD(a, b);
}

int main(){
int a;
int b;

cout << "Enter the numbers you want to calculate the LCM: ";
cin >> a >> b;

cout << "The LCM is: " ;
cout << lcm_naive(a, b);
return 0;
}