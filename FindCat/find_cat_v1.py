import pathlib
import re
import time

class FindCat:
    def __init__(self):
        with open(f'{pathlib.Path.cwd()}/list.txt','r') as d_list:
            print([l.rstrip() for l in d_list])

        self.i_path = input('어디로 가시겠습니까? : ')
        self.s_path = f'{pathlib.Path.cwd()}/{self.i_path}'
        self.life = 3
        pass

    def search(self):
        s_list = pathlib.Path(self.s_path)
        s_list = list(s_list.glob('*.txt'))
        pattern = 'cat'

        for i in s_list:                        #s_list is file list in s_path
            f_path = f'{self.s_path}/{i.name}'  # print *.txt
            with open(f_path, 'r') as f_txt:
                for j in f_txt.readlines():
                    print(j.rstrip())
                    result = re.search(pattern,i.name)
            if (result==None):                            #state: failed to find
                self.life -= 1
                print('\n당신은 고양이를 찾지 못했습니다...\n남은 목숨 :', '\u2665'*self.life)
            else:
                print('\n축하합니다! 당신은 고양이를 찾았습니다!\n당신은',(3-self.life)+1,'번 만에 성공했군요!')

                score_path = f'{pathlib.Path.cwd()}/score_board.txt'
                with open(score_path,'a') as r_list:
                    usr_name = input('\n당신의 이름은? : ')
                    r_list.write(f'\n{usr_name} = {self.life}')

                with open(score_path,'r') as scoreboard:
                    sb_lst = scoreboard.readlines()

                    #clamping delay
                    delay = 10/len(sb_lst)
                    if (delay>0.5): delay = 0.5
                    elif (delay<0.25): delay = 0.25

                    #print
                    for k in sb_lst:
                        print(k.rstrip())
                        time.sleep(delay)


a = FindCat()
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