#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long long MaxPairwiseProduct(const vector<int> & numbers){

    long long max_product = 0;
    int n = numbers.size();

    for (int first = 0; first < n; ++first){
        for (int second = first + 1; second < n; ++second){

            if ((long long)numbers[first] * numbers[second] > max_product){

                 max_product = ((long long)numbers[first] * numbers[second]);

            }
        }
    }

    return max_product;
}

long long MaxPairwiseProductFast(const vector<int> & numbers){
  int n = numbers.size();

  int max_index1 = -1;
  for (int first = 0; first < n; ++first){
    if ((max_index1 == -1) || (numbers[first] > numbers[max_index1])){
      max_index1 = first;
    }
  }

  int max_index2 = -1;
  for (int second = 0; second < n; ++second){
    if ((second != max_index1) && ((max_index2 == -1) || (numbers[second] > numbers[max_index2]))){
      max_index2 = second;
      }
  }

  return ((long long)(numbers[max_index1])) * numbers[max_index2];
}


int  main(){
    
    int n;
    cout << "Enter the length of the vector: ";
    cin >> n;
 
    cout <<"Enter " << n << " numbers: ";
    vector <int> numbers(n);
    for (int i=0; i < n; ++i){
        cin >> numbers[i];
    }

    long long result = MaxPairwiseProductFast(numbers);
    cout << result << '\n';
    return 0;
}



