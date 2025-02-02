def solve(heads,legs):
    y = (legs - 2*heads)//2
    x = heads - y
    
    return x, y


chickens, rabbits = solve(35,94)
print(f"chickens: {chickens}, Rabbits: {rabbits}")