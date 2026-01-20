import pickle
srsr = open('refinedt2-4p.pkl', 'rb+')
prpr = open('refinedt2-4s.pkl', 'rb+')
n = pickle.load(prpr)
m = pickle.load(srsr)
srsr.close()
prpr.close()

squares = [0,1,2,3,4,5,6,7,8]
winner = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [6,4,2]]

playersquares = []
systemsquares = []

player = 'neutral'
system = 'neutral'

def choose(bb,bob):
    q = bob[bb]
    m = q[0][1]
    g = 9
    for t in range(len(q)):
        if q[t][1]>m:
            m = q[t][1]
            g = q[t][0]
        elif m == q[0][1]:
            g = q[0][0]
    return(g)

def check_val(s):
    if s == []:
        return False
    else:
        return True
bs = [0,0,0,0,0,0,0,0,0]

x = True

while x == True:
    
    
    if x == True:
        if check_val(squares) == True:
            q = choose(tuple(bs),m)
            playersquares.append(q)
            squares.remove(q)
            bs[q] = 1
            print("player chose:    ", q)
            for c in winner:
                if c[1] in playersquares and c[2] in playersquares and c[0] in playersquares:
                    print("player won")
                    x = False
                    player = "W"
                    system = "L"
        
        
    if x == True:
        if check_val(squares) == True:
            w = int(input(":"))
            systemsquares.append(w)
            squares.remove(w)
            bs[w] = 2
            print("The system chose: ", w)
            for c in winner:
                if c[1] in systemsquares and c[2] in systemsquares and c[0] in systemsquares:
                    print("system won")
                    x = False
                    player = "L"
                    system = "W"

        elif check_val(squares) == False:
            print("Draw")
            system, player = "D", "D"
            x = False

