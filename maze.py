def load_maze(file_name):
    maze = []
    with open(file_name, 'r') as file:
        rows, columns = map(int, file.readline().split())
        
        for _ in range(rows):
            line = list(file.readline().strip())
            
            if len(line) != columns:
                print("ERROR: incorrect line length")
            
            maze.append(line)
        
        if len(maze) != rows:
            print("ERROR: incorrect number of rows")
    
    return maze, rows, columns


def check_maze(maze, rows, columns):
  entry = None
  exits = []
  
  for i in range (rows):
    for j in range(columns):
      if maze[i][j] == "#":
        if entry is not None:
          print("ERROR: more than one entry")
          return None, None
        entry = (i, j)
      elif maze[i][j] == "$":
        exits.append((i, j))
      elif maze[i][j] not in ["x", "."]:
        print("ERROR: invalid character")
        return None, None

  if entry is None:
    print("ERROR: no entry")
    return None, None
  if len(exits) < 1:
    print("ERROR: no exit")
    return None, None
  
  return entry, exits


maze = load_maze("maze.txt")
print(check_maze(maze[0], maze[1], maze[2]))