import networkx as nx
import matplotlib.pyplot as plt

def plotting_graph(source,des):
    G = nx.Graph()

    # Example edges (you can use your df values)
    edges = [(source, des, 5)]
    G.add_weighted_edges_from(edges)
    pos = nx.spring_layout(G)  # positions for nodes
    plt.figure(figsize=(5, 3))

    # Nodes and edges
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, edge_color='gray')

    # Edge labels (weights)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title("Traffic Network Graph")
    plt.savefig('static/network_graph.png')  # Save the graph as image
    plt.close()