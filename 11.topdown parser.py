
def parse(grammar, start_symbol, input_string):
    def expand(symbol):
        for production in grammar[symbol]:
            if all(part in input_string for part in production):
                return production
        return None

    stack = [start_symbol]
    while stack:
        symbol = stack.pop()
        if symbol in grammar:
            production = expand(symbol)
            if production is None:
                return False
            stack.extend(reversed(production))
        elif symbol != input_string.pop(0):
            return False
    return True if not input_string else False

def main():
    grammar = {
        'S': [['a', 'S', 'b'], ['']],
    }
    start_symbol = 'S'
    input_string = input("Enter a string: ").strip()
    result = parse(grammar, start_symbol, list(input_string))
    print("String can be derived from the grammar." if result else "String cannot be derived from the grammar.")

if __name__ == "__main__":
    main()
