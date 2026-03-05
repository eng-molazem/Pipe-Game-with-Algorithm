# pipe_game.py (Full updated version with assets/ and Lvl1.txt)
import pygame, sys, time
from collections import deque
import heapq
import os

TILE_SIZE = 64
WINDOW_BG = (30, 30, 30)
MAP_FILENAME = "Lvl3.txt" 

ASSET_DIR = os.path.join(os.path.dirname(__file__), "assets")

IMAGE_FILES = {
    "straight_empty": os.path.join(ASSET_DIR, "straight_empty.png"),
    "straight_full":  os.path.join(ASSET_DIR, "straight_full.png"),
    "elbow_empty":    os.path.join(ASSET_DIR, "elbow_empty.png"),
    "elbow_full":     os.path.join(ASSET_DIR, "elbow_full.png"),
    "tee_empty":      os.path.join(ASSET_DIR, "tee_empty.png"),
    "tee_full":       os.path.join(ASSET_DIR, "tee_full.png"),
    "cross_empty":    os.path.join(ASSET_DIR, "cross_empty.png"),
    "cross_full":     os.path.join(ASSET_DIR, "cross_full.png"),
    "stone":          os.path.join(ASSET_DIR, "stone.png"),
}

DIR_VECT = [(0, -1), (1, 0), (0, 1), (-1, 0)]

BASE_OPENINGS = {
    "straight": {0, 2},
    "elbow": {0, 1},
    "tee": {0, 1, 3},
    "cross": {0, 1, 2, 3},
    "stone": set(),
    "empty": set(),
}

SYMBOL_MAP = {
    "|": ("straight", 0),
    "-": ("straight", 1),
    "L": ("elbow", 0),
    "T": ("tee", 0),
    "+": ("cross", 0),
    "#": ("stone", 0),
    "S": ("straight", 0),
    "E": ("straight", 0),
    ".": ("empty", 0),
}

def load_map(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    with open(path, "r", encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f]
    grid = []
    start = None
    end = None
    for y, ln in enumerate(lines):
        row = []
        for x, ch in enumerate(ln):
            if ch not in SYMBOL_MAP:
                ch = "."
            ttype, trot = SYMBOL_MAP[ch]
            cell = {"type": ttype, "rot": trot, "symbol": ch}
            row.append(cell)
            if ch == "S":
                start = (x, y)
            if ch == "E":
                end = (x, y)
        grid.append(row)
    return grid, start, end


def openings_of(ttype, rot):
    if ttype == "straight":
        base = {0, 2}
    elif ttype == "elbow":
        base = {0, 1}
    elif ttype == "tee":
        base = {0, 1, 3}
    elif ttype == "cross":
        base = {0, 1, 2, 3}
    else:
        base = set()
    return {(d + rot) % 4 for d in base}



def load_images():
    imgs = {}
    for key, fname in IMAGE_FILES.items():
        try:
            img = pygame.image.load(fname).convert_alpha()
            img = pygame.transform.smoothscale(img, (TILE_SIZE, TILE_SIZE))
            imgs[key] = img
        except Exception:
            imgs[key] = None
    return imgs


def draw_tile(surface, imgs, x, y, cell, filled, start, end):
    rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    t = cell["type"]
    rot = cell["rot"]

    if t == "stone":
        img = imgs.get("stone")
        if img:
            surface.blit(img, rect)
        else:
            pygame.draw.rect(surface, (100, 100, 100), rect)
        return

    if t == "empty":
        return

    is_filled = filled or ((x, y) == start)

    kind = t
    key = f"{kind}_{'full' if is_filled else 'empty'}"
    img = imgs.get(key)
    
    if img:
        rimg = pygame.transform.rotate(img, -90 * rot)
        rrect = rimg.get_rect(center=rect.center)
        surface.blit(rimg, rrect.topleft)
    else:
        pygame.draw.rect(surface, (50, 50, 50), rect)
        color = (30, 160, 255) if is_filled else (180, 180, 180)
        center = rect.center
        pygame.draw.circle(surface, color, center, TILE_SIZE // 4)
        for d in openings_of(t, rot):
            dx, dy = DIR_VECT[d]
            sx = center[0] + dx * (TILE_SIZE // 4)
            sy = center[1] + dy * (TILE_SIZE // 4)
            pygame.draw.line(surface, color, center, (sx, sy), 10)

def compute_filled(grid, start):
    if not start:
        return set()
    W = len(grid[0])
    H = len(grid)
    visited = set()
    q = deque()

    sx, sy = start
    if grid[sy][sx]["type"] in ("stone", "empty"):
        return set()
    visited.add(start)
    q.append(start)

    while q:
        x, y = q.popleft()
        cell = grid[y][x]
        if cell["type"] in ("stone", "empty"):
            continue

        cur_open = openings_of(cell["type"], cell["rot"])
        for d in cur_open:
            nx = x + DIR_VECT[d][0]
            ny = y + DIR_VECT[d][1]
            if 0 <= nx < W and 0 <= ny < H:
                neigh = grid[ny][nx]
                if neigh["type"] in ("stone", "empty"):
                    continue

                neigh_open = openings_of(neigh["type"], neigh["rot"])
                if ((d + 2) % 4) in neigh_open:
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        q.append((nx, ny))
    return visited

def grid_to_state(grid):
    return tuple(cell["rot"] for row in grid for cell in row)


def state_to_grid(state, template_grid):
    W = len(template_grid[0]); H = len(template_grid)
    new = []
    i = 0
    for y in range(H):
        row = []
        for x in range(W):
            base = dict(template_grid[y][x])
            base["rot"] = state[i]
            row.append(base)
            i += 1
        new.append(row)
    return new


def index_of_pos(pos, grid):
    x, y = pos
    W = len(grid[0])
    return y * W + x

def is_goal_state(state, template_grid, start, end):
    grid = state_to_grid(state, template_grid)
    filled = compute_filled(grid, start)
    if not end:
        targets = {(x, y) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x]["type"] not in ("stone", "empty")}
        return targets.issubset(filled)
    else:
        return end in filled



def astar_solve(template_grid, start, end, max_iters=300000):
    W = len(template_grid[0]); H = len(template_grid) 
    start_state = grid_to_state(template_grid) 
    #notrotatr S+E
    start_idx = index_of_pos(start, template_grid) if start else None
    end_idx = index_of_pos(end, template_grid) if end else None

    
    rotatable = []
    for y in range(H):
        for x in range(W):
            t = template_grid[y][x]["type"]
            idx = y * W + x
            if t in ("stone", "empty", "cross"):
                continue
            if start_idx is not None and idx == start_idx:
                continue
            if end_idx is not None and idx == end_idx:
                continue
            rotatable.append(idx)

    def neighbors(state):
        res = []
        for idx in rotatable:
            new = list(state)
            new[idx] = (new[idx] + 1) % 4
            res.append((tuple(new), idx))
        return res

    pq = []
    heapq.heappush(pq, (0, 0, start_state, None))  
    came_from = {start_state: (None, None)} 
    gscore = {start_state: 0}
    iters = 0

    while pq:
        f, g, state, _ = heapq.heappop(pq)
        iters += 1
        if iters > max_iters:
            break
        
        if is_goal_state(state, template_grid, start, end):
            path = []
            cur = state
            while came_from[cur][0] is not None:
                prev, move_idx = came_from[cur]
                path.append(move_idx)
                cur = prev
            path.reverse()

            moves_pos = []
            for idx in path:
                x = idx % W
                y = idx // W
                moves_pos.append((x, y))
            return moves_pos

        
        for nstate, move_idx in neighbors(state):
            tentative_g = gscore[state] + 1 
            if nstate not in gscore or tentative_g < gscore[nstate]:
                gscore[nstate] = tentative_g 
                heapq.heappush(pq, (tentative_g, tentative_g, nstate, move_idx))
                came_from[nstate] = (state, move_idx)
    return None 



def show_win_message(screen, W, H):

    font = pygame.font.SysFont(None, 96)
    txt = font.render("YOU WIN !!", True, (255, 220, 0))
    rect = txt.get_rect(center=(W * TILE_SIZE // 2, H * TILE_SIZE // 2))

    overlay = pygame.Surface((W * TILE_SIZE, H * TILE_SIZE), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    screen.blit(overlay, (0, 0))
    screen.blit(txt, rect)
    pygame.display.flip()
    pygame.time.wait(2000)

# ----------------------------
# Main game loop



def main():
    pygame.init() 
    pygame.font.init()

    grid, start, end = load_map(MAP_FILENAME)
    if not start:
        print("Warning: no start 'S' found in map. Place 'S' where start tile should be")
    if not end:
        print("No end 'E' found in map. The solver will try to fill all tiles as goal")

    H = len(grid)
    W = len(grid[0]) 

    screen = pygame.display.set_mode((W * TILE_SIZE, H * TILE_SIZE))
    pygame.display.set_caption("Pipe Game - Algorithm")

    imgs = load_images()
    clock = pygame.time.Clock()


    solver_moves = None 
    animating = False 
    anim_index = 0 
    anim_start_time = 0 
    per_move_delay = 120 
    last_move_time = 0 

    won = False

    while True:
        dt = clock.tick(60) 

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT: 
                pygame.quit(); sys.exit()

            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_n and not animating and not won: 
                    print("Running Algorithm")
                    template = [[dict(c) for c in row] for row in grid]  
                    moves = astar_solve(template, start, end)
                    if moves is None:
                        print("No solution found.")
                        continue
                    solver_moves = moves
                    total_moves = max(1, len(solver_moves))
                    total_ms = max(3000, total_moves * 100)
                    per_move_delay = total_ms / total_moves
                    animating = True
                    anim_index = 0
                    anim_start_time = pygame.time.get_ticks()
                    last_move_time = anim_start_time
                    print(f"Solution has {len(solver_moves)} moves. Animating over {total_ms/1000:.2f}s.")

            elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1 and not animating and not won: 
                mx, my = ev.pos
                gx, gy = mx // TILE_SIZE, my // TILE_SIZE
                if 0 <= gx < W and 0 <= gy < H:
                    if start and (gx, gy) == start:
                        pass
                    elif end and (gx, gy) == end:
                        pass
                    else:
                        cell = grid[gy][gx]
                        if cell["type"] not in ("stone", "empty"):
                            cell["rot"] = (cell["rot"] + 1) % 4 


        if animating and solver_moves:
            now = pygame.time.get_ticks()
            if anim_index < len(solver_moves) and now - last_move_time >= per_move_delay:
                x, y = solver_moves[anim_index]
                if grid[y][x]["type"] not in ("stone", "empty"):
                    grid[y][x]["rot"] = (grid[y][x]["rot"] + 1) % 4
                anim_index += 1
                last_move_time = now
            if anim_index >= len(solver_moves):

                if pygame.time.get_ticks() - anim_start_time >= 3000:
                    animating = False
                    solver_moves = None
                    print("Animation complete.")


        filled = compute_filled(grid, start) if start else set()


        screen.fill(WINDOW_BG)
        for y in range(H):
            for x in range(W):
                draw_tile(screen, imgs, x, y, grid[y][x], (x, y) in filled, start, end) 


        for gx in range(W + 1):
            pygame.draw.line(screen, (20, 20, 20), (gx * TILE_SIZE, 0), (gx * TILE_SIZE, H * TILE_SIZE))
        for gy in range(H + 1):
            pygame.draw.line(screen, (20, 20, 20), (0, gy * TILE_SIZE), (W * TILE_SIZE, gy * TILE_SIZE))

        pygame.display.flip() 


        if not won and end and (end in filled):
            won = True
            print("You Win !!")
            show_win_message(screen, W, H)



if __name__ == "__main__":
    main()
