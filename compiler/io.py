from sys import argv
from os import listdir

from .instructions import Instructions

class IO:

    examples_input : str
    examples_output : str
    examples_logs : str
    filenames : list
    isCommandLine : bool
    
    def __init__(self) -> None:
        
        self.examples_input = 'examples/input/'
        self.examples_output = 'examples/output/'
        self.examples_logs = 'examples/logs/'
        self.filenames : list = []
        self.isCommandLine = False

    def input(self) -> list:

        if len(argv) == 1:

            self.isCommandLine = False

            for path in listdir(self.examples_input):

                self.filenames.append(self.examples_input + path)

        elif len(argv) > 1:

            self.isCommandLine = True

            self.filenames = argv.copy()

            self.filenames.pop(0)

        self.filenames.sort()

        return self.filenames
    
    def output(self, filename : str, instructions : Instructions) -> None:

        file : list = []
        output_file : str = ''
        log_file : str = ''

        if self.isCommandLine == False:

            file = filename.split('/')
            filename = file.pop()
            file = filename.split('.')
            file.pop()
            filename = file.pop()

            output_file = self.examples_output + filename + '_out'
            log_file = self.examples_logs + filename + '_log'
                

        elif self.isCommandLine == True:

            file = filename.split('.')

            file.pop()

            filename = file.pop()

            output_file = filename + '_out'
            log_file = filename + '_log'

        

        with open(output_file, 'w') as open_file:

            open_file.write('Estado da Pilha: \n\n')
            
            for item in instructions.items:
                open_file.write('Exit Code: ' + str(item))

        with open(log_file, 'w') as open_file:

            open_file.write('Estado das Instruções: \n\n')
                
            open_file.write('PC: ' + str(instructions.pc) + '\n')
            open_file.write('FBR: ' + str(instructions.fbr) + '\n')
            open_file.write('SP:' + str(instructions.sp) + '\n')


    def print(self, filename : str, instructions : Instructions) -> None:

        print('------------------------------')

        print('\n')
        
        print('Arquivo: ' + filename)

        print('\n')

        print(instructions.items)

        print('\n')

        print('PC: ' + str(instructions.pc))
        print('FBR: ' + str(instructions.fbr))
        print('SP: ' + str(instructions.sp))

        print('\n')
