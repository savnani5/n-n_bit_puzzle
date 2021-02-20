import time
import copy
from collections import deque
import numpy as np

# String is fast in comparion but searching and conversion from list to string will be time consuming
# Cannot implement binay search because we have to search in unsorted array

class Node: 

    def __init__(self, n, state, parent):
        self.n = n                              # n is the 1D dimension of the puzzle for eg: for a 4*4 puzzle, n will be 4
        self.state = state                      # state is the current state of the puzzle
        self.parent = parent                    # parent attribute stores the parent node of current node

    def __repr__(self):
        return str(self.state)                  # This method returns the state information of the node

    def up(self, pos):
        x,y = pos[0], pos[1]
        if x != 0:
            up_node = Node(self.n, copy.deepcopy(self.state), Node(self.n, self.state, self.parent))
            up_node.state[x][y], up_node.state[x-1][y] = up_node.state[x-1][y], up_node.state[x][y]
            return up_node
        return None

    def down(self, pos):
        x,y = pos[0], pos[1]
        if x != (self.n - 1):
            down_node = Node(self.n, copy.deepcopy(self.state), Node(self.n, self.state, self.parent))
            down_node.state[x][y], down_node.state[x+1][y] = down_node.state[x+1][y], down_node.state[x][y]
            return down_node
        return None

    def left(self, pos):
        x,y = pos[0], pos[1]
        if y != 0:
            left_node = Node(self.n, copy.deepcopy(self.state), Node(self.n, self.state, self.parent))
            left_node.state[x][y], left_node.state[x][y-1] = left_node.state[x][y-1], left_node.state[x][y]
            return left_node
        return None

    def right(self, pos):
        x,y = pos[0], pos[1]
        if y != (self.n - 1):
            right_node = Node(self.n, copy.deepcopy(self.state), Node(self.n, self.state, self.parent))
            right_node.state[x][y], right_node.state[x][y+1] = right_node.state[x][y+1], right_node.state[x][y]
            return right_node
        return None

    def pos_blank_tile(self):
        for i in range(len(self.state)):
            for j in range(len(self.state)):
                if self.state[i][j] == 0:
                    return (i,j)


    def generate_children(self, pos):
        
        children = []
        up_move = self.up(pos)
        down_move = self.down(pos)
        left_move = self.left(pos)
        right_move = self.right(pos)
        
        if up_move:
            children.append(up_move) 
        if down_move:
            children.append(down_move)
        if left_move:
            children.append(left_move)
        if right_move:
            children.ap pend(right_move)
        
        return children


if __name__== "__main__":

    input_state = [[1, 6, 2, 3], [9,5, 7, 4], [0, 10, 11, 8] , [13, 14, 15, 12]]
    goal_state = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]] 

    input_node = Node(4, input_state, None)
    queue = deque()
    queue.append(input_node)

    visited_states = []
    t = time.time()

    while(1):

        current_node = queue.popleft()
        print(current_node, end = '\n')
        if current_node.state == goal_state:
            print("Goal Found\n")
            print("Shortest path:\n")
            print(current_node)
            while(current_node.state != input_state):
                current_node = current_node.parent
                print(current_node)
            break

        if current_node.state not in visited_states:
            visited_states.append(current_node.state)
            pos = current_node.pos_blank_tile()
            children = current_node.generate_children(pos) 

            for child in children:
                queue.append(child)

    print(time.time()-t)
