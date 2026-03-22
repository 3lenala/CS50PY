# This program aims to obtain the energy of a mass m according to E = m*c^2
import math
# Convención habitual para definir constantes numéricas

SPEED_OF_LIGHT = 300_000_000
SPEED_OF_LIGHT_SQUARED = SPEED_OF_LIGHT ** 2

def main() -> None:
    try:
        mass = float(input('Mass (kg): '))
    except ValueError:
        print('Error: invalid numeric input.')
        return

    try:
        energy = calculate_energy(mass)
    except ValueError as exc:
        print(f'Error: {exc}')
        return
    
    print(f'Energy: {energy:.2e} J')
    return

def calculate_energy(mass: float) -> float:
    """Calculate energy using E = m * c^2."""
    if not math.isfinite(mass):
        raise ValueError('Mass must be a finite number.')
    if mass < 0:
        raise ValueError('Mass must be non-negative.')

    return mass * SPEED_OF_LIGHT_SQUARED

if __name__ == '__main__':
    main()

