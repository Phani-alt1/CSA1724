def vaccum(environment,current_position):
    actions=[]
    status_a,status_b=environment
    print("Initial Condition of environment: ",environment)
    for _ in range(2):
        if current_position=='A':
            if status_a=='Dirty':
                actions.append("Suck")
                status_a='Clean'
            actions.append("Right")
            current_position="B"
        elif current_position=="B":
            if status_b=="Dirty":
                actions.append("Suck")
                status_b='Clean'
            actions.append("Left")
            current_position='A'
    print("Final Environment; A= ",status_a,",B = ",status_b)
    return actions
env =['Dirty','Dirty']
start='A'
steps=vaccum(env,start)
print("Actions: ",steps)
