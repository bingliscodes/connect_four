#
# ps7pr5.py (Problem Set 7, Problem 5)
#
# TT Securities
#
#  Computer Science 111
#
from math import sqrt
def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    print('(3) Find the average price')
    print('(4) Find the standard deviation')
    print('(5) Find the max price and its day')
    print('(6) Test a threshold')
    print('(7) Your TT investment plan')
    print('(8) Quit')
    print()

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

## Part 1: revision of printing day and price
def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    for i in range(len(prices)):
        if i == 0:
            print('Day', 'Price')
            print('--- -----')
        day = i
        price = prices[i]
        print('%3.0f' % day, '%5.2f' % price)
            

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Part 2: support for options 3 - 5
# support for option 3
def average_price(prices):
    """ calculates the average of prices. """
    total = 0
    for i in prices:
        total += i
    num = len(prices)
    avg = total / num
    return avg

# support for option 4
def standard_dev(prices):
    """ calculates the standard deviation of prices. """
    avg = average_price(prices)
    x = 0
    for i in prices:
        x += (i - avg) ** 2
        print (x)
    x = x // len(prices)
    return sqrt(x)

# support for option 5
def max_price_and_day(prices):
    """ returns the max price and the day it occurs from a list of prices """
    #hold the first index and price in current_max to initalize
    max_day = 0
    max_price = prices[0]
    #now loop through, comparing each price and always hold the bigger one
    for i in range(len(prices)):
        if max_price < prices[i]:
            #print('comparing', max_price,'and', prices[i])
            max_day = i
            max_price = prices[i]
    lst = [max_day, max_price]
    return lst
        
## Part 3: support for option 6
# support for option 6
def test_a_threshold(prices):
    """ User inputs an integer and determines if there are any prices below that
        threshold. """
    #Take an integer from the user
    val = eval(input('Enter the threshold:'))
    for i in range(len(prices)):
        if prices[i] < val:
            print('There is at least one price under', val)
            break
        elif i == len(prices)-1 and prices[-1] > val:
            print('There are no prices under', val)
                

## Part 4: support for option 7
# support for option 7
def time_travel(prices):
    """ using the list prices, tells you which day to buy and sell to maximize profit.
        parameters: must buy before you sell """
    current_best = prices[1] - prices[0]
    best_buy_day = 0
    best_sell_day = 0
    best_buy = 0
    best_sell = 0
    check = 0
    profit = 0
    for i in range(len(prices)):
        for x in range(len(prices)):
            if i < x:
                check = prices[i]
                profit = prices[x] - prices[i]
                #print('comparing', prices[x], 'and', prices[i])
                if profit > current_best:
                    best_buy_day = i
                    best_sell_day = x
                    best_buy = prices[i]
                    best_sell = prices[x]
                    current_best = profit

    return [best_buy_day, best_sell_day, current_best, best_buy, best_sell]
        
    
def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        elif choice == 3:
            average = average_price(prices)
            print('The average price is', average)
        elif choice == 4:
            standard_deviation = standard_dev(prices)
            print('The standard deviation is', standard_deviation)
        elif choice == 5:
            max_price_list = max_price_and_day(prices)
            day = max_price_list[0]
            price = max_price_list[1]
            print('The max price is', price, 'on day', day)
        elif choice == 6:
            test_a_threshold(prices)
        elif choice == 7:
            best_results = time_travel(prices)
            day = best_results[0]
            day_sell = best_results[1]
            profit = best_results[2]
            price_buy = best_results[3]
            price_sell = best_results[4]
            print('Buy on day', day, 'at price', price_buy)
            print('Sell on day', day_sell, 'at price', price_sell)
            print('Total profit:', profit)
            

            
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')
