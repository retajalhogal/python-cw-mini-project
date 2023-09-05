# write your code here
def padel_court_cost(court_type):
    if court_type == "indoor":
        return 30 
    elif court_type == "out door":
        return 20
    
def reckets_cost (racket_brand):
    if racket_brand == "bullpadel":
        return 120
    elif racket_brand == "nox":
        return 140 
    elif racket_brand == " siux":
        return 200
    

def padel_balls_cost(ball_boxas):
    if ball_boxas == (1):
        return 2
    elif ball_boxas == (2):
        return 3.5
    elif ball_boxas == (3):
        return 5
    
def padel_game_cost():
    courts_type=input("enter the court type")
    rackets_brand=input("enter the recket brand")
    balls_boxes=int(input("enter the number of the boxes"))
    total= padel_court_cost(courts_type) + reckets_cost(rackets_brand) + padel_court_cost(balls_boxes)
    return total 
print(padel_game_cost)