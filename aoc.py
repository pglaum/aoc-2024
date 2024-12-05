def get_content(filename):
    with open(filename, 'r') as f:
        content = f.read()

    return content

def get_lines(filename):
    with open(filename, 'r') as f:
        content = f.readlines()

    return content


def get_columns(content, sep = ' ', to_int = True):
    columns = [[] for _ in range(len(content[0].split(sep)))]
    for line in content:
        splits = line.split(sep)
        for i, split in enumerate(splits):
            if to_int:
                columns[i].append(int(split))
            else:
                columns[i].append(split)

    return columns


def get_columns_from_file(filename, sep = ' ', to_int = True):
    content = get_lines(filename)
    return get_columns(content, sep, to_int)


def get_line_arrays(content, sep = ' ', to_int = True):
    lines = []
    for line in content:
        if to_int:
            lines.append([int(x) for x in line.split(sep)])
        else:
            lines.append(line.split(sep))

    return lines


def get_line_arrays_from_file(filename, sep = ' ', to_int = True):
    content = get_lines(filename)
    return get_line_arrays(content, sep, to_int)