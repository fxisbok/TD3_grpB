import pathlib
import re
import time

class FindCat:
    def __init__(self,life: int):
        self.life = life
        self.score_path = f'{pathlib.Path.cwd()}/score_board.txt'
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

    def writescore(self,usr_name: str) -> None:
        with open(self.score_path,'a') as r_list:
            score = f'{usr_name[0:7]:<8} |  {self.life+1}  |  {time.asctime()}\n'
            r_list.write(score)

    def sortscore(self) -> None:
        with open(self.score_path,'r') as s_list:
            sr_list = s_list.readlines()
            sortedcontainers = sorted(sr_list[1:], key=lambda x: x.split('|',2)[1],reverse=True)
            sortedcontainers.insert(0,sr_list[0])
        with open(self.score_path,'w') as sw_list:
            sw_list.write(''.join(sortedcontainers))


    def printscore(self) -> None:
        with open(self.score_path,'r') as scoreboard:
            sb_lst = scoreboard.readlines()

            delay = 10/len(sb_lst)
            if (delay>0.25): delay = 0.25
            elif (delay<0.1): delay = 0.1

            for k in sb_lst:
                print(k.rstrip())
                time.sleep(delay)
'''
#TODO
    def remove_overlap(self,pattern: str) -> str:
        with open(self.score_path,'r') as f:
            for i in f.readlines():
                result = re.search(pattern, i)
        return result
'''


#--------------------------------------------------------------------------------


catgame = FindCat(2)
while True:
    if (catgame.life < 0):
        print('\n당신은 고양이를 찾는 것에 실패 했습니다...')
        with open(f'{pathlib.Path.cwd()}/failed.txt','r') as fail_list:
            print(' '.join(fail_list.readlines()))
        break

    with open(f'{pathlib.Path.cwd()}/list.txt','r') as d_list:
        print(''.join(d_list.readlines()))

    path = input('어디로 가시겠습니까? : ')
    path = path.replace(' ','/')
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

    catgame.writescore(input('당신의 이름은? : '))
    catgame.sortscore()
    catgame.printscore()
    break


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
6. make life
 - while loop until life is 0
7. sort *.txt file as score (if it is possible..)
8. Add current time on scoreboard
'''


'''
#TO DO
1. DO NOT overlapping same value on scoreboard
    - sunny will do it!
'''


'''
#Question
1. split class n function file in real workflow?
2. how to make not-forcing parameter?
3. how to sort korean or other non-english language?
'''
