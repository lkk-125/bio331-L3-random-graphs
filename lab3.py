# L3: Random Graph Models
import random
from pyvis.network import Network

def main():
    """
    Main function. Takes not inputs and returns nothing.
    """
    ## CALL your functions here.


    return

## WRITE your own function definitions here.




def viz_graph(nodes,edges,outfile):
    """
    Visualize a graph and write it to an HTML file.
    :param: nodes - list or set of nodes
    :param: edges - list of 2-element lists.
    :param: outfile - string outfile that ends in '.html'
    :returns: None
    """
    
    # Refer to Lab 1 for instructions about visualizing a graph.
    G = Network() # create graph
    for n in nodes: # add nodes
        G.add_node(n,label=str(n),color='#ace3a8',shape='diamond')
    for u,v in edges: # add edges
        G.add_edge(u,v) 

    G.toggle_physics(True) 
    G.show_buttons(filter_=['physics'])

    G.write_html(outfile)
    print('Saved file as',outfile)

    return

# keep this at the bottom of the file.
if __name__ == '__main__':
    main()
