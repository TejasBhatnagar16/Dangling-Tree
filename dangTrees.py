class Node: 
    def __init__(self, tag, weight):
        self.neighbours = []
        self.weight = weight
        self.tag = tag
        self.degree = 0
        self.isLeaf = True 
        self.isEndNode = False

class Path:
    def __init__(self, startingLeaf): 
        self.starLeaf = startingLeaf
        self.cost = 0

def solver(fpath): 
    with open(fpath, 'r', encoding='utf-8') as f:
        nodes = []
        data = list(map(str.strip, f.readlines()))
        totalNodes, root = data[0].split()
        keys = data[1].split()
        for i in range(len(keys)):
            nodes.append(Node(i, keys[i]))
        for i in data[2:]:
            node1, node2 = i.split()              
            node1, node2 = int(node1), int(node2)  
            nodes[node1].neighbours.append(node2)   # append both the nodes to each others neighbours lists 
            nodes[node2].neighbours.append(node1)
            nodes[node1].degree += 1                # increament their degrees 
            nodes[node2].degree += 1 
            if nodes[node1].degree >= 2:            # set isLeaf to false if the conditions are violated 
                nodes[node1].isLeaf = False
                if nodes[node1].degree == 3:        # set isEndNode to True if the degree is 3 
                    nodes[node1].isEndNode = True 
            if nodes[node2].degree >= 2:
                nodes[node2].isLeaf = False
                if nodes[node2].degree == 3:
                    nodes[node2].isEndNode = True
        maxPath = None 
        minPath = None
        for leaf in nodes:                          # traversing through the tree looking for a leaf and then i 
            if leaf.isLeaf:                         # move up looking for a dangling tree path  
                currPath = Path(leaf.tag)
                lastVisitedNode = leaf.tag 
                currNode = leaf
                while not currNode.isEndNode:
                    currPath.cost += int(currNode.weight)
                    for i in currNode.neighbours:
                        if i != lastVisitedNode:
                            lastVisitedNode = int(currNode.tag)
                            currNode = nodes[i]
                            break
                if maxPath == None:                 # change the max and min path 
                    maxPath = currPath
                elif maxPath.cost < currPath.cost:   
                    maxPath = currPath
                if minPath == None: 
                    minPath = currPath
                elif minPath.cost > currPath.cost:
                    minPath = currPath 
        return [str(minPath.cost) + " " + str(maxPath.cost)]
                

# checking with the dataset 

for i in range(1, 10):
    input_file = "alg\dangTrees\dangTreeData\pub" + \
        '0' + str(i) + '.in'
    my_ans = solver(input_file)
    ouput_file = 'alg\dangTrees\dangTreeData\pub' + \
        '0' + str(i) + '.out'
    with open(ouput_file, 'r', encoding='utf-8') as out:
        ans = out.readlines()
        ans = list(map(str.strip, ans))
    print(my_ans == ans)
    
my_ans = solver('alg\dangTrees\dangTreeData\pub10.in')
with open('alg\dangTrees\dangTreeData\pub10.out', 'r', encoding='utf-8') as f:
    ans = f.readlines()
    ans = list(map(str.strip, ans))
    print(my_ans == ans) 




                    

                    
                    


        

            

            

        
           







