# функция вывода игрового поля
def show_fild(f):
      print('  0 1 2')
      for i in range(len(field)):
            print(str(i)+' '+' '.join(field[i]))

# функция хода
def user_input(f):
      while True:
            place=input('Введите координаты: ').split()
            if len(place)!=2:
                  print('Введите две координаты!')
                  continue
            if not (place[0].isdigit() and place[1].isdigit()):
                  print('Введите числа!')
                  continue
            x,y=map(int, place)
            if not (x>=0 and x<3 and y>=0 and y<3):
                  print('Вы вышли за поле игры! Введите координаты от 0 до 2.')
                  continue
            if f[x][y]!='-':
                  print('Клетка занята! Выберите другую.')
                  continue
            break
      return x,y

# функция проверки выйгрыша
def winer (f,user):
      def check_line(a1, a2, a3, user):
            if (a1==user and a2==user and a3==user):
                  return True
      for n in range(3):
            if check_line(f[n][0], f[n][1], f[n][2], user) or \
                    check_line(f[0][n], f[1][n], f[2][n], user) or \
                    check_line(f[0][0], f[1][1], f[2][2], user) or \
                    check_line(f[2][0], f[1][1], f[0][2], user):
               return True
      return False

# основная часть программы
field=[['-']*3 for _ in range(3)]
count=0
while True:
      if count%2==0:
            user='X'
      else:
            user='O'
      show_fild(field)
      x,y=user_input(field)
      field[x][y]=user
      if count==8:
            print('Ничья!')
            show_fild(field)
            input()
            break
      if winer(field,user):
            print(f"Выйграл {user} !")
            show_fild(field)
            input()
            break
      count+=1
