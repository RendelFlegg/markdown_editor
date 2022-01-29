formatters = ['plain', 'bold', 'italic', 'header', 'ordered-list', 'unordered-list', 'link', 'inline-code', 'new-line']
commands = ['!help', '!done']

while True:
    answer = input('- Choose a formatter:')
    if answer not in formatters + commands:
        print('Unknown formatting type or command.')
    if answer == '!help':
        print(f'Available formatters: {" ".join(formatters)}')
        print(f"Special commands: {' '.join(commands)}")
    elif answer == '!done':
        break

# print("# John Lennon")
# print("or ***John Winston Ono Lennon*** was one of *The Beatles*.")
# print("Here are the songs he wrote I like the most:")
# print("* Imagine")
# print("* Norwegian Wood")
# print("* Come Together")
# print("* In My Life")
# print("* ~~Hey Jude~~ (that was *McCartney*)")
