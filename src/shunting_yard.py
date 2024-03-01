from Stack import Stack


def shunting_yard(tokens):
    stack = Stack()
    out_queue = []
    
    def from_stack_to_queue():
        out_queue.append(stack.pop())
    
    for token in tokens:
        
        if token.get_type() == 'INT_LITERAL' or token.get_type() == 'FLOAT_LITERAL':
            out_queue.append(token)
        
        elif token.get_type() == 'L_PARANTHESIS' or token.get_type() == 'FUNCTION':
            stack.push(token)

        elif token.get_type() == 'OPERATOR':
            
            if not stack.is_empty():
                
                while (stack.head().get_type() == 'OPERATOR' and
                        ((stack.head().get_precendance() > token.get_precendance() or 
                        (stack.head().get_precendance() == token.get_precendance() and
                        token.get_asc()=='LEFT')))):
                    
                    from_stack_to_queue()
                    
                    if stack.is_empty():
                        break
            
            stack.push(token)

        elif token.get_type() == 'R_PARANTHESIS':
            
            if stack.is_empty():
                raise ValueError('Non-balanced on paranthesis expression!')
            
            while stack.head().get_type() != 'L_PARANTHESIS':
                
                from_stack_to_queue()

                if stack.is_empty():
                    raise ValueError('Non-balanced on paranthesis expression!')
            
            stack.pop()
            
            if not stack.is_empty() and stack.head().get_type() == 'FUNCTION':
                from_stack_to_queue()

        elif token.get_type() == 'SEPARATOR':
            if stack.is_empty:
                raise ValueError('Paranthesis or separator missed!')
            
            while stack.head().get_type() != 'L_PARANTHESIS':
                from_stack_to_queue()

                if stack.is_empty():
                    raise ValueError('Paranthesis or separator missed!')
    
    while not stack.is_empty():
        
        if stack.head().get_type() == 'L_PARANTHESIS':
            raise ValueError('Paranthesis-unbalanced expression!') 
        else:
            from_stack_to_queue()   

    return out_queue