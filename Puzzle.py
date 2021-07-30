# import sys
#
#
# def Prims(G):
#     V = len(G)
#
#     infinity = sys.maxsize
#
#     result = []
#     visited = [0 for i in range(len(G))]
#     visited[0] = True
#
#     edges = 0
#
#     while edges < V - 1:
#
#         minimum = infinity
#         x = 0
#         y = 0
#
#         # find (a,b) where a is visited and b is not AND edge(A,B) is min
#         for i in range(len(G)):
#             if visited[i]:
#                 for j in range(len(G[0])):
#                     if not visited[j] and G[i][j]:
#                         if minimum > G[i][j]:
#                             minimum = G[i][j]
#                             x = i
#                             y = j
#         result.append((x, y))
#         visited[y] = True
#         edges += 1
#
#     return result
#
#
# G = [[0, 9, 75, 0, 0],
#      [9, 0, 95, 19, 42],
#      [75, 95, 0, 51, 66],
#      [0, 19, 51, 0, 31],
#      [0, 42, 66, 31, 0]]
#
# print(Prims(G))


def solve_puzzle(Board, Source, Desination):
    # initialize board and visited list
    visisted = [[0 for i in range(len(Board))] for j in range(len(Board[0]))]

    source_x = Source[0] - 1
    source_y = Source[1] - 1
    # visisted[source_x][source_y] = True

    dest_x = Desination[0] - 1
    dest_y = Desination[1] - 1

    # implement a BFS to find shorest path to destination

    # initialize empty stack
    queue = []
    traveled_list = []
    queue.append(Source)

    while len(queue) > 0:
        current = queue.pop(0)
        current_x = current[0] - 1
        current_y = current[1] - 1
        if visisted[current_x][current_y]:
            continue
        visisted[current_x][current_y] = True
        if current == (dest_x, dest_y):
            traveled_list.append(current)
            break

        successors = get_successors(board, current)
        counter = 0
        traveled_list.append(current)

        for square in successors:
            square_x = square[0]
            square_y = square[1]
            if square_x < 0 or square_y < 0:
                continue
            if not visisted[square_x][square_y]:
                queue.append(square)
            counter += 1


    return traveled_list


def get_successors(board, current):
    current_x = current[0] - 1
    current_y = current[1] - 1

    next_move_list = []

    # up
    if board[current_x - 1][current_y] == '-' and (current_x - 1 >= 0):

        next_move_list.append((current_x - 1, current_y))


    # down
    if board[current_x + 1][current_y] == '-' and (current_x + 1 >= 0):
        next_move_list.append((current_x + 1, current_y))

    # left
    if board[current_x][current_y - 1] == '-' and (current_y - 1 >= 0):
        next_move_list.append((current_x, current_y - 1))

    # right
    if board[current_x][current_y + 1] == '-' and (current_y + 1 >= 0):
        next_move_list.append((current_x, current_y + 1))

    return next_move_list









board = [['-', '-', '-', '-', '-'],
         ['-', '-', '#', '-', '-'],
         ['-', '-', '-', '-', '-'],
         ['#', '-', '#', '#', '-'],
         ['-', '#', '-', '-', '-']]

print(solve_puzzle(board, (1, 1), (1, 2)))


def dfs(self, v_start, v_end=None) -> []:
    """
    Depth first search that returns a list
    of vertices in the order they were visited during the search.
    If the starting vertex is not in the graph an empty list is returned
    Param v_start: starting search node
    Param v_end: ending search node
    Return: list of traversed nodes in order of visit
    """

    # Starting node is not in the graph
    if v_start not in range(len(self.adj_matrix)):
        return []

    # 1) initialize hash table of vertices
    visited = {}
    matrix = self.adj_matrix
    for vertex in range(len(matrix)):
        visited[vertex] = False

    # initialize empty stack
    stack = []
    traveled_list = []
    stack.append(v_start)

    while len(stack) > 0:
        # pop top element
        top = stack.pop()

        if top == v_end:
            traveled_list.append(top)
            return

        elif top != v_end and not visited[top]:
            # appended traveled list
            traveled_list.append(top)
            # set vertex as visited
            visited[top] = True
            # add each successor of vertex to the stack
            successors = self.adj_matrix[top]

            counter = len(successors)
            for vertex in range(len(successors), 0, -1):
                counter -= 1
                if successors[counter] > 0:
                    stack.append(counter)

    return traveled_list
