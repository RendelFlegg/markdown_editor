formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line']
commands = ['!help', '!done']


def plain():
    pass


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


# def new_line(text):
#     return f'{text}\n'


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
