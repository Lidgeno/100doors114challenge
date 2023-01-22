result=0

def buttonpush(lightar,button):
    #print(button)
    match button:
        case 0:
            button=0
        case 1:
            lightar[1]=(lightar[1]+1)%2
            lightar[6]=(lightar[6]+1)%2
            lightar[8]=(lightar[8]+1)%2
        case 2:
            lightar[2]=(lightar[2]+1)%2
            lightar[6]=(lightar[6]+1)%2
            lightar[7]=(lightar[7]+1)%2
            lightar[9]=(lightar[9]+1)%2
        case 3:
            lightar[3]=(lightar[3]+1)%2
            lightar[5]=(lightar[5]+1)%2
            lightar[9]=(lightar[9]+1)%2
        case 4:
            lightar[1]=(lightar[1]+1)%2
            lightar[4]=(lightar[4]+1)%2
            lightar[7]=(lightar[7]+1)%2
        case 5:
            lightar[1]=(lightar[1]+1)%2
            lightar[2]=(lightar[2]+1)%2
            lightar[3]=(lightar[3]+1)%2
            lightar[5]=(lightar[5]+1)%2
        case 6:
            lightar[4]=(lightar[4]+1)%2
            lightar[6]=(lightar[6]+1)%2
            lightar[9]=(lightar[9]+1)%2
        case 7:
            lightar[1]=(lightar[1]+1)%2
            lightar[3]=(lightar[3]+1)%2
            lightar[7]=(lightar[7]+1)%2
        case 8:
            lightar[4]=(lightar[4]+1)%2
            lightar[5]=(lightar[5]+1)%2
            lightar[8]=(lightar[8]+1)%2
        case 9:
            lightar[2]=(lightar[2]+1)%2
            lightar[8]=(lightar[8]+1)%2
            lightar[9]=(lightar[9]+1)%2
    #print(lightar)
    return lightar


def seriepush(i):
    seriear=['x',0,0,0,0,0,0,0,0,0]
    lightar=["X",1,1,0,0,0,0,1,0,1]
    print(i)
    for j in range(8,-1,-1):
        if 2**j<=i:
            i=i-2**j
            seriear[j+1]=1
            print(2**j)
            print(i)
    print(seriear)
    for j in range(0,10):
        if(seriear[j]==1):
            lightar=buttonpush(lightar,j)
    print(i)
    print(counter1)
    print(lightar)
    return(lightar)
    

for counter1 in range(0,512,1):
    lightar=seriepush(counter1)
    counter2=0
    
    for j in range(0,10):
        if(lightar[j]==1):
            counter2=counter2+1
    if counter2==9:
        print("!!!!! SOLUTION !!!!!")
        print(counter1)
        result=counter1
    print(result)
