class StateMachine:
    def __init__(self):
        self.current_state = 'start'

    def transition(self, input_char):
        if self.current_state == 'start':
            if input_char == 'a':
                self.current_state = 'a_seen'
            else:
                self.current_state = 'start'
        elif self.current_state == 'a_seen':
            if input_char == 'b':
                self.current_state = 'ab_seen'
            elif input_char == 'a':
                self.current_state = 'a_seen'
            else:
                self.current_state = 'start'
        elif self.current_state == 'ab_seen':
            if input_char == 'a':
                self.current_state = 'a_seen'
            else:
                self.current_state = 'start'

    def is_accepted(self):
        return self.current_state == 'ab_seen'


def match_string(input_string):
    fsm = StateMachine()
    for char in input_string:
        fsm.transition(char)
    return fsm.is_accepted()


def main():
    input_string = input("Enter a string: ")
    print(f"String: {input_string}, Accepted: {match_string(input_string)}")


if __name__ == "__main__":
    main()
