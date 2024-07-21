#nk = list(map(int,input().split()))       #for taking n spaced integer input

def find_side(coordinates_x,coordinates_y):
    min_x=min(coordinates_x)
    max_x=max(coordinates_x)
    min_y=min(coordinates_y)
    max_y=max(coordinates_y)

    side=min((max_x-min_x),(max_y-min_y))
    return side


T=int(input())
areas=[]
for i in range(T):
    n = int(input())
    coordinates_x=[]
    coordinates_y=[]
    for j in range(n):
        coordinates_input = list(map(int, input().split()))
        coordinates_x.append(coordinates_input[0])
        coordinates_y.append(coordinates_input[1])
    side=find_side(coordinates_x,coordinates_y)
    area=side*side
    areas.append(area)
for x in areas:
    print(x)
