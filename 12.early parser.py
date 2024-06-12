
def earley_parser(grammar, start_symbol, input_string):
    chart = [[] for _ in range(len(input_string) + 1)]
    chart[0].append(('S', (start_symbol,), 0))

    for i in range(len(input_string) + 1):
        for state in chart[i]:
            if state[2] < len(state[1]) and state[1][state[2]] in grammar:
                non_term = state[1][state[2]]
                for rule in grammar[non_term]:
                    new_state = (non_term, rule, 0)
                    if new_state not in chart[i]:
                        chart[i].append(new_state)

            elif state[2] < len(state[1]) and state[1][state[2]] == input_string[i - 1]:
                new_state = (state[0], state[1], state[2] + 1)
                if new_state not in chart[i]:
                    chart[i].append(new_state)

            elif state[2] == len(state[1]):
                for s in chart[state[3]]:
                    if s[2] < len(s[1]) and s[1][s[2]] == state[0]:
                        new_state = (s[0], s[1], s[2] + 1)
                        if new_state not in chart[i]:
                            chart[i].append(new_state)

    for state in chart[-1]:
        if state[0] == 'S' and state[2] == len(state[1]) and state[3] == 0:
            return True
    return False

def main():
    grammar = {
        'S': [('NP', 'VP')],
        'NP': [('Det', 'N'), ('NP', 'PP')],
        'VP': [('V', 'NP'), ('VP', 'PP')],
        'PP': [('P', 'NP')],
        'Det': ['the', 'a'],
        'N': ['man', 'dog', 'cat'],
        'V': ['chased', 'sat'],
        'P': ['on', 'in']
    }
    start_symbol = 'S'
    input_string = input("Enter a string: ").strip().split()
    result = earley_parser(grammar, start_symbol, input_string)
    print("String can be derived from the grammar." if result else "String cannot be derived from the grammar.")

if __name__ == "__main__":
    main()
