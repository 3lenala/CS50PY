# VERSION 1 FUNCIONA PARA SUMAS Y RESTAS DE LOS NUMEROS QUE SEAN Y CUALQUIER OPERACION DE DOS NUMEROS

OPERATIONS = {'+':0, '-':1, '*':2, '/':3}

def main():
    arithmetic_expression_input = input('Expression: ')
    print(execute_operation(arithmetic_expression_input)) 
    return

def execute_operation(arithmetic_expression_input: str) -> float:
    "Returns a list with the numbers involved in the expression and the opeartions relative to the notation in OPERATIONS"
    current_factor = ''
    previous_factor = 0
    arithmetic_result = 0

    for character in arithmetic_expression_input:
        if character != ' ' and character not in OPERATIONS:
            current_factor = current_factor + character
        elif character in OPERATIONS:
            operation = OPERATIONS[character]
            match OPERATIONS[character]:
                case 0:
                   arithmetic_result = previous_factor + float(current_factor)
                case 1:
                    arithmetic_result = previous_factor - float(current_factor)
                case 2:
                    arithmetic_result = previous_factor * float(current_factor)
                case 3:
                    arithmetic_result = previous_factor / float(current_factor)
            previous_factor = float(current_factor)
            current_factor = ''
    return arithmetic_result


if __name__ == '__main__':
    main()