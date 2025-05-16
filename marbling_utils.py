from marbling_drop import MarblingDrop

DEFAULT_SIZE = 60 # starting radius
colors = [(30, 50, 100), (50, 100, 30), (100, 30, 50)] #RGB colors used successively

def create_new_drop(x, y, drops):
    new_drop = MarblingDrop(
        x, y,
        colors[len(drops) % len(colors)],
        DEFAULT_SIZE
    )
    for existing in drops:
        displace_drop(existing, new_drop)
    drops.append(new_drop)

def displace_drop(existing, new_drop): #displacement of existing drops after a new drop is added according to Jaffer's formula
    C = PVector(new_drop.x, new_drop.y)
    r = new_drop.size / 2

    for i, P in enumerate(existing.boundary_points):
        PC = PVector.sub(P, C)
        distance = PC.mag()
        if distance > 0:
            displacement = sqrt(1 + (r**2 / distance**2))
            existing.boundary_points[i] = PVector.add(C, PVector.mult(PC, displacement))

def tine_deform(drops, M, x, y, z, c): # tineline along M vector starting from a point B(x,y). z and c are given constants.
    u = 1.0 / pow(2, 1.0 / c)
    B = PVector(x, y)

    for drop in drops:
        for i, P in enumerate(drop.boundary_points):
            PB = PVector.sub(P, B)
            N = M.copy().rotate(HALF_PI) # N is a vector normal to M
            d = abs(PB.dot(N)) # d is the length of the vertical dropped from P onto M vector emanating from B. 
            mag = z * pow(u, d)
            P.add(M.copy().mult(mag)) # updated P vector after tineline deformation

def reset_all_drops(drops):
    for drop in drops:
        drop.generate_boundary(400)
