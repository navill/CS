from stack import Stack

class Calculator:
    def __init__(self):
        self.org_exp=None
        self.postfix_exp=None
        self.result=None
    
    def set_org_exp(self, org_exp):
        self.org_exp=org_exp.replace(' ', '')
        self.postfix_exp=None
        self.result=None

    def get_org_exp(self):
        return self.org_exp

    def get_weight(self, oprt):
        if oprt=='*' or oprt=='/':
            return 9
        elif oprt=='+' or oprt=='-':
            return 7
        elif oprt=='(':
            return 5

    def convert_to_postifx(self):
        pass

    def get_postfix_exp(self):
        if not self.org_exp:
            return None

        if not self.postfix_exp:
            self.convert_to_postifx()

        return self.postfix_exp

    def calc_two_oprd(self, oprd1, oprd2, oprt):
        if oprt=='+':
            return oprd1+oprd2
        elif oprt=='-':
            return oprd1-oprd2
        elif oprt=='*':
            return oprd1*oprd2
        elif oprt=='/':
            return oprd1//oprd2

    def calculate(self):
        pass

    def get_result(self):
        if not self.org_exp:
            return None
        
        if not self.result:
            self.calculate()
        
        return self.result

if __name__=="__main__":
    calc=Calculator()

    while True:
        exp=input("수식을 입력하세요 (종료:0):")
        if exp=='0':
            break
        calc.set_org_exp(exp)
        print(calc.get_postfix_exp())
        print('{exp}={result}'.format(exp=calc.get_org_exp(), 
        result=calc.get_result()))
