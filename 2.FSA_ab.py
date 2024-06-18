
def create_automaton():
    """Creates the automaton's states and transitions."""
    return {
        "q0": {"a": "q1", "b": "q0"},
        "q1": {"a": "q0", "b": "q2"},
        "q2": {"a": "q0", "b": "q2"}  # Accept state for strings ending with 'ab'
    }, "q0", ["q2"]  # Pack states, start_state, accepting_states

def process_input(automaton, input_string):
    """Processes the input string through the automaton."""
    states, start_state, accepting_states = automaton
    current_state = start_state
    for char in input_string:
        if char not in states[current_state]:
            return "Invalid input character: {}".format(char)
        current_state = states[current_state][char]

    return "Accepted" if current_state in accepting_states else "Rejected"

def main():
    states, start_state, accepting_states = create_automaton()
    while True:
        input_string = input("Enter a string (or 'q' to quit): ")
        if input_string.lower() == 'q':
            break
        result = process_input(automaton=(states, start_state, accepting_states), input_string=input_string)
        print(result)

        # Add y/n option for another run
        run_again = input("Run again? (y/N): ")
        if run_again.lower() != 'y':
            break

if __name__ == "__main__":
    main()
