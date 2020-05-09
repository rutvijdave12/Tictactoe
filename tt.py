z = 'y'
while z == 'y' or z == 'Y':
    def my_board(pos):
        print(' '+pos[1]+'|'+' '+pos[2]+' '+'|'+pos[3]+' ')
        print('--|---|--')
        print(' '+pos[4]+'|'+' '+pos[5]+' '+'|'+pos[6]+' ')
        print('--|---|--')
        print(' '+pos[7]+'|'+' '+pos[8]+' '+'|'+pos[9]+' ')
        




    #my_board(['#','X','O','X','O','X','X','O','O'])


    def my_marker():
        marker = ''
        while marker !='X' and marker != 'O':
            marker = input("Player1,please choose a marker 'X' or 'O':")
            player1 = marker
            if player1 == 'X':
                player2 = 'O'
            else:
                player2 = 'X'

        return (player1,player2)

    player1 , player2 = my_marker()




    def my_placer(player1,player2):
        n = 0
        a = False
        pos = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        my_board(pos)
        while n<9:
            t = True
            if a == False:
                if n%2==0:
                    position = int(input("Player1,pick your position:"))
                    if pos[position] == ' ':
                        del pos[position]
                        pos.insert(position,player1)
                        my_board(pos)
                    else:
                        print("Position unavailable")
                        t = False
                        my_board(pos)
                
                else:
                    position = int(input("Player2,pick your position:"))
                    if pos[position] == ' ':
                        del pos[position]
                        pos.insert(position,player2)
                        my_board(pos)
                    else:
                        print("Position unavailable")
                        t = False  
                        my_board(pos)
                a = result(pos,player1,player2)
                if t == True:
                    n = n + 1
            else:
                break
        else:
            print("It's a Tie!")
        

    def result(pos,player1,player2):
        if player1 == 'X':
            if pos[1:4] == ['X']*3 or pos[4:7] == ['X']*3 or pos[7:10] == ['X']*3:
                print('Player1 has won')
                return True

            elif(pos[1:4] == ['O']*3) or (pos[4:7] == ['O']*3) or (pos[7:10] == ['O']*3):
                print('Player2 has won')
                return True

            else:
                pass
            
            if(pos[1] == pos[4] == pos[7] == 'X') or (pos[2] == pos[5] == pos[8] == 'X') or (pos[3] == pos[6] == pos[9] == 'X'):
                print('Player1 has won')
                return True

            elif(pos[1] == pos[4] == pos[7] == 'O') or (pos[2] == pos[5] == pos[8] == 'O') or (pos[3] == pos[6] == pos[9] == 'O'):
                print('Player2 has won')
                return True

            else:
                pass   
            
            if(pos[1] == pos[5] == pos[9] == 'X') or (pos[3] == pos[5] == pos[7] == 'X'):
                print('Player1 has won')
                return True
            
            elif(pos[1] == pos[5] == pos[9] == 'O') or (pos[3] == pos[5] == pos[7] == 'O'):
                print('Player2 has won')
                return True
            
            else:
                return False
        else:
            if(pos[1:4] == ['X']*3) or (pos[4:7] == ['X']*3) or (pos[7:10] == ['X']*3):
                print('Player2 has won')
                return True

            elif(pos[1:4] == ['O']*3) or (pos[4:7] == ['O']*3) or (pos[7:10] == ['O']*3):
                print('Player1 has won')
                return True

            else:
                pass



            if(pos[1] == pos[4] == pos[7] == 'X') or (pos[2] == pos[5] == pos[8] == 'X') or (pos[3] == pos[6] == pos[9] == 'X'):
                print('Player2 has won')
                return True

            elif(pos[1] == pos[4] == pos[7] == 'O') or (pos[2] == pos[5] == pos[8] == 'O') or (pos[3] == pos[6] == pos[9] == 'O'):
                print('Player1 has won')
                return True

            else:
                pass   
            
            if(pos[1] == pos[5] == pos[9] == 'X') or (pos[3] == pos[5] == pos[7] == 'X'):
                print('Player2 has won')
                return True
            
            elif(pos[1] == pos[5] == pos[9] == 'O') or (pos[3] == pos[5] == pos[7] == 'O'):
                print('Player1 has won')
                return True
            
            else:
                return False


    my_placer(player1,player2)
    z = input("Do you want to play again,Press Y if Yes,Press any key if No:")

                


