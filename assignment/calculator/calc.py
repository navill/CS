from stack import Stack

def get_weight(oprt):
    """
    get_weight(operator)-> value
    operator : '*' or '/' or '+' or '-' or '('
    value : 가중치
    """
    if oprt=='*' or oprt=='/':
        return 9
    elif oprt=='+' or oprt=='-':
        return 7
    elif oprt=='(':
        return 5

def convert_to_postfix(infix_expression):
    """
    convert_to_postfix(infix_expression)->postfix_expression
    infix_expression : 중위 표기법 수식
    입력받은 문자열입니다.
    postfix_expression : 후위 표기법 수식
    반환값도 문자열입니다. 
    """
    exp_list=[]
    oprt_stack=Stack()

    for ch in infix_expression:
        if ch.isdigit():
            exp_list.append(ch)
        else:
            if oprt_stack.empty() or ch=='(':
                oprt_stack.push(ch)
            elif ch==')':
                op=oprt_stack.pop()
                while op!='(':
                    exp_list.append(op)
                    op=oprt_stack.pop()
            elif get_weight(ch) > \
                get_weight(oprt_stack.peek()):
                oprt_stack.push(ch)
            else:
                while not oprt_stack.empty() and get_weight(ch) <=\
                    get_weight(oprt_stack.peek()):
                    exp_list.append(oprt_stack.pop())
                oprt_stack.push(ch)
    while not oprt_stack.empty():
        exp_list.append(oprt_stack.pop())

    return ''.join(exp_list)

def calc_two_oprd(oprd1, oprd2, oprt):
    """
    calc_two_oprd(oprd1, oprd2, oprt)->value
    oprd1, oprd2 : 피연산자입니다. 정수형 데이터를 받습니다.
    oprt : 연산자입니다. 문자입니다. 예를 들어, '+', '/', '*', '/'
    value : 반환값은 두 피연산자를 연산자로 계산한 결과입니다.
    """
    if oprt=='+':
        return oprd1+oprd2
    elif oprt=='-':
        return oprd1-oprd2
    elif oprt=='*':
        return oprd1*oprd2
    elif oprt=='/':
        return oprd1//oprd2

def calculate(postfix_expression):
    """
    calculate(postfix_expression)->value
    postfix_expression : 후위표기법 수식입니다.
    문자열입니다.
    value : 후위표기법 수식을 계산한 결과입니다.
    """
    oprd_stack=Stack()

    for ch in postfix_expression:
        if ch.isdigit():
            oprd_stack.push(int(ch))
        else:
            oprd2=oprd_stack.pop()
            oprd1=oprd_stack.pop()
            oprd_stack.push(calc_two_oprd(oprd1, oprd2, ch))

    return oprd_stack.pop()
if __name__=="__main__":
    while True:
        infix_exp=input("수식을 입력하세요 (종료:0):")
        infix_exp=infix_exp.replace(' ', '')
        if infix_exp=='0':
            break
        postfix_exp=convert_to_postfix(infix_exp)
        print(postfix_exp)
        print('{exp}={result}'.format(exp=infix_exp, result=calculate(postfix_exp)))
    

