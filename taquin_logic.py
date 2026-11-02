import random

# configuration finale
GOAL = (1, 2, 3,
        8, 0, 4,
        7, 6, 5)

# Heuristiques
def h_misplaced(state):
    for i in range(9):
        if state[i] != 0 and state[i] != GOAL[i]:
            count = count + 1
    return count


def h_manhattan(state):
    total = 0
    for i in range(9):
        if state[i] != 0:
            j = GOAL.index(state[i])
            row_diff = abs(i // 3 - j // 3)
            col_diff = abs(i % 3 - j % 3)
            total = total + row_diff + col_diff
    return total


# Deplacements
def get_successors(state):
    result = []
    e = state.index(0)
    row = e // 3
    col = e % 3
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in moves:
        r = row + dr
        c = col + dc
        if r >= 0 and r < 3 and c >= 0 and c < 3:
            t = r * 3 + c
            new_state = list(state)
            new_state[e] = new_state[t]
            new_state[t] = 0
            result.append(tuple(new_state))
    return result


def move_tile(state, i):
    e = state.index(0)
    same_row = (i // 3 == e // 3) and abs(i % 3 - e % 3) == 1
    same_col = (i % 3 == e % 3) and abs(i // 3 - e // 3) == 1
    if same_row or same_col:
        new_state = list(state)
        new_state[e] = new_state[i]
        new_state[i] = 0
        return tuple(new_state)
    return None


def shuffle_state(state, n):
    for k in range(n):
        state = random.choice(get_successors(state))
    return state


# Algorithme A* 
def a_star(start, h):
    open_list = {}
    closed = {}
    explored = []

    open_list[start] = (h(start), 0, None)

    while len(open_list) > 0:
        current = min(open_list, key=lambda s: (open_list[s][0], h(s)))
        f, g, parent = open_list.pop(current)
        closed[current] = (f, g, parent)
        explored.append((current, g, h(current), f))

        if current == GOAL:
            path = []
            node = current
            while node is not None:
                path.append(node)
                node = closed[node][2]
            path.reverse()
            return path, explored

        for nxt in get_successors(current):
            g2 = g + 1                       
            f2 = g2 + h(nxt)
            if nxt in open_list:
                if g2 < open_list[nxt][1]:
                    open_list[nxt] = (f2, g2, current)
            elif nxt in closed:
                if g2 < closed[nxt][1]:
                    del closed[nxt]
                    open_list[nxt] = (f2, g2, current)
            else:
                open_list[nxt] = (f2, g2, current)

    return None, explored 