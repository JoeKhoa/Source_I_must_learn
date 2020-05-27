 
#include <iostream>
using namespace std;

// main() is where program execution begins.
int main() {
	int A[5][5],i,j;
	A[0][0] = 0;
	for(i=1; i<5;i++){
		for(j=1;j<i+1;j++){
			A[i][j] = 1;
		}
	}
	for(i=1;i<5;i++){
		cout << endl;
		for(j=1;j<j+1;j++){
			cout << A[i][j];
		}
	}
//	int n=5, x[n] = {1,3,5,1,4},i;
//	for (i=0; i < n;i++){
//		cout << x[i];
//	}
//	return 0;

}
