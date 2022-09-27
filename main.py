import os

from prettytable import PrettyTable


def folder_size(p):
    size = 0
    if os.path.isdir(p):
        try:
            for e in os.listdir(p):
                size += folder_size(os.path.join(p, e))
        except PermissionError:
            pass
    else:
        try:
            size = os.path.getsize(p)
        except PermissionError:
            pass
    return size


def format_size(size: int):
    if size < 1e3:
        return f'{size} B'
    elif size < 1e6:
        return f'{size / 1e3:.2f} KB'
    elif size < 1e9:
        return f'{size / 1e6:.2f} MB'
    else:
        return f'{size / 1e9:.2f} GB'


if __name__ == '__main__':
    path = input('Enter path: ')

    data = {}
    for element in os.listdir(path):
        data[element] = folder_size(os.path.join(path, element))

    prettytable = PrettyTable(['Folder Name', 'Size'])
    prettytable.align['Folder Name'] = 'l'
    prettytable.align['Size'] = 'r'

    for key, value in sorted(data.items(), key=lambda item: item[1], reverse=True):
        prettytable.add_row([key, format_size(value)])

    print(prettytable)
    print(f'Total size: {format_size(sum(data.values()))}')