def water_jug():
    jug1=0 #4
    jug2=0 #3
    
    while True:
        print(f"Jug1: {jug1}L, Jug2: {jug2}L")
        
        if jug1==2 or jug2 ==2:
            print("Goal reached")
            break
        if jug1==0:
            jug1=4
        elif jug2!=3:
            pour =min(jug1,3-jug2)
            jug1-=pour
            jug2+=pour
        else:
            jug2=0
    print("Final answer: ")
    if jug1==2:
        jug2=0;
    if jug2==2:
        jug1=0
    print(f"Jug1: {jug1}L, Jug2: {jug2}L")
water_jug()
