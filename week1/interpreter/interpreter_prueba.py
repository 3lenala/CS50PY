

def operate_high_priority(numbers: list[float], operations: list[str]) -> tuple[list[float], list[str]]:
    """Resolve multiplication and division first."""
    simplified_numbers = [numbers[0]]
    simplified_operations = []

    for index, operation in enumerate(operations):
        next_number = numbers[index + 1]

        if operation in ('*', '/'):
            try:
                simplified_numbers[-1] = POSSIBLE_OPERATIONS[operation](simplified_numbers[-1], next_number)
            except ZeroDivisionError as exc:
                raise ZeroDivisionError('Division by zero is not allowed.') from exc
        else:
            simplified_operations.append(operation)
            simplified_numbers.append(next_number)

    return simplified_numbers, simplified_operations
