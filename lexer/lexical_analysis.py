class Lexer:
    filename : str 

    def __init__(self, filename : str):
        self.filename = filename

    def tokenize(self):
        with open(self.filename, 'r') as file:
            tokens = []
            for line in file:
                line = line.strip()
                if line:
                    tokens.extend(line.split())

            return tokens
        

