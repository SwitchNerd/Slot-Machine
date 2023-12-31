# Prompt: Text based slot machine
# User will deposit a certain amount of money
# Bet on either one two or three lines of the slot machine
# Determine if they won (multiply by lines)
# Keep playing till cash out or run out of money
import random
import sys, time

m_lines = 3
m_rows = [1,2,3,4]

def main():
    account_balance = 3000
    
    while True:
        
        if input("Would you like to see current balance? ") == 'y':
            print(f'${account_balance}')
        
        if account_balance == 0:
            break
        
        bettings = bet(account_balance)
        account_balance = account_balance - bettings
        
        lines = no_lines()
        
        print('')

        sys.stdout.write('Loading')
        
        for _ in range (3):
            time.sleep(0.5)
            sys.stdout.write('.')
            sys.stdout.flush()
        
        print('')
        print('')
        
        winnings = has_won(lines,bettings)
        print(f'You have won {winnings}!')
        
    
        
def bet(a_b): 
    while True:
        bet_amount = input("Enter amount you would like to bet($): ")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if bet_amount < 0:
                print("Bet has to be above $0. ")
            elif bet_amount > a_b:
                print("Invalid funds. ")
            else:
                break
        else:
            print("Please enter a number. ")
            
    return bet_amount

    
def no_lines():
    while True:
        lines = input(f"How many lines would you like to bet on (1-{m_lines})? ")
        if lines.isdigit():
            lines = int(lines)
            if lines >= 1 and lines <= m_lines:
                break
            else:
                print("Enter a number between the range")
        else:
            print("Please enter a number. ")
            
    return lines

def has_won(line, bets):
    i = 0
    for _ in range (line):
        if random.choice(m_rows) != 1:
            i = 1
    if i == 0:
        return bets * line
    else: 
        return 0

main()