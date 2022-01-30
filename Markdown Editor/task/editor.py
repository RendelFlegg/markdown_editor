formatters = ['plain', 'bold', 'italic', 'header', 'ordered-list', 'unordered-list', 'link', 'inline-code', 'new-line']
commands = ['!help', '!done']


def bold(text):
    return f'**{text}**'


def italic(text):
    return f'*{text}*'


def header(level, text):
    return f'{"#" * int(level)} {text}\n'


def link(label, url):
    return f'[{label}]({url})'


def inline_code(text):
    return f'`{text}`'


def formatted_list(number_of_rows, ordered=False):
    rows = []
    point = '*'
    for n in range(1, number_of_rows + 1):
        row = input(f'Row #{n}: ')
        if ordered:
            point = f'{n}.'
        rows.append(f'{point} {row}\n')
    return rows


def choose_formatter(formatter):
    if formatter == 'plain':
        text_list.append(input('Text: '))
    elif formatter == 'bold':
        text_list.append(bold(input('Text: ')))
    elif formatter == 'italic':
        text_list.append(italic(input('Text: ')))
    elif formatter == 'header':
        while True:
            try:
                header_level = int(input('Level: '))
                assert header_level in range(1, 7)
            except (ValueError, AssertionError):
                print('The level should be within the range of 1 to 6')
            else:
                text_list.append(header(header_level, input('Text: ')))
                break
    elif formatter == 'link':
        text_list.append(link(input('Label: '), input('URL: ')))
    elif formatter == 'inline-code':
        text_list.append(inline_code(input('Text: ')))
    elif formatter == 'new-line':
        text_list.append('\n')
    elif formatter in ['ordered-list', 'unordered-list']:
        while True:
            try:
                number_of_rows = int(input('Number of rows: '))
                assert number_of_rows > 0
            except (ValueError, AssertionError):
                print('The number of rows should be greater than zero')
            else:
                for row in formatted_list(number_of_rows, ordered=True if formatter == 'ordered-list' else False):
                    text_list.append(row)
                break


text_list = []
while True:
    answer = input('- Choose a formatter: ')
    if answer not in formatters + commands:
        print('Unknown formatting type or command.')
    elif answer in commands:
        if answer == '!help':
            print(f'Available formatters: {" ".join(formatters)}')
            print(f"Special commands: {' '.join(commands)}")
        elif answer == '!done':
            break
    else:
        choose_formatter(answer)
        print(''.join(text_list))
