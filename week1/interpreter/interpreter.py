# VERSION 1 FUNCIONA PARA SUMAS Y RESTAS DE LOS NUMEROS QUE SEAN Y CUALQUIER OPERACION DE DOS NUMEROS

OPERATIONS = {'+':0, '-':1, '*':2, '/':3}

def main():
    arithmetic_expression_input = input('Expression: ')
    factors,operations = obtain_factors_and_operations(arithmetic_expression_input)
    print(execute_operation(factors, operations)) 
    return

def obtain_factors_and_operations(arithmetic_expression_input: str) -> tuple[list[int], list[int]]:
    "Returns a list with the numbers involved in the expression and the opeartions relative to the notation in OPERATIONS"
    factors = []
    factor = ''
    factors_index = 0
    operations = []
    for character in arithmetic_expression_input:
        if character != ' ' and character not in OPERATIONS:
            factor += character
        elif character in OPERATIONS: 
            operations.append(OPERATIONS[character])
            factors.append(int(factor))
            factor = ''
    factors.append(int(factor))
    return factors, operations

def execute_operation(factors: list[int], operations: list[int]) -> float:
    "Returns the result of the arithmetic expression"
    index = 0
    arithmetic_result = factors[index]
    while index < (len(factors) - 1):
        index += 1
        for operation in operations:
            match operation:
                case 0:
                   arithmetic_result += factors[index]
                case 1:
                    arithmetic_result -= factors[index]
                case 2:
                    arithmetic_result *= factors[index]
                case 3:
                    arithmetic_result /= factors[index]
            index += 1

    return arithmetic_result
    


if __name__ == '__main__':
    main()