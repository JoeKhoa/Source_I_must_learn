#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;

	int So_to(int Amount, int size, int A[]){
		int n = Amount/A[size-1];
		int k = Amount % A[size-1];
		if (k == 0 && n==0) {
			return n; 
		}
		else{
			for (int i=n-1; i>0; i--){
				if (!k%A[i]){
					return n+1;
				}
				else{
					return n+So_to(k%A[i],size-2,A);
				}
			}
		}
		return 0;
	}

int main(int argc, char** argv) {
	int A[4] = {2,5,7,11};
	int Amount_A = 57;
	int size_A = sizeof(A);

	int x = So_to(Amount_A, size_A, A);
	cout << x;


 	
}
