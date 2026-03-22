import operator

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def main():
    arithmetic_expression_input = input('Expression: ')
    try:
        factors, operations = obtain_factors_and_operations(arithmetic_expression_input)
        result = execute_operation(factors, operations)
        print(result)
    except ValueError as exc:
        print(exc)
    except ZeroDivisionError as exc:
        print(exc)
    
    return

def obtain_factors_and_operations(arithmetic_expression_input: str) -> tuple[list[float], list[str]]:
    """Separates from the original expression a list with the factors and """
    factors = []
    factor = ''

    operations = []
    for character in arithmetic_expression_input:
        if character != ' ' and character not in OPERATIONS:
            factor += character
        elif character in OPERATIONS: 
            operations.append(character)
            try:
                number = float(factor)
            except ValueError as exc:
                raise ValueError('Invalid character in expression. Only numbers and operators (+, -, *, /) are allowed') from exc
            factors.append(number)
            factor = ''
    try:
        number = float(factor)
    except ValueError as exc:
        raise ValueError('Invalid expression introduced. Try again') from exc
    factors.append(number)

    return factors, operations

def execute_operation(factors: list[float], operations: list[str]) -> float:
    "Returns the result of the arithmetic expression"
    arithmetic_result = factors[0]
    for index in range(len(operations)):
        operation = operations[index]
        try: 
            arithmetic_result = OPERATIONS[operation](arithmetic_result, factors[index+1])
        except ZeroDivisionError as zde:
            raise ZeroDivisionError('Invalid expression: division by zero') from zde
    return arithmetic_result
    

if __name__ == '__main__':
    main()