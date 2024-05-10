import os
import sys

class OutputHandler:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.create_output_directory()

    def create_output_directory(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def write_to_file(self, output_file, content):
        with open(output_file, 'w') as f:
            f.write(content)