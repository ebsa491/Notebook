#!/usr/bin/python3
# Lesser General Public License (LGPL) v3.0 .
# The project has been developed by Saman Ebrahimnezhad .
# Created at Iran (IR) .
# Python 3 .

import sys
import os

class Notebook:

    def __init__(self):

        iconFile = open("/etc/Notebook/icon.txt", 'r')

        # Figlet used

        icon = iconFile.read()

        print(icon)

        if(len(sys.argv) > 1):

            self.filename = self.replacer(sys.argv[1])

        else:

            os.system("ls /etc/Notebook/notes/")

            self.filename = input("Enter the text name: ")

            self.filename = self.replacer(self.filename)

        self.text = input("Enter the text: ")

        os.system("echo \"" + self.replacer(self.text) + "\" > /etc/Notebook/notes/" + self.filename + ".txt")

    def replacer(self, string):
        return str(string).replace(" *:!@#$%^&|\'\";><?~.,", "")

def main():
    app = Notebook()

if __name__ == '__main__':
    main()
