#include <stdio.h>

//전역변수 
//data segment
//생성 : 프로세스 생성
//소멸 : 프로세스 소멸
int g_num = 10;

//지역변수
//생성 : 함수 호출시
//소멸 : 함수 종료시
int func(int a, int b, int ** dbl_ptr) {
	int c;
	c = a + b;
	//heap 영역에 할당
	//생성 시점 : 내가 원할 때
	*dbl_ptr = (int*)malloc(sizeof(int));
	**dbl_ptr = c;

	return c;
}

int main(void) {
	int a = 10;
	int b = 20;
	int * ptr = NULL;

	func(a, b, &ptr);

	printf("%d \n", *ptr);

	//heap 영역의 메모리 해제 시점
	//해제 : 내가 원할 때
	free(ptr);
	ptr = NULL;



	return 0;
}