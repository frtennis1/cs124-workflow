#include <iostream>
#include <string>
#include <cstdlib>
#include <iterator>
using namespace std;
int main() {
      int n;
      cin >> n;
      int arr[n];
      bool test = true;
      if (test){
          for (int i =0; i<n; i++){  // Generate random test data
            int k = rand() % 100;
            arr[i] = k;
          }
      }
      Else{                 // Read test data from a file
        for (int i = 0; i<n; i++){
            int k;
            cin >> k;
            arr[i] = k;
        }
      }      
    for (int i = 0; i < n; i++){
      cout << arr[i] << " ";
    }
      cout << "\n"; 
      return 0;
}
