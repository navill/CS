#include <stdio.h>

int make_cmp(int a, int b, int num) {
	int c, ret;
	//c = a + b;
	__asm {
		mov eax, dword ptr[a]
		add eax, dword ptr[b]
		mov dword ptr[c], eax
	}
	
	/*if (c > num)
		ret=1;
	else
		ret=0;*/

	__asm {
		mov eax, dword ptr[c]
		cmp eax, dword ptr[num]
		jle SMALL
		mov dword ptr[ret], 01h		
		jmp FINE
		
		SMALL:
		mov dword ptr[ret], 00h

		FINE:
	}


	//return ret;
	__asm {
		mov eax, dword ptr[ret]
	}
}

int main(void) {
	int a, b, num, result;

	//a=10;
	__asm {
		mov dword ptr[a], 0Ah
	}

	//b=20;
	__asm {
		mov dword ptr[b], 14h
	}

	//num=15;
	__asm {
		mov dword ptr[num], 0Fh
	}

	//result = make_cmp(a, b, num);
	__asm {
		//push parameter to stack frame
		mov eax, dword ptr[num]
		push eax
		//push parameter to stack frame
		mov ecx, dword ptr[b]
		push ecx
		//push parameter to stack frame
		mov edx, dword ptr[a]
		push edx
		// call function
		call make_cmp
		//remove parameters
		add esp, 0Ch
		//assign the return value to result
		mov dword ptr[result], eax
	}

	if (result == 1)
		printf("%d + %d is greater than %d\n", a, b, num);
	else
		printf("%d + %d is less than %d\n", a, b, num);

	return 0;
}