class Token:

    def __init__(self, string, t_type, asc=None):
        
        if t_type == 'OPERATOR' and asc == None:
            raise ValueError('Associativity required!')
        
        elif t_type != 'OPERATOR' and asc != None:
            raise ValueError("Non-operator token can't have an associativity!?")
        
        else:
            self.__string = string
            self.__type = t_type
            self.__op_asc = asc

    def get_precendance(self):
        op_l_associative = {'+' : 2, '-' : 2, '/' : 3, '*' : 3, '^' : 5}
        op_r_associative = {'-' : 4} 
        
        if self.__op_asc == None:
            raise ValueError(f'Token "{self.__string}" is not an operatator, impossible.')
        
        elif self.__op_asc == 'LEFT':
            return op_l_associative[self.__string]
        
        elif self.__op_asc == 'RIGHT':
            return op_r_associative[self.__string]
        
        else:
            raise ValueError('Unknown Operators!')
        
    def get_type(self):
        return self.__type
    
    def get_asc(self):
        return self.__op_asc
    
    def get_str(self):
        return self.__string
        
