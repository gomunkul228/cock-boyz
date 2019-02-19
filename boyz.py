import sys
import math

# Grab Snaffles and try to throw them through the opponent's goal!
# Move towards a Snaffle and use your team id to determine where you need to throw it.

my_team_id = int(input())  # if 0 you need to score on the right of the map, if 1 you need to score on the left
if my_team_id == 1:
    goal = [0,3750]
    sign = -1
else:
    goal = [16000,3750]
    sign = 1

def dist(pos1,pos2):
    return(math.sqrt((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2))   
    
    
    
class ball:
    def __init__(self, entity_id, x, y, vx, vy, state):
        self.entity_id = entity_id
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.state = state        


class my_boy:
    def __init__(self, entity_id, x, y, vx, vy, state):
        self.entity_id = entity_id
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.state = state
    def get_pos(self):
        return([self.x,self.y])
    def nearest_ball(self):
        list_of_dist = list(map(lambda x: dist(x,[self.x,self.y]), pos_balls))
        return pos_balls[list_of_dist.index(min(list_of_dist))]
    def list_of_dict(self):
        return list(map(lambda x: dist(x,[self.x,self.y]), pos_balls))


def check_accio(pos):
    return sign*(boy1.get_pos()[0] - pos[0]) > 0 and sign*(boy2.get_pos()[0] - pos[0]) > 0

#нужно добавить магию
# game loop
while True:
    pos_balls = []
    dict_balls = {}
    curse_balls = []
    ko=3
    
    my_score, my_magic = [int(i) for i in input().split()]
    opponent_score, opponent_magic = [int(i) for i in input().split()]
    entities = int(input())  # number of entities still in game
    for i in range(entities):
        # entity_id: entity identifier
        # entity_type: "WIZARD", "OPPONENT_WIZARD" or "SNAFFLE" (or "BLUDGER" after first league)
        # x: position
        # y: position
        # vx: velocity
        # vy: velocity
        # state: 1 if the wizard is holding a Snaffle, 0 otherwise
        entity_id, entity_type, x, y, vx, vy, state = input().split()
        entity_id = int(entity_id)
        x = int(x)
        y = int(y)
        vx = int(vx)
        vy = int(vy)
        state = int(state)
        
        if entity_type == "WIZARD":
            if ko == 3:
                boy1 = my_boy(entity_id, x, y, vx, vy, state)
                ko = 4
            else:
                boy2 = my_boy(entity_id, x, y, vx, vy, state)
            
        
        if entity_type == "SNAFFLE" and state == 0:
            pos_balls += [[x,y]]
            dict_balls[str([x,y])] = entity_id
        elif entity_type == "SNAFFLE":
            curse_balls += [[x,y]]
            
            
    boys = [boy1.entity_id,boy2.entity_id]
    
    
    
    dict = {}
    for i in range(0,len(pos_balls)):
        for j in range(0,len(pos_balls)):
            if i != j:
                dict[boy1.list_of_dict()[i] + boy2.list_of_dict()[j]] = [i,j]
    if dict != {}:
        move_boy1 = pos_balls[dict[min(dict)][0]]
        move_boy2 = pos_balls[dict[min(dict)][1]]
    elif pos_balls != []:
        move_boy1 = boy1.nearest_ball()
        move_boy2 = boy2.nearest_ball()
    else:
        move_boy1 = curse_balls[0]
        move_boy2 = curse_balls[0]
    
#    if boy1.nearest_ball() == boy2.nearest_ball():
#        if dist(boy1.get_pos(),boy1.nearest_ball()) <= dist(boy2.get_pos(),boy2.nearest_ball()):
#            move_boy1 = boy1.nearest_ball()
#            pos_balls = list(filter(lambda x: x != boy1.nearest_ball(), pos_balls))
#            move_boy2 = boy2.nearest_ball()
#        else:
#            move_boy2 = boy2.nearest_ball()
#            pos_balls = list(filter(lambda x: x != boy2.nearest_ball(), pos_balls))
#            move_boy1 = boy1.nearest_ball()
#    else:
#        move_boy1 = boy1.nearest_ball()
#        move_boy2 = boy2.nearest_ball()
    same_accio = 0   
            
    for i in boys:
        
        
        if i == boy1.entity_id:
            ac = list(filter(lambda x: check_accio(x) and dist(x,boy1.get_pos())<4000 and dist(x,boy1.get_pos())>600 and dist(x,boy2.get_pos())>600, pos_balls))
            if boy1.state == 1:
                print("THROW " + str(goal[0]) + " " + str(goal[1]) + " " + str(500))
            elif ac != [] and my_magic > 15 and same_accio != dict_balls[str(ac[0])]:
                print("ACCIO " + str(dict_balls[str(ac[0])]))
                same_accio = dict_balls[str(ac.pop(0))]
            else:
                print("MOVE " + str(move_boy1[0]) + " " + str(move_boy1[1]) + " " + str(150))
        else:
            ac = list(filter(lambda x: check_accio(x) and dist(x,boy2.get_pos())<4000 and dist(x,boy2.get_pos())>600 and dist(x,boy1.get_pos())>600, pos_balls))
            if boy2.state == 1:
                print("THROW " + str(goal[0]) + " " + str(goal[1]) + " " + str(500))
            elif ac != [] and my_magic > 15 and same_accio != dict_balls[str(ac[0])]:
                print("ACCIO " + str(dict_balls[str(ac[0])]))
                same_accio = dict_balls[str(ac.pop(0))]
            else:
                print("MOVE " + str(move_boy2[0]) + " " + str(move_boy2[1]) + " " + str(150))
            
        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr)


        # Edit this line to indicate the action for each wizard (0 ? thrust ? 150, 0 ? power ? 500)
        # i.e.: "MOVE x y thrust" or "THROW x y power"
        #print("MOVE 8000 3750 100")