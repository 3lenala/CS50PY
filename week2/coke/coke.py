VALID_COINS = {25, 10, 5}
# lo que te importa no es el orden ni la repetición, sino consultar si un valor pertenece al conjunto -> {}

def main() -> None:
    owed_amount = 50
    while owed_amount > 0:
        print(f'Amount due: {owed_amount}')
        inserted_coin = get_valid_coin()
        owed_amount -= inserted_coin
    print(f'Change owed: {-owed_amount}')

def get_valid_coin() -> int:
    while True:
        try:
            inserted_coin = int(input('Insert coin: '))
            if is_valid_coin(inserted_coin):
                return inserted_coin
        except ValueError:
            print('Not a coin. Insert 25 cents, 10 cents or 5 cents')
            continue
        print('Invalid coin inserted. Insert 25 cents, 10 cents or 5 cents')

def is_valid_coin(inserted_coin: int) -> bool:
    return inserted_coin in VALID_COINS

if __name__ == '__main__':
    main()