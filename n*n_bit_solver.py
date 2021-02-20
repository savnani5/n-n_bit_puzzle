import time
import copy
from collections import deque
import numpy as np

#____________________________Optimization results___________________________
# The deque class from collections module is used as the data structure to store the nodes because it is faster compared to the python's inbuilt list.
# String is fast in comparion but searching and conversion from list to string is time consuming(experimentally verified)
# Cannot implement binay search to improve searching speeds because we have to search in an unsorted array.

class Node:
    """ This class stores the attributes(like puzzle size, state and parent node) and methods(like up, down actions, generate children etc.) 
        for the Node in the puzzle tree. Also, it can be used to solve any general n*n bit puzzle""" 

    def __init__(self, n, state, parent):
        self.n = n                              # n is the 1D dimension of the puzzle for eg: for a 4*4 puzzle, n will be 4
        self.state = state                      # state is the current state of the puzzle
        self.parent = parent                    # parent attribute stores the parent node of current node

    def __repr__(self):
        return str(self.state)                  # This method returns the state information of the node

    def up(self, pos):
        # This method performs the up action on the current node
        x,y = pos[0], pos[1]
        if x != 0:
            up_node = Node(self.n, copy.deepcopy(self.state), Node(self.n, self.state, self.parent))
            up_node.state[x][y], up_node.state[x-1][y] = up_node.state[x-1][y], up_node.state[x][y]
            return up_node
        return None

    def down(self, pos):
        # This method performs the down action on the current node
        x,y = pos[0], pos[1]
        if x != (self.n - 1):
            down_node = Node(self.n, copy.deepcopy(self.state), Node(self.n, self.state, self.parent))
            down_node.state[x][y], down_node.state[x+1][y] = down_node.state[x+1][y], down_node.state[x][y]
            return down_node
        return None

    def left(self, pos):
        # This method performs the left action on the current node
        x,y = pos[0], pos[1]
        if y != 0:
            left_node = Node(self.n, copy.deepcopy(self.state), Node(self.n, self.state, self.parent))
            left_node.state[x][y], left_node.state[x][y-1] = left_node.state[x][y-1], left_node.state[x][y]
            return left_node
        return None

    def right(self, pos):
        # This method performs the right action on the current node
        x,y = pos[0], pos[1]
        if y != (self.n - 1):
            right_node = Node(self.n, copy.deepcopy(self.state), Node(self.n, self.state, self.parent))
            right_node.state[x][y], right_node.state[x][y+1] = right_node.state[x][y+1], right_node.state[x][y]
            return right_node
        return None

    def pos_blank_tile(self):
        # This method is used to find the position of the blank tile in the puzzle
        for i in range(self.n):
            for j in range(self.n):
                if self.state[i][j] == 0:
                    return (i,j)


    def generate_children(self, pos):
        # This method applies the actions functions to generate the children nodes of the current node 
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
            children.append(right_move)
        
        return children
    


if __name__== "__main__":


    input_test_cases = [[[1, 2, 3, 4],[ 5, 6,0, 8], [9, 10, 7, 12] , [13, 14, 11, 15]], 
                        [[1, 0, 3, 4],[ 5, 2, 7, 8], [9, 6, 10, 11] , [13, 14, 15, 12]], 
                        [[0, 2, 3, 4],[ 1,5, 7, 8], [9, 6, 11, 12] , [13, 10, 14, 15]], 
                        [[5, 1, 2, 3],[0,6, 7, 4], [9, 10, 11, 8] , [13, 14, 15, 12]], 
                        [[1, 6, 2, 3], [9,5, 7, 4], [0, 10, 11, 8] , [13, 14, 15, 12]]]  # Input 
    
    goal_state = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]  # Output  

    for input_state in input_test_cases:
        input_node = Node(4, input_state, None)
        queue = deque()                             # Using python's inbuilt queue becaus it performs faster enqueue and dequeue operations compared to  a list
        queue.append(input_node)

        visited_states = []
        t = time.time()

        with open(f"nodePath_{input_test_cases.index(input_state) + 1}.txt", "w") as text_file:
            
            # Breadth First Search(BFS) Implementation
            while(1):
                current_node = queue.popleft()
                text_file.write(str(current_node.state)+ "\n")
                # print(current_node, end = '\n')
                
                if current_node.state == goal_state:
                    print("Goal Found\n")
                    print("Shortest path:\n")
                    print(current_node)
            
            # Backtracking the parent node to find the shortest path
                    while(current_node.state != input_state):
                        current_node = current_node.parent
                        print(current_node)
                    break
            #____________________________________________________

                if current_node.state not in visited_states:
                    visited_states.append(current_node.state)
                    pos = current_node.pos_blank_tile()
                    children = current_node.generate_children(pos) 

                    for child in children:
                        queue.append(child)

        print("Execution time", time.time()-t)
