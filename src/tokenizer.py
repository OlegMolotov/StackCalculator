from Token import Token


def tokenize(expr):
    state = 0
    tokens = []
    valid_operators = "+-*^/"

    buffer = ''
    buffer_token_type = 'INT_LITERAL'

    def tokenize_op_paranth_sep():
        if is_op:
            if not tokens or tokens[-1].get_type() == 'L_PARANTHESIS':
                tokens.append(Token(s, 'OPERATOR', 'RIGHT'))
            else:
                tokens.append(Token(s, 'OPERATOR', 'LEFT'))
        
        elif is_paranth:
            tokens.append(Token(s, 'R_PARANTHESIS' if is_r_paranth else 'L_PARANTHESIS'))
        
        elif is_sep:
            tokens.append(Token(s, 'SEPARATOR'))
    
    for s in expr:
        is_digit = s.isdigit()
        is_letter = s.isalpha()
        is_l_paranth = s == '('
        is_r_paranth = s == ')'
        is_paranth = is_l_paranth or is_r_paranth
        is_point = s == '.'
        is_sep = s == ','
        is_op = s in valid_operators

        if not (is_digit or is_letter or is_paranth or is_point or is_sep or is_op):
            raise ValueError(f'Unknown symbol: {s}')
        
        if state == 0:
            if is_op or is_paranth:
                state = 1
            elif is_digit:
                state = 2
            elif is_letter:
                state = 4
            elif is_point or is_sep:
                raise ValueError(f'Unexpected symbol: {s}')
                   
        elif state == 1:
            if is_digit:
                state = 2
            elif is_letter:
                state = 4
            elif is_point or is_sep:
                raise ValueError(f'Unexpected symbol: {s}')
                   
        elif state == 2:
            buffer_token_type = 'INT_LITERAL'
            if is_point:
                state = 3
            elif is_paranth or is_op or is_sep:
                state = 5
            elif is_letter:
                raise ValueError(f'Unexpected symbol: {s}')
            
        elif state == 3:
            buffer_token_type = 'FLOAT_LITERAL'
            if is_paranth or is_op or is_sep:
                state = 5
            elif is_point:
                raise ValueError(f'Unexpected symbol: {s}')
            
        elif state == 4:
            buffer_token_type = 'FUNCTION'
            if is_l_paranth:
                state = 5
            elif is_op or is_r_paranth or is_sep:
                raise ValueError(f'Unexpected symbol: {s}')
            
        elif state == 5:
            if is_paranth or is_op:
                state = 1
            elif is_digit:
                state = 2
            elif is_letter:
                state = 4
            elif is_point or is_sep:
                raise ValueError(f'Unexpected symbol: {s}')
                        
        if state == 1:
            tokenize_op_paranth_sep()
                
        elif state == 2 or state == 3 or state == 4:
            buffer += s
            
        elif state == 5:
            tokens.append(Token(buffer, buffer_token_type))
            buffer = ''
            tokenize_op_paranth_sep()
    
    if buffer:
        tokens.append(Token(buffer, buffer_token_type))
    
    return tokens