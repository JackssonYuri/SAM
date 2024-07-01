class Analysis:
    
    filename : str 
    tokens : list

    def __init__(self, filename : str):
        self.filename = filename
        self.tokens = []

    def tokenize(self):
        with open(self.filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    self.tokens.append(line.split())

            return self.tokens


    def check_comments(self):

        start_comment : int

        start_comment = -1

        for linetokens in self.tokens:

            for i,token in enumerate(linetokens):

                if token[0:2] == '//':

                    start_comment = i
                    

                if start_comment != -1:

                    linecomment = linetokens[start_comment:len(linetokens)]

                    for _ in linecomment:
                        linetokens.pop(start_comment)

                    start_comment = -1

        
        while [] in self.tokens:

            self.tokens.remove([])


    def check_labels(self):

        command : list = []
        function : list = []
        symbol_index : int = 0
        new_command : bool

        new_command = False

        for i,linetokens in enumerate(self.tokens):

            for token in linetokens:

                symbol_index = token.find(':')

                if symbol_index == -1:
                    continue

                if symbol_index == (len(token) - 1) and len(linetokens) > 1:

                    command = linetokens[1:len(linetokens)]

                    for _ in command:
                        linetokens.pop(1)


                    if not new_command:
                        self.tokens.insert(i+1, command)
                        new_command = True

                if symbol_index < (len(token) - 1) and len(linetokens) > 1:

                    function = token.split(':')

                    function[0] = function[0] + ':'

                    linetokens.pop(0)

                    if not new_command:

                        linetokens.insert(0, function.pop())
                        linetokens.insert(0, function.pop())

                        new_command = True

                    new_command = False

                    command = linetokens[1:len(linetokens)]

                    for _ in command:
                        linetokens.pop(1)


                    if not new_command:
                        self.tokens.insert(i+1, command)
                        new_command = True

            command = []
            new_command = False
