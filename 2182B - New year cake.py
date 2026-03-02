for _ in range(int(input())):
    a,b = map(int, input().split())
    def simulate(opener, follower):
        h=0
        cost =1 

        while True:
            if h%2==0:
                if opener>=cost:
                    opener-=cost 
                else:
                    break
            else:
                if follower >= cost:
                    follower-=cost
                else:
                    break
        
            h+=1
            cost = cost*2 
        return h

    score1 = simulate(a,b)
    score2 = simulate(b,a)
    print(max(score1, score2))    


    


            

