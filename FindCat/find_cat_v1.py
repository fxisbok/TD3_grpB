import pathlib
import re

class FindCat:
    def __init__(self, s_path: str):
        self.s_path = f'{pathlib.Path.cwd()}/{s_path}'
        print(self.s_path)
        pass

    def search(self):
        s_list = pathlib.Path(self.s_path)
        s_list = list(s_list.glob('*.txt'))
        pattern = 'cat'

        for i in s_list:
            result = re.search(pattern, i.name)
            if (result == None):                    #state: failed to find
                print('Unfound')
                continue
            else:
                f_path = f'{self.s_path}/{i.name}'  #state: success to find
                with open(f_path,'r') as f_txt:
                    for i in f_txt.readlines():
                        print(i.rstrip('\n'))            # .strip() is function which delete '\n' at last



a = FindCat('a/b')
print(a.search())




'''
#Done
1. make class
2. make module search
    - need to extract file name only
3. print depend on if-state
    - how to print?
        1) contains on code
        2) contains on cat.txt >> choice!!
         - how to extract only file / file path ?''
'''

'''
#TO DO
2. make interpriter
 - type on terminal
 - type only 서울시/양천구/목동   >>>> Done!!!!
3. receive current python file's path
4. make life
 - while loop until life is 0
'''