def is_broke(initial,spent):
  total = (initial - spent)
  
  if total<0:
    return True #player is broke
    
  else:
    return False #player still has money
  
  
def betting(player_budget): 
  
  player_bets = []
    
  for i in range( len(player_budget) ) : 
    
    player_round = [0,0,0,0,0,0]
    
    skip = input("Player" + str(i) + ", do you want to place bets this round? (y/n)")
    
    if(skip == 'y'): #if player doesn't skip
    
      for c in [1,2,5,10]:
        
        bet = [0,0,0,0,0,0]
        
        broke = True #must be true to run first time, will get corrected at end of while
        
        while broke == True: #repeats 
          
          prompt = int(input("How many " + str(c) + "$ chips do you want to bet on hearts: "))
          bet[0] = (c*prompt)
          
          prompt = int(input("How many " + str(c) + "$ chips do you want to bet on spades: "))
          bet[1] = (c*prompt)
          
          prompt = int(input("How many " + str(c) + "$ chips do you want to bet on diamonds: "))
          bet[2] = (c*prompt)
            
          prompt = int(input("How many " + str(c) + "$ chips do you want to bet on clubs: "))
          bet[3] = (c*prompt)
            
          prompt = int(input("How many " + str(c) + "$ chips do you want to bet on crown: "))
          bet[4] = (c*prompt)
            
          prompt = int(input("How many " + str(c) + "$ chips do you want to bet on anchor: "))
          bet[5] = (c*prompt)
            
          print("\n")
          
          total_bet=0
          for t in range(6):
            total_bet = total_bet + bet[t] 
          
          broke = is_broke(player_budget[i],total_bet)
          
          if broke == True:
            print("You don't have enough money to make these bets, try again!\n")
            bet = [0,0,0,0,0,0] #all bets will be 0 
            print("Current budget = " + str(player_budget[i]) + "\n")
            
          else: #places bets if player is not broke
          
            player_round[0] = player_round[0] + bet[0]
            player_round[1] = player_round[1] + bet[1]
            player_round[2] = player_round[2] + bet[2]
            player_round[3] = player_round[3] + bet[3]
            player_round[4] = player_round[4] + bet[4]
            player_round[5] = player_round[5] + bet[5]
            
            player_budget[i] =  ( player_budget[i] - total_bet )
            
            print("Current budget = " + str(player_budget[i]) + "\n")

          
          
    else: #player has skipped
      player_round = [0,0,0,0,0,0] #all bets will be 0 
    
    
    print(player_round)
    player_bets.append(player_round) #creates a list of lists with all bets
    
  print(player_bets)
  return player_bets
  
  
  
    

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
  
  player_budget = [] #keeps track of winnings
  
  for i in range(player_num): #starts everyone with 10$
    player_budget.append(10)
    
  betting(player_budget) #starts betting prompts and logic
  
  

  
  
  
main()
  
