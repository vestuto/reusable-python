a = 1
b = 2
c = 3

def local_things():
    g = 7
    h = 8
    i = 9
    const = locals()
    return const
    
def global_things():
    l = 12
    m = 13
    n = 14
    const_l = locals()
    const_g = globals()
    return const_l, const_g
