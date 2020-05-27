//http://www.cplusplus.com/doc/tutorial/arrays/
#include <iostream>
using namespace std;
int define_matrix();
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
   	define_matrix();

	return 0;
}

int define_matrix(){
	const size_t n = 5; 
   int a[n][n];
   a[0][0] = 1;
   for (int i=0; i<n; i++){
   		for (int j=0; j<n; j++){
   				a[i][j+1] = a[i][j]+1;
		   }
   }
   for (int i=0; i < n; i++){
   		cout << endl;
   		for(int j=0; j < n; j++){
			if (a[i][j] < 10 ){
				cout << a[i][j] << "  ";
			}else
			cout << a[i][j] << " ";

	   }
   }

}
