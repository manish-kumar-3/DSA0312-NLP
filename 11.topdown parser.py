import re

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def parse(self):
        return self.E() and self.position == len(self.tokens)

    def E(self):
        if self.T():
            while self.peek() == '+':
                self.consume()
                if not self.T():
                    return False
            return True
        return False

    def T(self):
        if self.F():
            while self.peek() == '*':
                self.consume()
                if not self.F():
                    return False
            return True
        return False

    def F(self):
        if self.peek() == 'id':
            self.consume()
            return True
        elif self.peek() == '(':
            self.consume()
            if self.E() and self.peek() == ')':
                self.consume()
                return True
        return False

    def peek(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return None

    def consume(self):
        self.position += 1

def lexer(input_string):
    token_specification = [
        ('id',    r'[a-zA-Z_][a-zA-Z_0-9]*'),  
        ('PLUS',  r'\+'),                   
        ('MULT',  r'\*'),                    
        ('LPAREN',r'\('),                    
        ('RPAREN',r'\)'),                     
        ('SKIP',  r'[ \t]+'),               
        ('MISMATCH', r'.'),                
    ]
    token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    tokens = []
    for mo in re.finditer(token_regex, input_string):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'id':
            tokens.append('id')
        elif kind == 'PLUS':
            tokens.append('+')
        elif kind == 'MULT':
            tokens.append('*')
        elif kind == 'LPAREN':
            tokens.append('(')
        elif kind == 'RPAREN':
            tokens.append(')')
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character {value}')
    return tokens

def main():
    input_string = input("Enter an arithmetic expression: ")
    tokens = lexer(input_string)
    print("Tokens:", tokens)
    parser = Parser(tokens)
    if parser.parse():
        print("The input string is syntactically correct.")
    else:
        print("The input string is syntactically incorrect.")

if __name__ == "__main__":
    main()
