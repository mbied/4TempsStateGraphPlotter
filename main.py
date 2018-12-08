import json
import pygraphviz as pgv
import networkx as nx
import matplotlib.pyplot as plt


if __name__ == "__main__":
    # the data is not included in the repository, please ask Marie-Morgane (retroguidage.fr)
    jason_data = './data/passes.json'

    with open(jason_data, 'r') as f:
        passes_dict = json.load(f)

    #https://stackoverflow.com/questions/17947027/open-dot-formatted-graph-from-python
    #https://networkx.github.io/documentation/latest/reference/drawing.html


    G2 = pgv.AGraph(strict='False', overlap='False', directed="True")

    label_dict={0:'DD', 1:'GD', 2:'DDGG', 3:'GDDG', 4:'Position fermée', 5:'Lâché'}

    G = nx.Graph()
    pos = nx.spring_layout(G)

    for idx in range(len(passes_dict['nodes'])):
        id = passes_dict['nodes'][idx]['id'] #unfortunatly idx and id is not always identical
        label = passes_dict['nodes'][idx]['attributes']['name']
        G.add_node(id)
        G2.add_node(id, label=label_dict[idx])
        #label_dict[idx] = label

    for idx in range(len(passes_dict['edges'])):
        source = passes_dict['edges'][idx]['source']
        target = passes_dict['edges'][idx]['target']
        edge_label = passes_dict['edges'][idx]['label']
        G.add_edge(source, target)
        G2.add_edge(source, target, label=edge_label)


    G2.layout()
    G2.draw('file.png')


    label_dict={0:'DD', 1:'GD', 2:'DDGG', 3:'GDDG', 4:'Position fermée', 5:'Lâché'}
    edge_labels_dict = {}
    #edge_labels_dict['0'] = 'test'
    #edge_labels_dict['1'] = 'test2'

    #nx.draw_networkx_labels(G, pos, labels, font_size= 16)
    #nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels_dict)
    nx.draw(G, labels=label_dict, with_labels=True)
   # nx.draw_networkx_edge_labels(G)
    plt.show()
    #print(label_dict)
    print("success")