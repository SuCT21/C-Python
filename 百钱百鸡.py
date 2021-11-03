for x in range(0,100):
    for y in range(0,100):
        for z in range(0,100):
            if (x + y + z == 100 and 3 * x + 5 * y + z / 3 == 100 and z % 3 == 0):
                print("%d,%d,%d\n",x,y,z)