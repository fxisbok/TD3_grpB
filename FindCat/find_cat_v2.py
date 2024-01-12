import pathlib
import re
import time

class FindCat:
    def __init__(self,life: int):
        with open(f'{pathlib.Path.cwd()}/list.txt','r') as d_list:
            print([l.rstrip() for l in d_list])
        self.life = life
    def get_path(self, i_path: str) -> str:
        s_path = f'{pathlib.Path.cwd()}/{i_path}'
        return s_path
    def search(self,s_path: str,pattern: str) -> list:
        s_list = pathlib.Path(s_path)
        s_list = list(s_list.glob('*.txt'))

        for i in s_list:                                #s_list is file list in s_path
            result = [re.search(pattern,i.name), str(i.name)]
            return result
        #return result

    def print_file(self,s_path: str,f_name: str):
        f_path = f'{s_path}/{f_name}'
        with open(f_path,'r') as f_txt:
            for j in f_txt.readlines():
                print(j.rstrip())

    def scoreboard(self):
        score_path = f'{pathlib.Path.cwd()}/score_board.txt'
        with open(score_path,'a') as r_list:
            usr_name = input('\n당신의 이름은? : ')
            r_list.write(f'\n{usr_name} = {self.life}')

        with open(score_path,'r') as scoreboard:
            sb_lst = scoreboard.readlines()

            delay = 10/len(sb_lst)
            if (delay>0.25): delay = 0.25
            elif (delay<0.1): delay = 0.1

            for k in sb_lst:
                print(k.rstrip())
                time.sleep(delay)



catgame = FindCat(2)
while True:
    path = input('경로를 입력하여 주세요 : ')
    if (catgame.life==0):
        print('당신은 고양이를 찾는 것에 실패 했습니다...')
        break
    result = catgame.search(path,'cat')
    try:
        catgame.print_file(path,result[1])
    except TypeError:
        print('\n당신은 고양이를 찾지 못했습니다...' '\n남은 목숨 : ',('\u2665' * catgame.life))
        catgame.life -= 1
        continue
    if (result[0]==None):
        print('\n당신은 고양이를 찾지 못했습니다...' '\n남은 목숨 : ', ('\u2665' * catgame.life),'\n')
        catgame.life -= 1
        continue
    catgame.scoreboard()
    break


#print(result)
#catgame.print_file(result[1])
#vaild = result[0]
#if (vaild==None):
#    print('Failed')

#f_print = a.print_file(search[1])
#a.statement(search[0])
#a.scoreboard()



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
4. make interpriter
 - type on terminal
 - type only 서울시/양천구/목동
5. receive current python file's path
'''

'''
#TO DO
1. make life
 - while loop until life is 0
'''