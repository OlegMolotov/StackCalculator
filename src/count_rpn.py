from Stack import Stack
import math

def count_rpn(rpn_tokens):
    stack = Stack()
    res = None

    def get_one_token():
        if stack.is_empty():
            raise ValueError('Not enough arguments in function!')
        return stack.pop()
    
    def get_two_tokens():
        x = get_one_token()
        y = get_one_token()
        return (y, x)
    
    for token in rpn_tokens:
        string = token.get_str()

        if token.get_type() == 'INT_LITERAL':
            stack.push(float(string))

        elif token.get_type() == 'FLOAT_LITERAL':
            stack.push(float(string))

        elif token.get_type() == 'OPERATOR':
            
            if token.get_asc() == 'LEFT':
                a, b = get_two_tokens()
                
                if string == '+':
                    res = a + b
                
                elif string == '-':
                    res = a - b
                
                elif string == '*':
                    res = a * b
                
                elif string == '/':
                    try:
                        res = a / b
                    except ZeroDivisionError as e:
                        print(e)
                
                elif string == '^':
                    res = math.pow(a, b)
                
                else:
                    raise ValueError('Unknown operator!')
            
            elif token.get_asc() == 'RIGHT':
                a = get_one_token()

                if string == '-':
                    res = -a
                else:
                    raise ValueError('Unknown operator!')
            
            stack.push(res)

        elif token.get_type() == 'FUNCTION':
            
            if string == 'log2':
                a = get_one_token()
                try:
                    res = math.log2(a)
                except Exception as e:
                    print(e)
            
            elif string == 'sqrt':
                a = get_one_token()
                try:
                    res = math.sqrt(a)
                except Exception as e:
                    print(e)
            else:
                raise ValueError('Unknown function!')
            
            stack.push(res)
    
    return stack.pop()