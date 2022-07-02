#Directed Unweighted Graph

adj_list ={}
mylist=[]
def add_node(node):
    if node not in mylist:
        mylist.append(node)
    else:
        print("Node", node, "already exists!")

def add_edge(node1, node2):
        temp =[]
        if node1 in mylist and node2 in mylist:
            if node1 not in adj_list:
                temp.append(node2)
                adj_list[node1] =temp 

            elif node1 in adj_list:
                temp.extend(adj_list[node1])
                temp.append(node2)
                adj_list[node1] =temp

            else:
                print("Node Don't exsits") 

def graph():
    for node in adj_list:
        print(node, " ----->", [i for i in adj_list[node]])

# Adding nodes
add_node(0)          
add_node(1)          
add_node(2)          
add_node(3)          
add_node(4)
# Ading adges 
add_edge(0,1)
add_edge(1,2)
add_edge(2,3)
add_edge(3,4)
add_edge(4,0)

# printing the grapg
graph()

# Printing the adjacency List
print(adj_list)

          

