def low(x):
    if x <= 20:
        return 1
    elif x < 50:
        return (50-x)/30
    return 0
def medium(x):
    if x <= 20 or x >= 80:
        return 0
    elif x <= 50:
        return (x-20)/30
    return (80-x)/30
def high(x):
    if x >= 80:
        return 1
    elif x > 50:
        return (x-50)/30
    return 0
# Input
level = float(input("Enter tank level: "))
demand = float(input("Enter water demand: "))
# 1. Fuzzification
L = [low(level), medium(level), high(level)]
D = [low(demand), medium(demand), high(demand)]
print("Level:", L)
print("Demand:", D)
# 2. Rule Base (0=Slow, 1=Medium, 2=Fast)
rules = [[1,2,2],
         [0,1,2],
         [0,0,1]]
# 3. Rule Evaluation and Aggregation
S = [0,0,0]
for i in range(3):
    for j in range(3):
        strength = min(L[i], D[j])
        output = rules[i][j]
        S[output] = max(S[output], strength)
print("Output strengths:", S)
# 4. Centroid Defuzzification
top = 0
bottom = 0
for z in range(101):
    mu = max(
        min(S[0], low(z)),
        min(S[1], medium(z)),   
        min(S[2], high(z))
    )
    top += z * mu
    bottom += mu
speed = top / bottom
print("Pump speed:", round(speed, 2), "%")

# a=10
# b=25
# c=40
# def low(X):
#     if X<=a:
#         return 1
#     if x<=b:
#         return b-X/b-a
#     return 0

# def medium(X):
#     if X<=a or X>=c:
#         return 0
#     if X<=b:
#         return X-a/b-a
#     return c-X/c-b

# def high(X):
#     if X>=c:
#         return 1
#     if X>=b:
#         return b-X/c-b
#     return 0