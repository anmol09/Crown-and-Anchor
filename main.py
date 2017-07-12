def betting(player_winnings): 
  
  player_bets = []
    
  for i in range( len(player_winnings) ) : 
    
    player_round = [0,0,0,0,0,0]
    
    skip = input("Player" + str(i) + ", do you want to place bets this round? (y/n)")
    
    if(skip == 'y'): #if player doesn't skip
    
      for c in [1,2,5,10]:
        
        prompt = int(input("How many " + str(c) + "$ chips do you want to bet on hearts: "))
        player_round[0] = player_round[0] + (c*prompt)
        
        prompt = int(input("How many " + str(c) + "$ chips do you want to bet on spades: "))
        player_round[1] = player_round[1] + (c*prompt)
        
        prompt = int(input("How many " + str(c) + "$ chips do you want to bet on diamonds: "))
        player_round[2] = player_round[2] + (c*prompt)
          
        prompt = int(input("How many " + str(c) + "$ chips do you want to bet on clubs: "))
        player_round[3] = player_round[3] + (c*prompt)
          
        prompt = int(input("How many " + str(c) + "$ chips do you want to bet on crown: "))
        player_round[4] = player_round[4] + (c*prompt)
          
        prompt = int(input("How many " + str(c) + "$ chips do you want to bet on anchor: "))
        player_round[5] = player_round[5] + (c*prompt)
          
        print("\n")
          
    else: #player has skipped
      player_round = [0,0,0,0,0,0]
    
    
  print(player_round)
    

def main():

  player_num = int(input("# of players: ")) #prompts user for number of players
  
  print("\nEach player intially starts with $10\nLet the game begin!\n")
  

  '''
  a) ask for bets -- symbol and amount bet (or skip this round)
  b) show the winning "slot"
  c) indicate how much was won by each player
  d) indicate how much money each player currently has
  Repeat the above steps while at least one player has money left.
  '''
  
  #	options = { 1 : 'heart', 2 : 'spade' , 3 : 'diamond' , 4: 'club' , 5: 'crown', 6 : 'anchor' }
  
  player_winnings = [] #keeps track of winnings
  
  for i in range(player_num): #starts everyone with 10$
    player_winnings.append(10)
    
  print(player_winnings)
  
  betting(player_winnings)
  
  

  
  
  
main()
  
