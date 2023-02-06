import argparse
import os
import sys

from compressor.engine import Engine


class ParseArguments:
    def __init__(self):  # config argument parser for this library
        self.parser = argparse.ArgumentParser(description="Arguments:",
                                              formatter_class=argparse.ArgumentDefaultsHelpFormatter)

        self._set_arguments()
        self._extract_data_from_args()
        self._check_argument_viability()

    def _set_arguments(self):  # create the parser
        self.parser.add_argument("-f", "--file", action="store_true",
                                 help="Converts only one file to exe.",
                                 default=False)
        self.parser.add_argument("-d", "--directory", action="store_true",
                                 help="Compresses entire code directory to exe.",
                                 default=False)
        self.parser.add_argument("-c", "--console", action="store_true",
                                 help="Generated executable is windowed.",
                                 default=False)
        self.parser.add_argument("-w", "--windowed", action="store_true",
                                 help="Generated executable is GUI.",
                                 default=False)
        self.parser.add_argument("-o", "--output_dir", action="store_true",
                                 help="Sets directory where executable will be generated.",
                                 default=False)

    def _extract_data_from_args(self):  # retrieve user arguments
        self.args = self.parser.parse_args()
        self.config = vars(self.args)

        self.file = str(self.config).split(', ')[0]
        self.workspace = str(self.config).split(', ')[1]

    def _check_argument_viability(self):  # check is arguments are correct
        if 'False' in self.file and 'False' in self.workspace:
            print('Error: Cannot run py-exe exe generator without any arguments.')
            sys.exit(-1)

        if 'True' in self.file and 'True' in self.workspace:
            print('Error: Conflicting arguments, option --file and --directory is selected which is not allowed.')
            sys.exit(-1)

        if 'True' in self.file:
            self._desired_file = input('Enter you desired file location: ')
            self._run_code_exe_gen_compressor('file', self._desired_file)

        if 'True' in self.workspace:
            self._desired_file = input('Enter you desired directory location: ')
            self._run_code_exe_gen_compressor('directory', self._desired_file)

    @staticmethod
    def _run_code_exe_gen_compressor(file_type, file):  # start py-exe exe generator
        if file_type == 'file':
            if not os.path.isfile(file):  # error if argument is not a file
                print('Error: Selected item must be a file.')
                sys.exit(-1)

            if not os.path.splitext(file)[1] == '.py':  # error if file is not python script
                print('Error: Cannot compress non python file.')
                sys.exit(-1)

            Engine().run_py_exe('file', file)
        elif file_type == 'directory':
            if not os.path.isdir(file):  # error if argument is not a directory
                print('Error: Selected item must be a directory.')
                sys.exit(-1)

            Engine().run_py_exe('directory', file)


if __name__ == '__main__':
    ParseArguments()
