
def check_agreement(grammar, input_string):
    agreement_errors = []
    for rule in grammar['Agreement']:
        if rule[0] in input_string and rule[1] in input_string:
            agreement_errors.append((rule[0], rule[1]))
    return agreement_errors

def main():
    grammar = {
        'Agreement': [('NN', 'VBZ'), ('NNS', 'VBZ')],
    }
    input_string = input("Enter a sentence: ").strip().split()
    agreement_errors = check_agreement(grammar, input_string)
    if agreement_errors:
        print("Agreement errors found:")
        for error in agreement_errors:
            print(f"{error[0]} does not agree with {error[1]}")
    else:
        print("No agreement errors found.")

if __name__ == "__main__":
    main()
