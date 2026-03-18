def main():
    mass = float(input('m: '))
    c = 300000000
    c_squared = c**2
    energy = int(mass * c_squared)
    print('E: ', energy)

if __name__ == '__main__':
    main()
