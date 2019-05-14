import networkx as nx

import matplotlib.pyplot as plt
from matplotlib.patches import ArrowStyle

from telethon import TelegramClient


def graph_me_up_senpai(G, kurasu):
    # recursion is bae
    G.add_node(kurasu)
    for basedesu in kurasu.__bases__:
        G.add_node(basedesu)
        G.add_edge(kurasu, basedesu)
        graph_me_up_senpai(G, basedesu)


G = nx.DiGraph()
graph_me_up_senpai(G, TelegramClient)

# idk how to name the nodes when making them
nx.relabel_nodes(
    G,
    {node: node.__name__ for node in G},
    copy=False
)

# draw graph (excuse the poor rice)
nx.draw(
    G,
    with_labels=True,
    font_weight='bold',
    node_size=100,
    font_size=6,
    width=0.3,
    font_family='monospace',
    edge_color='#808080',
    node_color='#8fd2ff',
    arrowstyle=ArrowStyle('Fancy', head_length=.3, head_width=.3, tail_width=.01)
)
plt.savefig('graphnami.png', dpi=300)