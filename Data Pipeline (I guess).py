import time
import random
import pickle



def base_poongs(x, qew = "systemt2.txt", pew = "playert2.txt"):
    timerstart = time.time()
    
    for p in range(x):
    
        squares = ['a1', 'a2', 'a3','b1', 'b2', 'b3', 'c1', 'c2', 'c3']
        winner = [['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'], ['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'], ['a1', 'b2', 'c3'], ['a3', 'b2', 'c1']]
        playersquares = []
        systemsquares = []
        print("| a1 | a2 | a3 | \n"
              "| b1 | b2 | b3 | \n"
              "| c1 | c2 | c3 |")
        print("The above is for your reference as to which square has been saved as what on the system." + "           " + "Run Number:         ", p+1)
        
        player = "neutral"
        system = "neutral"
        def check_val(s):
            if s == []:
                return False
            else:
                return True
    
        x = True
        
        while x == True:
        
            if x == True:
                if check_val(squares) == True:
                
                    a = random.randint(0, (len(squares) - 1))
                    q = squares[a]
                    playersquares.append(q)
                    squares.remove(q)
                    print("player chose:    ", q)
                    for c in winner:
                        if c[1] in playersquares and c[2] in playersquares and c[0] in playersquares:
                            print("player won")
                            x = False
                            player = "W"
                            system = "L"
        
        
            if x == True:
                if check_val(squares) == True:
    
                    g = random.randint(0, (len(squares) - 1))
                    w = squares[g]
                    systemsquares.append(w)
                    squares.remove(w)
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
    
    
        with open(qew, "a+") as stuffies:
            stuffies.write(str(systemsquares) + "  --->  " + system + "\n")
        
        with open(pew, "a+") as stuffies:
            stuffies.write(str(playersquares) + "  --->  " + player + "\n")
        
        print("end of operation")
        print("Run over:                                                                    :::::::::::::::::::::::                           ", p+1)
    
    timerend = time.time()
    print(timerend - timerstart)


def refiner1(y, qew = 'playert2.txt', pew = 'systemt2.txt', chew = 'Refinedt2-2.pkl'):
    board = [0,0,0,
             0,0,0,
             0,0,0]
    
    positions = {'a1': 0, 'a2' : 1, 'a3' : 2, 'b1' : 3, 'b2' : 4, 'b3' : 5, 'c1' : 6, 'c2' : 7, 'c3' : 8}
    extraction = [(2, 3), (8, 9), (14, 15), (20, 21), (26, 27)]
    playstuff = open(qew, 'r')
    playdata = playstuff.readlines()
    playstuff.close()
    sysstuff = open(pew, 'r')
    sysdata = sysstuff.readlines()
    sysstuff.close()
    
    for l in range(y):
    
        print("                                                                                      Run Number:            ", l+1)
        board = [0,0,0,
             0,0,0,
             0,0,0]
        
        extractor = 0
        syssquares = []
        playsquares = []
        gameorder = []
        winner = " "
    
        
        playinfo = playdata[l]
        print(playinfo)
        x = 0
        for i in range(0,len(playinfo)):
                if playinfo[i] == ']':
                    x = i
    
        if x == 11:
            extractor = 2
        elif x == 17:
            extractor = 3
        elif x == 23:
            extractor = 4
        elif x == 29:
            extractor = 5
    
        for i in range(extractor):
            playsquares.append(playinfo[extraction[i][0]] + playinfo[extraction[i][1]])
    
        if playinfo[-2] == "W":
            winner = "P"
            print(playinfo[-2])
    
        sysinfo = sysdata[l]
        print(sysinfo)
        x = 0
        for i in range(0,len(sysinfo)):
                if sysinfo[i] == ']':
                    x = i
    
        if x == 11:
            extractor = 2
        elif x == 17:
            extractor = 3
        elif x == 23:
            extractor = 4
    
        for i in range(extractor):
            syssquares.append(sysinfo[extraction[i][0]] + sysinfo[extraction[i][1]])
    
        if sysinfo[-2] == "W":
            winner = "S"
        elif sysinfo[-2] == "D":
            winner = "N"
    
        if len(playsquares)>len(syssquares):
            for i in range(len(syssquares)):
                gameorder.append(playsquares[i])
                gameorder.append(syssquares[i])
            gameorder.append(playsquares[-1])
    
        elif len(playsquares) == len(syssquares):
            for i in range(len(syssquares)):
                gameorder.append(playsquares[i])
                gameorder.append(syssquares[i])
    
        print(gameorder)
    
        binaryorder = []
        sysbinaryorder = []
        playbinaryorder = []
    
        for i in playsquares:
            playbinaryorder.append(positions[i])
    
        for i in syssquares:
            sysbinaryorder.append(positions[i])
    
        for i in gameorder:
            binaryorder.append(positions[i])
    
        print(binaryorder)
        
        
        with open(chew, 'ab+') as stage1:
            pickle.dump([binaryorder, winner],stage1)

def refiner2(qew = 'Refinedt2-2.pkl', pew = 'refinedt2-3.pkl'):
    ts = time.time() 
    
    srs = open(qew,'rb+')
    sres = open(pew,'ab+')
    
    f = True
    t= 1
    while f is True:
        try:
            boardstate = [0,0,0,0,0,0,0,0,0]
            g = pickle.load(srs)
            nm = g[0][0]
            np = 'P'
            wm = len(g[0])
            winner = g[1]
            pickle.dump([tuple(boardstate),np,nm,wm,winner], sres)
            print([tuple(boardstate),np,nm,wm,winner]) 
            for y in range(len(g[0])):
                if y in [0,2,4,6,8]:
                    boardstate[g[0][y]] = 1
                    np = 'S'
                else:
                    boardstate[g[0][y]] = 2
                    np = 'P'
                if y == len(g[0]) - 1:
                    nm = 9
                else:
                    nm = g[0][y+1]
                wm -= 1
                if wm == 0:
                    np = 'N'
        
                pickle.dump([tuple(boardstate),np,nm,wm,winner], sres)
                print([tuple(boardstate),np,nm,wm,winner])
            print("                                                                                                  ::::::::::::::          ", t)
            t += 1
        except EOFError:
            f = False
            break
    
    srs.close()
    sres.close()
    
    te = time.time()
    
    print(te-ts)

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


def creditassignment(qew = 'refinedt2-3.pkl', pew = 'refinedt2-4p.pkl', chew = 'refinedt2-4s.pkl', lew = 'refinedt2-4s.txt', sew = 'refinedt2-4p.txt'):
    ts = time.time()
    srs = open(qew, 'rb+')
    sresp = open(pew, 'ab+')
    sress = open(chew, 'ab+')
    sreess = open(lew, 'a+')
    sreesp = open(sew, 'a+')
    pdick = {}
    sdick = {}
    
    hmm = 1
    ghh = True
    xexex = 1
    while ghh is True:
        try:
            mew = pickle.load(srs)
            ml = mew[-2]
            pm = mew[-3]
            w = mew[-1]
            np = mew[-4]
            bs = mew[0]
            if np == 'P':
                if w == 'P':
                    c = 1.2
                elif w == 'N':
                    c = 1.0
                elif w == 'S':
                    c = -1.2
    
                if bs in pdick:
                    prs = "not found"
                    l = []
                    p = []
                    for t in pdick[bs]:
                        l.append(t[0])
                    for i in range(len(l)):
                        if l[i] == pm:
                            qwe = i
                            prs = "found"
                            break
                        
                    if prs == "found":
                        pdick[bs][qwe][1] = ((pdick[bs][qwe][1])*(pdick[bs][qwe][2])+c)/(pdick[bs][qwe][2]+1)
                        pdick[bs][qwe][2] += 1
                    elif prs != "found":
                        pdick[bs].append([pm,c,1])
    
                elif bs not in pdick:
                    pdick[bs] = [[pm,c,1]]
    
                    
            if np == 'S':
                if w == 'S':
                    c = 1.2
                elif w == 'N':
                    c = 1.0
                elif w == 'P':
                    c = -1.2
    
                if bs in sdick:
                    prs = "not found"
                    l = []
                    p = []
                    for t in sdick[bs]:
                        l.append(t[0])
                    for i in range(len(l)):
                        if l[i] == pm:
                            qwe = i
                            prs = "found"
                            break
                        
                    if prs == "found":
                        sdick[bs][qwe][1] = ((sdick[bs][qwe][1])*(sdick[bs][qwe][2])+c)/(sdick[bs][qwe][2]+1)
                        sdick[bs][qwe][2] += 1
                    elif prs != "found":
                        sdick[bs].append([pm,c,1])
    
                elif bs not in sdick:
                    sdick[bs] = [[pm,c,1]]
    
            print("                                           :::::::::                        ", xexex)
            xexex += 1
        except EOFError:
            ghh = False
            break

def randoplay(x):

    
    
    
            
bebe = int(input("thoos"))
randoplay(bebe)
