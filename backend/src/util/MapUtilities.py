import math



def getNeighbor(q,r,direction):
    return {
        'q': q + direction['q'],
        'r': r + direction['r']
    }

def getAllNeighbors(q, r):
    directions = [
        (1, 0),   # East
        (1, -1),  # Northeast  
        (0, -1),  # Northwest
        (-1, 0),  # West
        (-1, 1),  # Southwest
        (0, 1)    # Southeast
    ]

    neighbors = []
    for dq, dr in directions:
        neighbors.append({
            'q': q + dq,
            'r': r + dr
        })

    return neighbors


def axialToPixel(q, r, hexSize=20):
    x = hexSize * (3/2 * q)
    y = hexSize * (math.sqrt(3) * (r + q / 2))
    return (x, y)

def pixelToAxal(x, y, hexSize=20):
    q = (2/3 * x) / hexSize
    r = (-1/3 * x + math.sqrt(3)/3 * y) / hexSize
    return roundAxial(q, r)

def roundAxial(q, r):
    # Convert to cube, round, convert back
    x = q
    y = -q - r
    z = r
    rx = round(x)
    ry = round(y)
    rz = round(z)
   
    x_diff = abs(rx - x)
    y_diff = abs(ry - y)
    z_diff = abs(rz - z)

    if x_diff > y_diff and x_diff > z_diff:
        x = -y - z
    elif y_diff > z_diff:
        y = -x - z
    else:
        z = -x - y
    return {q: x, r: z}

def hexDistance(q1, r1, q2, r2):
    """Manhattan distance between two hexes"""
    return max(abs(q1 - q2) + abs(q1 + r1 - q2 - r2) + abs((r1 - r2)) / 2)

def hexesInRange(centerQ, centerR, range):
    """Get all hexes within a certain range of a center hex"""
    results = []
    for q in range(-range, range + 1):
        r1 = max(-range, -q - range)
        r2 = min(range, -q + range)
        for r in range(r1, r2 + 1):
            results.append({
                'q': centerQ + q,
                'r': centerR + r
            })
    return results

def hexLine(q1, r1, q2, r2):
    """Get all hexes on a straight line between two points"""
    distance = hexDistance(q1, r1, q2, r2)
    results = []
    
    for i in range(distance + 1):  
        t = 0 if distance == 0 else i / distance  
        q = lerp(q1, q2, t)
        r = lerp(r1, r2, t)
        results.append(roundAxial(q, r))
    return results

def lerp(a, b, t):
    return a * (1 - t) + b * t


def hasLineOfSight(q1, r1, q2, r2, blocked_hexes):
    line = hexLine(q1, r1, q2, r2)
    path = line[1:-1]  
    
    for hex_pos in path:
        if hex_pos in blocked_hexes:
            return False
    return True

def fireProjectile(start_q, start_r, target_q, target_r, game_map):
    path = hexLine(start_q, start_r, target_q, target_r)
    
    for i, (q, r) in enumerate(path[1:], 1):
        hex_data = game_map.get_hex(q, r)
        
        if hex_data and hex_data.get('blocks_projectiles'):
            return {
                'hit_position': (q, r),
                'hit_object': hex_data,
                'path_taken': path[:i+1]
            }
    
    return {'hit_position': path[-1], 'path_taken': path}

def getMovementPath(start_q, start_r, end_q, end_r):
    """Get the hexes a unit moves through"""
    path = hexLine(start_q, start_r, end_q, end_r)
    return path[1:]

def calculateMovementCost(path, terrain_map):
    """Calculate total movement cost"""
    total_cost = 0
    for q, r in path:
        terrain = terrain_map.get((q, r), 'normal')
        cost = {'normal': 1, 'forest': 2, 'mountain': 3, 'water': 999}
        total_cost += cost.get(terrain, 1)
    return total_cost


"""EXAMPLE PLASMA"""
def plasmaBolt(start_q, start_r, end_q, end_r, game_map):
    """Plasma spell affects all hexes in a line"""
    affected_hexes = hexLine(start_q, start_r, end_q, end_r)
    
    for q, r in affected_hexes:
        unit = game_map.get_unit_at(q, r)
        if unit:
            unit.take_damage(25)  # Plasma damage

        # Visual effect
        game_map.add_effect(q, r, 'plasma', duration=1.0)