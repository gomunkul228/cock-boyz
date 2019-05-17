import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

number_mine_spots = int(input())
for i in range(number_mine_spots):
    x, y = [int(j) for j in input().split()]




class boy:
    def __init__(self, unit_id, x, y, level):
        self.unit_id = unit_id
        self.x = x
        self.y = y
        self.level = level
    def get_pos(self):
        return([self.x,self.y])
    def unit_id(self):
        return(self.unit_id)


def tr(pair):
    return(str(pair[0])+" "+str(pair[1]))




# game loop
while True:
    boy_souls = []
    counter_souls = 0
    
    gold = int(input())
    income = int(input())
    opponent_gold = int(input())
    opponent_income = int(input())
    for i in range(12):
        line = input()
    building_count = int(input())
    for i in range(building_count):
        owner, building_type, x, y = [int(j) for j in input().split()]
        
        if owner == 1:
            enemy_capital = [x,y]
        else:
            my_capital = [x,y]
        
    unit_count = int(input())
    for i in range(unit_count):
        owner, unit_id, level, x, y = [int(j) for j in input().split()]
        
        if owner == 0:
            boy_souls.append(boy(unit_id, x, y, level))
            counter_souls += 1

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    res = ""
    
    if gold >= 10 and my_capital[0]+1 < 12 :
        res += "TRAIN 1 "+ str(my_capital[0]+1) + " " + str(my_capital[1]) + "; "
        gold -= 10
    if gold >= 10 and my_capital[0]-1 >= 0:
        res += "TRAIN 1 "+ str(my_capital[0]-1) + " " +str(my_capital[1]) + "; "
        gold -= 10
    if gold >= 10 and my_capital[1]+1 < 12:
        res += "TRAIN 1 "+ str(my_capital[0]) + " " +str(my_capital[1]+1) + "; "
        gold -= 10
    if gold >= 10 and my_capital[1]-1 >= 0:
        res += "TRAIN 1 "+ str(my_capital[0]) + " " +str(my_capital[1]-1) + "; "
        gold -= 10


    for soul in boy_souls:
        soldier = soul
        res += "MOVE "+ str(soldier.unit_id) + " "+tr(enemy_capital) + "; "
        
        
    res += "WAIT"
    print(res)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    