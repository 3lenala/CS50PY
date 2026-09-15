def get_items() -> tuple:
    appearances = {}
    items = []
    while True:
        try:
            item = input().upper().strip()
        except (EOFError, KeyboardInterrupt):
            return appearances, items
        if item == '':
            return appearances, items
        if item in appearances:
            appearances[item] += 1
        else:
            appearances[item] = 1
            items.append(item)


def bubble_sort(items: list[str]) -> list[str]:
    for _ in range(len(items)):
        for j in range(len(items)-1):
            if out_of_order(items[j], items[j+1]):
                lower, higher = items[j+1], items[j]
                items[j] = lower
                items[j+1] = higher
    return items


def out_of_order(item1, item2):

    def sort_pair(item1: str, item2: str) -> tuple[str, str]:
        for i in range(min(len(item1), len(item2))):
            if item1[i] > item2[i]:
                lower = item2
                higher = item1
                return lower, higher
            elif item1[i] < item2[i]:
                lower = item1
                higher = item2
                return lower, higher

        if len(item1) < len(item2):
            return item1, item2
        return item2, item1

    if sort_pair(item1, item2) != (item1, item2):
        return True
    return False


def main():
    appearances, items = get_items()
    items = bubble_sort(items)
    for item in items:
        try:
            print(f'{appearances[item]} {item}')
        except KeyError:
            raise KeyError(f'The algorithm did not successfully captured item {item}')


if __name__ == '__main__':
    main()