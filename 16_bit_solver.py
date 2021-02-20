import copy
import time
from collections import deque
import numpy as np

# string is fast in comparion but searching and conversion from list to string will be time consuming
# Cannot implement binay search because we have to search in unsorted array


def up(pos, state):
    x,y = pos[0], pos[1]
    n = len(state) - 1
    if x != 0:
        state[x][y], state[x-1][y] = state[x-1][y], state[x][y]
        return state
    return None

def down(pos, state):
    x,y = pos[0], pos[1]
    n = len(state) - 1
    if x != n:
        state[x][y], state[x+1][y] = state[x+1][y], state[x][y]
        return state
    return None

def left(pos, state):
    x,y = pos[0], pos[1]
    n = len(state) - 1
    if y != 0:
        state[x][y], state[x][y-1] = state[x][y-1], state[x][y]
        return state
    return None

def right(pos, state):
    x,y = pos[0], pos[1]
    n = len(state) - 1
    if y != n:
        state[x][y], state[x][y+1] = state[x][y+1], state[x][y]
        return state
    return None

def generate_children(pos, current_state):
    
    children = []
    up_move = up(pos, current_state.copy())
    down_move = down(pos, current_state.copy())
    left_move = left(pos, current_state.copy())
    right_move = right(pos, current_state.copy())
    
    if up_move:
        children.append(up_move) 
    if down_move:
        children.append(down_move)
    if left_move:
        children.append(left_move)
    if right_move:
        children.append(right_move)
    
    return children

def pos_blank_tile(state):
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] == 0:
                return (i,j)


if __name__== "__main__":

    input_state = [[1, 6, 2, 3], [9,5, 7, 4], [0, 10, 11, 8] , [13, 14, 15, 12]]
    goal_state = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]] 


    queue = deque()
    queue.append(input_state)

    visited_states = []

    t = time.time()

    while(1):

        current_state = queue.popleft()
        print(current_state, end = '\n')
        if current_state == goal_state:
            print("Goal Found")
            break

        if current_state not in visited_states:
            visited_states.append(current_state)
            pos = pos_blank_tile(current_state)
            children = generate_children(pos, current_state) 

            for child in children:
                queue.append(child)

    print(time.time()-t)
