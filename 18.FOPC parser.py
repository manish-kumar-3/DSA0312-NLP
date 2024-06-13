import re

def parse_fopc(expression):
    # Regular expression to match predicates and variables
    pattern = r'([A-Za-z]+\([A-Za-z]+\))|([A-Za-z]+)'
    matches = re.findall(pattern, expression)

    predicates = set()
    variables = set()

    for match in matches:
        for group in match:
            if group:
                parts = group.split('(')
                if len(parts) > 1:
                    predicate = parts[0]
                    variable = parts[1][:-1]
                    predicates.add(predicate)
                    variables.add(variable)
                else:
                    variables.add(group)

    return predicates, variables

# Get input from user
user_input = input("Enter a logical expression: ")

# Parse the expression
predicates, variables = parse_fopc(user_input)

# Print the results
print("Predicates:", predicates)
print("Variables:", variables)
