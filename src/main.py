from tokenizer import tokenize
from shunting_yard import shunting_yard
from count_rpn import count_rpn

def calculate(expression):
    try:
        res = count_rpn(shunting_yard(tokenize(expression)))
        return res
    except Exception as e:
        res = e
        return res



if __name__ == '__main__':
    expression = "log2(23)+(-2/(3.14))*(sqrt(0.1*10^(-3)/0.02))"
    print(calculate(expression))