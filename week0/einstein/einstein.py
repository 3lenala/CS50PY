# This program aims to obtain the energy of a mass m according to E = m*c^2

C = 300000000
C_SQUARED = C * C

def main():
    mass = float(input('m: '))
    energy = int(mass * C_SQUARED)
    print('E: ', energy)

if __name__ == '__main__':
    main()
