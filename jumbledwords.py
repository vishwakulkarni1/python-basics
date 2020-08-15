import random 
def choose():
    words=['rainbow','computer','science','programming','mathematics','player','condition','reverse','water','board','samsung','introduction','river','iphone']
    pick = random.choice(words)
    return pick
def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled
def thank(p1n,p2n,p1,p2):
    print(p1n,'your score is :',p1)
    print(p2n,'your score is :',p2)
    print('thanks for playing')
    print('have a nicee day')
def play():
    p1name=input('player1,please enter your name ')
    p2name=input('player2,please enter your name ')
    pp1=0
    pp2=0
    turn=0
    while(1):
        picked_word=choose()
        qn=jumble(picked_word)
        print(qn)
        if turn % 2== 0:
            print(p1name,' your turn')
            ans=input('what is on your mind?')
            if ans==picked_word:
                pp1=pp1+1
                print('your score is:',pp1)
            else:
                print('better luck next time',picked_word)
                c=input('press 1 to continue and 0 to quit :')
                if c==0:
                    thank(p1name,p2name,pp1,pp2)
                    break
        else:
            print(p2name,' your turn')
            ans=input('what is on your mind?')
            if ans==picked_word:
                pp2=pp2+1
                print('your score is:',pp2)
            else:
                print('better luck next time',picked_word)
                c=input('press 1 to continue and 0 to quit :')
                if c==0:
                    thank(p1name,p2name,pp1,pp2)
                     break
                    turn=turn+1
play()               