def earley_parser(grammar, start_symbol, input_string):
    chart = [[] for _ in range(len(input_string) + 1)]
    start_state = (start_symbol, (start_symbol,), 0, 0)
    chart[0].append(start_state)

    for i in range(len(input_string) + 1):
        for state in chart[i]:
            lhs, rhs, dot, origin = state
            if dot < len(rhs):
                next_symbol = rhs[dot]
                if next_symbol in grammar:
                    # Predictor
                    for rule in grammar[next_symbol]:
                        new_state = (next_symbol, rule, 0, i)
                        if new_state not in chart[i]:
                            chart[i].append(new_state)
                elif i < len(input_string) and next_symbol == input_string[i]:
                    # Scanner
                    new_state = (lhs, rhs, dot + 1, origin)
                    if new_state not in chart[i + 1]:
                        chart[i + 1].append(new_state)
            else:
                # Completer
                for s in chart[origin]:
                    s_lhs, s_rhs, s_dot, s_origin = s
                    if s_dot < len(s_rhs) and s_rhs[s_dot] == lhs:
                        new_state = (s_lhs, s_rhs, s_dot + 1, s_origin)
                        if new_state not in chart[i]:
                            chart[i].append(new_state)

    for state in chart[-1]:
        lhs, rhs, dot, origin = state
        if lhs == start_symbol and dot == len(rhs) and origin == 0:
            return True
    return False

def main():
    grammar = {
        'S': [('NP', 'VP')],
        'NP': [('Det', 'N'), ('NP', 'PP')],
        'VP': [('V', 'NP'), ('VP', 'PP')],
        'PP': [('P', 'NP')],
        'Det': [('the',), ('a',)],
        'N': [('man',), ('dog',), ('cat',)],
        'V': [('chased',), ('sat',)],
        'P': [('on',), ('in',)]
    }
    start_symbol = 'S'
    input_string = input("Enter a string: ").strip().split()
    result = earley_parser(grammar, start_symbol, input_string)
    print("String can be derived from the grammar." if result else "String cannot be derived from the grammar.")

if __name__ == "__main__":
    main()
