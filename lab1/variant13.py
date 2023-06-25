import re

def main():

    with open('text3.txt', 'r', encoding='utf-8') as f:
        data = f.read()
        text = data[249:267]
        print("Text:" + text)
        print("Last 6 symbols: " + text[-6:])
        print("Length: " + str(len(text)))
        print("Count o's: " + str(text.count('o')))
        print("Index of o: " + str(text.find('o')))
        print("Index of Holmes: " + str(text.find('Holmes')))
        print("To upper: " + text.upper())
        print("To lower: " + text.lower())
        print("Text title: " + text.title())
        print("Text capitalize: " + text.capitalize())
        print("Join with _: " + '_'.join(text))
        print("Is digit: " + str(text.isdigit()))
        print("Start with I: " + str(text.startswith('I')))

        date1_pattern = r'(\d{2})\/(\d{2})\/(\d{4})'
        date2_pattern = r'(\d{4})\-(\d{2})\-(\d{2})'

        data = re.sub(date1_pattern, r'\2.\1.\3', data)
        data = re.sub(date2_pattern, r'\3.\2.\1', data)

        print(data)

if __name__ == '__main__':
    main()