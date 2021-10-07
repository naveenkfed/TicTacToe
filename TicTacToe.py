import random

player_sym = {1:' ',2:' '}

def display_table(v_list):
    """ Displays the passed string in the formatted xo table

    """ 
    print ("\n")
    print ("\t\t\t\t\t\t| {} | {} | {} |".format(v_list[0],v_list[1],v_list[2]))
    print ("\t\t\t\t\t\t_____________\n")
    print ("\t\t\t\t\t\t| {} | {} | {} |".format(v_list[3],v_list[4],v_list[5]))
    print ("\t\t\t\t\t\t_____________\n")
    print ("\t\t\t\t\t\t| {} | {} | {} |".format(v_list[6],v_list[7],v_list[8]))
    print ("\t\t\t\t\t\t_____________")
    print ("\n")

def check_table(v_list,ch=''):
    """ Checks the table for any winning sequence of 'X's or 'O's

    """
    success = False
    for ind in [0,1,2]:
        if v_list[ind] == ch and v_list[ind+3] == ch and v_list[ind+6] == ch:
            success = True        
            break
            
    if success == False:
        for ind in [0,3,6]:
            if v_list[ind] == ch and v_list[ind+1] == ch and v_list[ind+2] == ch:
                success = True
                break
                
    if success == False:
        if (v_list[0] == ch and v_list[4] == ch and v_list[8] == ch) or (v_list[2] == ch and v_list[4] == ch and v_list[6] == ch):
            success = True
    return success    

def get_user_str(input_str,error_str,data_range):
    """ Utility function to retrieve string from player

    """    
    val_inp = False
    while val_inp == False:
        cch = input(input_str)
        if cch in data_range:
            val_inp = True
        else:
            print (error_str)
    return cch

def fetch_input():
    """ Randomly choose who goes first and request symbol preference X or O

    """
    sel_player = random.randint(1,2)
    non_sel_player = 2
    if sel_player == 2:
        non_sel_player = 1
        
    c_ch = get_user_str("PLAYER_{}: Select X or O:   ".format(sel_player), "Please enter either X or O", ['x','X','o','O'])
    player_sym[sel_player] = c_ch.upper()
    if c_ch.upper() == 'X':
        player_sym[non_sel_player] = 'O'
    else:
        player_sym[non_sel_player] = 'X'
    
    return sel_player,non_sel_player
            
def seek_position(player,entered_list):
    """ Fetch position in table from player to enter corresponding player's symbol

    """    
    val = False
    pos = -1
    while not val:
        pos = int(input("PLAYER_{}: Choose position in table to enter {}:   ".format(player,player_sym[player])))
        if pos in range(1,10):
            if pos not in entered_list:
                val = True
            else:
                print("ERROR...Position already taken")
        else:
            print ("ERROR...Enter number from 1 to 9")
                
    return pos
    
    
def make_move(player,entered_list,v_list):
    """ Logic to fetch position from player and update table and determine
    if player won or table is full

    """ 
    won, full = False, False
    entered_pos = seek_position(player,entered_list) 
    v_list[entered_pos-1] = player_sym[player]
    entered_list.append(entered_pos)
    display_table(v_list)
    if len(entered_list)>4 and check_table(v_list,player_sym[player]):
        print ("Player {} WON !!!!!".format(player))
        won = True
    elif len(entered_list) == 9:
        print ("MATCH DRAWN")
        full = True
    return won,full

def main():

    quit_game = False
    while not quit_game:
        first,second = fetch_input()
        xoxo_table = ['1','2','3','4','5','6','7','8','9']        
        print (player_sym)
        display_table(xoxo_table)
        
        anyone_won, table_full = False, False
        entries = []        
        while not (anyone_won or table_full):
            anyone_won,table_full= make_move(first,entries,xoxo_table)
            if not (anyone_won or table_full):
                anyone_won,table_full = make_move(second,entries,xoxo_table)
        else:
             game = get_user_str("Do you want to play another round? Enter Y or N:    ", "ERROR....Please enter Y or N", ['Y','y','N','n'])
             if game.upper() == 'N':
                quit_game = True
    else:
         print ("THANKS FOR PLAYING THE GAME!!!")
            
main()
