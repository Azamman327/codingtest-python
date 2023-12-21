def solution(wallpaper):
    xlist = []
    ylist = []
    
    for y in range(len(wallpaper)):
        for x in range(len(wallpaper[y])):
            if wallpaper[y][x] == "#":
                xlist.append(x)
                ylist.append(y)
    
    return [min(ylist), min(xlist), max(ylist) + 1, max(xlist) + 1]
                