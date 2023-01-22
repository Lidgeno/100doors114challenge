result=-1

def buttonpush(lightar,button):
    # Here we put the action caused by the different buttons
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

    return lightar


def seriepush(i):
    # Here, the idea is to convert an integer into a binary
    # The binary will perform the push of a button on every 1 it contains
    # the rank of this 1 giving the bulb number to push
    # by example 18 = 10010 which is 10000+10 which is 1 of rank 5 and 1 of rank 2, the bulbs pushed will be 5 and 2

    #initialization of seriear, we'll put in every bulb we intend to push
    seriear=['x',0,0,0,0,0,0,0,0,0]

    #starting condition (if the lightbulbs are different, change this parameter)
    lightar=["X",1,1,0,0,0,0,1,0,1]
    
    print("Number is :",i)
    
    for j in range(8,-1,-1):
        # if 2^n is lower than our number, then the number contains a 1 at that rank
        # we do not start at 9 because 2^9 = 512 which is greater than 511
        if 2**j<=i:
            # of course we must not forget to withdraw this number in order to get the remaining 1 in this binary number
            i=i-2**j
            # if it's a 1, then write as 1 the according cell in array
            seriear[j+1]=1
    
    print("We will then push the following bulbs")
    print(seriear)
    
    # for every bulb we intended to push, push it and get the result in lightar
    for j in range(0,10):
        if(seriear[j]==1):
            lightar=buttonpush(lightar,j)

    print("Lights would look like :")
    print(lightar)
    
    return(lightar)
    

# for every possible solution, 0 to 511 do
for counter1 in range(0,512,1):
    # give the result for the binary of this number being pushed
    lightar=seriepush(counter1)
    
    # initialize counter 2
    counter2=0
    
    # check how many light bulbs are on (if it's not what we want as a result, change that part)
    for j in range(0,10):
        if(lightar[j]==1):
            counter2=counter2+1
    # we want all 9 bubls on
    if counter2==9:
        print("!!!!! SOLUTION !!!!!")
        print(counter1)
        result=counter1
    # well this displays the last answer at the end (although there might be intermediate answers)
    if(result = -1):
        print("sorry, no answer detected")
    else:
        print(seriepush(result))