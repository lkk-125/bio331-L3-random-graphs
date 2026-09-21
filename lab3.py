# L3: Random Graph Models
import random
from pyvis.network import Network

def main():
    """
    Main function. Takes no inputs and returns nothing.
    """
    ## CALL your functions here.
    test = []
    testlabels = ['ER_test.html', 'BA_test100.html', 'BA_test50.html', 'WS_test.html']
    test.append(gen_ER(25, 100))
    test.append(gen_BA(3, 1, 100))
    test.append(gen_BA(3, 2, 50))
    test.append(gen_WS(25, 5, 0.5))
    for i in range(len(test)):
        viz_graph(test[i], testlabels[i])
    
    return

## WRITE your own function definitions here.

def gen_ER(n, m):
    nodes = []
    edges = []
    for i in range(n):
        nodes.append(str(i+1))
    while len(edges) < m:
        u = random.choice(nodes)
        v = u
        while v == u:
            v = random.choice(nodes)
        if not ([u, v] in edges or [v, u] in edges):
            edges.append([u, v])
    return edges 

def gen_BA(n, m, t):
    nodes = ['0']
    edges = []
    for i in range(n-1):
        nodes.append(str(i+1))
        edges.append([str(i), str(i+1)])
    for i in range(t):
        bag = []
        for node in nodes: #this for loop calculates degree - getDeg
            d = 0
            for edge in edges:
                if node in edge:  
                    d += 1
            for j in range(d): # this loop creates a "bag" of node duplicates with proportions equal to their degree      
                bag.append(node)              
        temp = len(nodes)
        v = str(temp)
        nodes.append(v)
        for j in range(m): 
            u = random.choice(bag)
            while ([u, v] in edges or [v, u] in edges):
                u = random.choice(bag)
            edges.append([u, v])
    return edges  

def gen_WS(n, k, pr):
    nodes = ['0']
    edges = []

    hd = round(k/2) #half average degree
    #initial graph
    for i in range(n-1): #make a line of nodes of length n
        nodes.append(str(i+1))
        edges.append([str(i), str(i+1)])
    if n != 2: #close the loop
        edges.append(['0', str(n-1)])
    for node in nodes: #make
        for i in range(hd-1):
            to = str((int(node)+2+i)%(len(nodes)))
            if not ([node, to] in edges or [to, node] in edges):
                edges.append([node, to])
    #rewire
    for u,v in edges:
        r = random.random()
        if r < pr:
            edges.remove([u,v])
            w = random.choice(nodes)
            while ([u, w] in edges or [w, u] in edges):
                w = random.choice(nodes)
            edges.append([u, w]) 

    return edges        

def viz_graph(edges,outfile):
    """
    Visualize a graph and write it to an HTML file.
    :param: nodes - list or set of nodes
    :param: edges - list of 2-element lists.
    :param: outfile - string outfile that ends in '.html'
    :returns: None
    """
    
    # Refer to Lab 1 for instructions about visualizing a graph.
    G = Network() # create graph
    nodes = []
    i = 0
    for u,v in edges: # add nodes an edges per edge without duplicates
        if u not in nodes:
            nodes.append(u)
            G.add_node(u,label=u,color='#ace3a8',shape='diamond')
        if v not in nodes:
            nodes.append(v)
            G.add_node(v,label=v,color='#ace3a8',shape='diamond')
        i += 1
        G.add_edge(u,v,title="Order: " + str(i))

    G.toggle_physics(True) 
    G.show_buttons(filter_=['physics'])

    G.write_html(outfile)
    print('Saved file as',outfile)

    return

# keep this at the bottom of the file.
if __name__ == '__main__':
    main()
