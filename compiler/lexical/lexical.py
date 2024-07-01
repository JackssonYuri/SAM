from .lexical_analysis import Analysis

class Lexical:

    filename : str
    lexer : Analysis
    tokens : list

    def __init__(self, filename : str):

        self.filename = filename

        self.lexer = Analysis(filename)

        self.tokens = []
        
    
    def filetokens(self) -> list:

        self.tokens = self.lexer.tokenize()

        self.lexer.check_comments()
        self.lexer.check_labels()

        return self.tokens