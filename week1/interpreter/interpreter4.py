# The next step on the project is to implement operations hierarchy
# The first approximation to solve this problem will be to evaluate the list twice. First considering only
# multiplication and division, and a last one considering all the rest of the operations

import operator

POSSIBLE_OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def main():
    arithmetic_input = input('Expression: ')
    try:
        # You get the tokens of the expression
        numbers, operations = obtain_numbers_and_operations(arithmetic_input)
        # Executes the tokens from left to right
        result = operate(numbers, operations)
        print(result)
    except ValueError as exc:
        print(exc)
    except ZeroDivisionError as exc:
        print(exc)
    
    return

def obtain_numbers_and_operations(arithmetic_input: str) -> tuple[list[float], list[str]]:
    """Takes the original expression and generates two lists. One with all the numbers involved, and the other one with all the operations to be performed on those numbers"""
    numbers = []
    number = ''
    consecutive_operations = 0
    operations = []
    building_number = False

    for character in arithmetic_input:
        if character != ' ' and character not in POSSIBLE_OPERATIONS:
            number += character
            building_number = True
            consecutive_operations = 0

        elif character in POSSIBLE_OPERATIONS:
            consecutive_operations += 1

            if consecutive_operations == 2:
                if character == '-':
                    number += character
                else:
                    raise ValueError('Two consecutive operations in the expression.')
            elif consecutive_operations > 2:
                    raise ValueError('More than two consecutive operations in the expression.')
            
            # If we find an operation character on the first position of the arithmetic expression we include it as a part of the first factor (e.g.: negative number)
            if not building_number:
                number += character
                continue

            operations.append(character)
            float_number = conversion_to_float(number)
            numbers.append(float_number)
            number = ''
            building_number = False
    
    # The last number on the expression does not have an operation that follows it -> we turn it to float at the end
    float_number = conversion_to_float(number)
    numbers.append(float_number)
    number = ''

    return numbers, operations

def operate(numbers: list[float], operations: list[str]) -> float:
    """Returns the result of the arithmetic expression"""
    numbers_simplified, operations_simplified = higher_order_operations(numbers, operations)
    arithmetic_result = numbers_simplified[0]

    if operations_simplified:
        for index, operation in enumerate(operations_simplified):
            arithmetic_result = POSSIBLE_OPERATIONS[operation](arithmetic_result, numbers_simplified[index+1])
        

    return arithmetic_result

def higher_order_operations(numbers: list[float], operations: list[str]) -> tuple[list[float], list[str]]:
    """Executes all multiplication and division (higher order operations) simplifying the lists of values to operate"""
    simplified_numbers = []
    simplified_operations = []
    accumulation = False
    accumulated = 0


    for index, operation in enumerate(operations):
        current_number = numbers[index]
        next_number = numbers[index+1]
        # Keep the values and operations related with + or -
        if operation not in ('*','/'):
            if accumulation:
                simplified_numbers.append(accumulated)
                simplified_operations.append(operation)
                accumulation = False
                continue

            simplified_numbers.append(current_number)
            simplified_operations.append(operation)
            accumulation = False

        # Operate multiplication and division
        else:
            if not accumulation:
                accumulated = current_number
            try:
                accumulated = POSSIBLE_OPERATIONS[operation](accumulated, next_number)
                accumulation = True
            except ZeroDivisionError as zde:
                raise ZeroDivisionError('Division by zero is not allowed.') from zde
    if accumulation:
        simplified_numbers.append(accumulated)
    else:
        simplified_numbers.append(next_number)

    return simplified_numbers, simplified_operations

def conversion_to_float(number: str) -> float:
    """Convert numeric string to float"""
    try:
        float_number = float(number)
        return float_number
    except ValueError as exc:
        raise ValueError(f'Invalid number: {number!r}') from exc
    

if __name__ == '__main__':
    main()