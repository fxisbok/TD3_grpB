import sys
import pathlib
import re


class FindCat:
    def __init__(self, s_path: str):
        self.s_path = s_path
        pass

    def search(self):
        s_list = pathlib.Path(self.s_path)
        s_list = list(s_list.glob('*.txt'))
        pattern = 'cat'

        for i in s_list:
            re.search(pattern, i.name)
            #cat is searched file

        return s_list


'''
#Done

1. make class
2. make module search
    - need to extract file name only
'''

'''
#TO DO

1. print depend on if-state
    - how to print?
        1) contains on code
        2) contains on cat.txt >> choice!!
         - how to extract only file / file path ?
2. make interpriter - type on terminal
'''


test = FindCat('/home/rapa')
print(test.search())