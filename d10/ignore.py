# remove all of the stuff that isn't connected
for y in range(0,len(lines)):
    for x in range(0, len(lines[y])):
        minx = max(0,x-1)
        maxx = min(len(lines[y])-1, x+1)
        miny = max(0, y-1)
        maxy = min(len(lines)-1, y+1)

        for cy in range(miny, maxy+1):
            for cx in range(minx, maxx + x):
                

        '''
        maxx = min(number[1][1]+1, schema_max_x)
    maxy = min(number[1][0]+1, schema_max_y)
    minx = max(0, number[1][1]-len(number[0]))
    miny = max(0, number[1][0]-1)'''