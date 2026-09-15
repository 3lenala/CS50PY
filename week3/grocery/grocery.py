def get_items() -> list[str]:
    item_list = []
    while True:
        try:
            item = input()
        except (EOFError, KeyboardInterrupt):
            return item_list
        else:
            item_list.append(item)


def order(items: list[str]) -> list[str]:
    for i in range(len(items)):
        for j in range(len(items)-1):
            if out_of_order(items[j], items[j+1]):
                shorter, longer = compare(items[j], items[j+1])
                items[j] = shorter
                items[j+1] = longer
    return items

def out_of_order(item1, item2):
    if compare(item1, item2) != (item1, item2):
        return True

def compare(item1: str, item2: str) -> tuple[str, str]:
    def shorter_longer(item1: str, item2: str) -> tuple[str, str]:
        if len(item1) < len(item2):
            shorter = item1
            longer = item2
            return shorter, longer
        else:
            shorter = item1
            longer = item2
            return shorter, longer

    for i in range(min(len(item1), len(item2))):
        if item1[i] > item2[i]:
            lower = item2
            higher = item1
            return lower, higher
        elif item1[i] < item2[i]:
            lower = item1
            higher = item2
            return lower, higher
    return shorter_longer(item1, item2)

def main():
    items = get_items()
    items = order([items[i].upper().strip() for i in range(len(items))])
    i = 0
    while i < len(items):
        number_elements = items.count(items[i])
        print(f'{number_elements} {items[i]}')
        i += number_elements

if __name__ == '__main__':
    main()
