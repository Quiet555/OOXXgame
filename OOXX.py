board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
table=f'{board[0]:^3}|{board[1]:^3}|{board[2]:^3}\n---|---|---\n{board[3]:^3}|{board[4]:^3}|{board[5]:^3}\n---|---|---\n{board[6]:^3}|{board[7]:^3}|{board[8]:^3}'
flag=1
sign='X'
print(table)
print(f'現在是{sign}的回合')

def setsign(x,sign):
    if board[x]==' ':
        board[x]=sign
        table=f'{board[0]:^3}|{board[1]:^3}|{board[2]:^3}\n---|---|---\n{board[3]:^3}|{board[4]:^3}|{board[5]:^3}\n---|---|---\n{board[6]:^3}|{board[7]:^3}|{board[8]:^3}'
        print(table)
        print()
    else:
        print(f'此位置已存在{sign}')
        return 0
    
def checkwin():                 #[0,1,2][3,4,5][6,7,8]，[0,3,6][1,4,7][2,5,8]，[0,4,8][2,4,6]
    if board[0]==board[1]==board[2]=='O' or board[3]==board[4]==board[5]=='O' or board[6]==board[7]==board[8]=='O':
        print('O獲勝')
        return -1
    elif board[0]==board[3]==board[6]=='O' or board[1]==board[4]==board[7]=='O' or board[2]==board[5]==board[8]=='O':
        print('O獲勝')
        return -1
    elif board[0]==board[4]==board[8]=='O' or board[2]==board[4]==board[6]=='O':
        print('O獲勝')
        return -1
    elif board[0]==board[1]==board[2]=='X' or board[3]==board[4]==board[5]=='X' or board[6]==board[7]==board[8]=='X':
        print('X獲勝')
        return -1
    elif board[0]==board[3]==board[6]=='X' or board[1]==board[4]==board[7]=='X' or board[2]==board[5]==board[8]=='X':
        print('X獲勝')
        return -1
    elif board[0]==board[4]==board[8]=='X' or board[2]==board[4]==board[6]=='X':
        print('X獲勝')
        return -1
    else :
        return 1

def switchside():
    if sign=='X':
        return 'O'
    elif sign=='O':
        return 'X'
        
while flag!=-1:
    place= int(input('選擇放置位置:'))
    if place==-1:
        flag=-1
    noset=setsign(place,sign)
    if noset==0:
        continue
    flag=checkwin()
    if flag==-1:
        break
    sign=switchside()
    print(f'輪到{sign}的回合')