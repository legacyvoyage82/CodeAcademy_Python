#%%

def distance_from_zero(x):
    if type(x) == int or type(x) == float:
        return abs(x)
    else:
        return "Nope"

print(distance_from_zero(8.9))
print(distance_from_zero(3))
print(distance_from_zero("batman"))