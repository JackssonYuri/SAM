from lexical.lexical_analysis import Analysis

class Lexical:

    filename : str
    lexer : Analysis
    filetokens : list = []

    def __init__(self, filename : str):

        self.filename = filename

        self.lexer = Analysis(filename)
        
    
    def filetokens(self) -> list:

        tokens : list = self.lexer.tokenize()

        self.filetokens.append(tokens)

        return self.filetokens