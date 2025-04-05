import pydot

# Create a new directed graph
graph = pydot.Dot(graph_type='digraph')

# Define the nodes
nodes = {
    "Typhoon": "台风灾害",
    "Construction Sites Waterlogged": "施工现场积水",
    "Flooding": "洪水",
    "Geological Disasters": "地质灾害",
    "Waterlogging": "内涝",
    "Houses Flooded and Collapsed": "房屋淹没倒塌",
    "Dam Break": "大坝决堤",
    "Consequences 1": "人员伤亡",
    "Consequences 2": "经济损失",
    "Consequences 3": "交通中断",
    "Consequences 4": "供电中断",
    "Consequences 5": "供水中断",
    "Consequences 6": "通信中断"
}

# Add nodes to the graph
for node in nodes:
    graph.add_node(pydot.Node(node, label=nodes[node]))

# Define the edges
edges = [
    ("Typhoon", "Construction Sites Waterlogged"),
    ("Typhoon", "Flooding"),
    ("Typhoon", "Geological Disasters"),
    ("Typhoon", "Waterlogging"),
    ("Construction Sites Waterlogged", "Consequences 1"),
    ("Construction Sites Waterlogged", "Consequences 2"),
    ("Flooding", "Houses Flooded and Collapsed"),
    ("Flooding", "Consequences 3"),
    ("Flooding", "Consequences 4"),
    ("Flooding", "Consequences 5"),
    ("Geological Disasters", "Dam Break"),
    ("Geological Disasters", "Consequences 6"),
    ("Waterlogging", "Consequences 1"),
    ("Waterlogging", "Consequences 2"),
    ("Waterlogging", "Consequences 3"),
    ("Waterlogging", "Consequences 4"),
    ("Waterlogging", "Consequences 5")
]

# Add edges to the graph
for edge in edges:
    graph.add_edge(pydot.Edge(edge[0], edge[1]))

# Save the graph to a file and display it
graph.write_png('bayesian_network.png')
print("Bayesian network graph saved as 'bayesian_network.png'")