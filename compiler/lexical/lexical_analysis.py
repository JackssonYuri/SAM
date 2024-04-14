class Analysis:
    
    filename : str 
    tokens : list

    def __init__(self, filename : str):
        self.filename = filename
        self.tokens = []

    def tokenize(self):
        with open(self.filename, 'r') as file:
            self.tokens = []
            for line in file:
                line = line.strip()
                if line:
                    self.tokens.extend(line.split())

            return self.tokens
        

