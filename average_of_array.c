#include <stdio.h>
float array[6] = {1,2,3,4,5,6};
float summer = 0;
int itter;
float diver = 0;
int main(){
	for(itter=0; itter<6; itter++){
		summer += array[itter];
		diver += 1;
	}
	summer = summer / diver;
	printf("%f", summer);
	return 0;
}


