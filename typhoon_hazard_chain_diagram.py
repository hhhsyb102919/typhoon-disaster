import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from matplotlib.patches import FancyArrowPatch
import matplotlib.patheffects as PathEffects

# Create a figure with a light background
plt.figure(figsize=(16, 12), facecolor='white')
plt.rcParams.update({'font.size': 12})

# Create directed graph
G = nx.DiGraph()

# Define the node categories and their members
categories = {
    "Typhoon Properties": [
        "H1: Typhoon class",
        "H2: Max wind speed",
        "H3: Min pressure",
        "H4: Typhoon track",
        "H7: Storm surge height",
        "H6: Rainfall"
    ],
    "Environmental Factors": [
        "H9: Sea Surface Temperature",
        "H10: Wind shear",
        "H11: Soil moisture",
        "H12: Tidal state"
    ],
    "Direct Hazards": [
        "E1: Storm surge inundation",
        "E2: Strong wind damage",
        "E3: Short-term heavy rainfall",
        "E4: River water level",
        "E5: Landslides/mudslides"
    ],
    "Infrastructure": [
        "O1: Low-lying residential areas",
        "O2: Coastal dykes",
        "O3: Urban drainage",
        "O5: Old buildings"
    ],
    "Indirect Events": [
        "E8: Power facility damage",
        "E9: Communication disruption",
        "E10: Underground space flooding",
        "E13: Water supply disruption"
    ],
    "Social Systems": [
        "O8: Hospital capacity",
        "O11: Social media influence"
    ],
    "Preventive Measures": [
        "M1: Flood water release",
        "M3: Population transfer",
        "M4: Structure reinforcement"
    ],
    "Rescue Measures": [
        "M6: Assault boats deployment",
        "M8: Medical team response",
        "M9: Official information release" 
    ],
    "Consequences": [
        "C1: Direct fatalities",
        "C2: Injured persons",
        "C4: Psychological trauma",
        "C5: Infrastructure repair costs",
        "C10: Government credibility"
    ]
}

# Add nodes to the graph
for category, nodes in categories.items():
    for node in nodes:
        G.add_node(node, category=category)

# Define key edges (connections between nodes)
edges = [
    # Environmental Factors to Typhoon Properties
    ("H9: Sea Surface Temperature", "H1: Typhoon class"),
    ("H9: Sea Surface Temperature", "H2: Max wind speed"),
    ("H10: Wind shear", "H4: Typhoon track"),
    
    # Typhoon Properties to Direct Hazards
    ("H1: Typhoon class", "E1: Storm surge inundation"),
    ("H2: Max wind speed", "E2: Strong wind damage"),
    ("H6: Rainfall", "E3: Short-term heavy rainfall"),
    ("H6: Rainfall", "E4: River water level"),
    ("H6: Rainfall", "E5: Landslides/mudslides"),
    ("H7: Storm surge height", "E1: Storm surge inundation"),
    
    # Environmental Factors to Direct Hazards
    ("H11: Soil moisture", "E5: Landslides/mudslides"),
    ("H12: Tidal state", "E1: Storm surge inundation"),
    
    # Infrastructure influence on Hazards
    ("O1: Low-lying residential areas", "E1: Storm surge inundation"),
    ("O2: Coastal dykes", "E1: Storm surge inundation"),
    ("O3: Urban drainage", "E3: Short-term heavy rainfall"),
    ("O5: Old buildings", "E2: Strong wind damage"),
    
    # Direct Hazards to Indirect Events
    ("E1: Storm surge inundation", "E8: Power facility damage"),
    ("E1: Storm surge inundation", "E10: Underground space flooding"),
    ("E2: Strong wind damage", "E8: Power facility damage"),
    ("E2: Strong wind damage", "E9: Communication disruption"),
    ("E3: Short-term heavy rainfall", "E10: Underground space flooding"),
    ("E4: River water level", "E13: Water supply disruption"),
    ("E5: Landslides/mudslides", "E13: Water supply disruption"),
    
    # Preventive Measures influence on Hazards
    ("M1: Flood water release", "E4: River water level"),
    ("M3: Population transfer", "C1: Direct fatalities"),
    ("M4: Structure reinforcement", "E2: Strong wind damage"),
    
    # Indirect Events to Consequences
    ("E8: Power facility damage", "C5: Infrastructure repair costs"),
    ("E9: Communication disruption", "C10: Government credibility"),
    ("E10: Underground space flooding", "C5: Infrastructure repair costs"),
    
    # Social Systems influence on Indirect Events and Consequences
    ("O8: Hospital capacity", "C2: Injured persons"),
    ("O11: Social media influence", "C4: Psychological trauma"),
    ("O11: Social media influence", "C10: Government credibility"),
    
    # Rescue Measures influence on Consequences
    ("M6: Assault boats deployment", "C1: Direct fatalities"),
    ("M8: Medical team response", "C2: Injured persons"),
    ("M9: Official information release", "C4: Psychological trauma"),
    ("M9: Official information release", "C10: Government credibility"),
    
    # Direct Hazards to Consequences
    ("E1: Storm surge inundation", "C1: Direct fatalities"),
    ("E2: Strong wind damage", "C1: Direct fatalities"),
    ("E2: Strong wind damage", "C2: Injured persons"),
    ("E5: Landslides/mudslides", "C1: Direct fatalities"),
    ("E5: Landslides/mudslides", "C2: Injured persons"),
]

# Add edges to the graph
G.add_edges_from(edges)

# Define positions for each category (vertical layers)
pos = {}
categories_list = list(categories.keys())
num_categories = len(categories_list)
vertical_spacing = 1.0

# Define position mapping by category - adjust spacing to create a clearer layout
category_positions = {
    "Environmental Factors": (0.2, 9),
    "Typhoon Properties": (0.6, 8),
    "Infrastructure": (0.15, 6.5),
    "Preventive Measures": (0.85, 6.5),
    "Direct Hazards": (0.5, 5),
    "Indirect Events": (0.5, 3.5),
    "Social Systems": (0.8, 3.5),
    "Rescue Measures": (0.7, 2),
    "Consequences": (0.5, 0.5)
}

# Position nodes within each category
for category, (x_center, y_pos) in category_positions.items():
    nodes = categories[category]
    num_nodes = len(nodes)
    
    if num_nodes == 1:
        pos[nodes[0]] = (x_center, y_pos)
    else:
        width = 0.2 if num_nodes <= 3 else 0.4
        for i, node in enumerate(nodes):
            x = x_center - width/2 + width * i / (num_nodes - 1)
            pos[node] = (x, y_pos)

# Define node colors by category
color_map = {
    "Environmental Factors": "#A8D08D",      # Light green
    "Typhoon Properties": "#9BC4E2",         # Light blue
    "Direct Hazards": "#F8CECC",             # Light red
    "Infrastructure": "#F5F5A7",             # Light yellow
    "Indirect Events": "#FFB570",            # Light orange
    "Social Systems": "#E6C2A2",             # Light beige
    "Preventive Measures": "#D9E6F5",        # Very light blue
    "Rescue Measures": "#B0C4DE",            # Light steel blue
    "Consequences": "#E0BBE4"                # Light purple
}

# Create node colors list based on category
node_colors = [color_map[G.nodes[node]['category']] for node in G.nodes()]

# Define node shapes by category
node_shapes = {
    "Environmental Factors": "o",           # Circle
    "Typhoon Properties": "o",              # Circle
    "Direct Hazards": "s",                  # Square
    "Infrastructure": "s",                  # Square
    "Indirect Events": "s",                 # Square
    "Social Systems": "s",                  # Square
    "Preventive Measures": "^",             # Triangle up
    "Rescue Measures": "^",                 # Triangle up
    "Consequences": "d"                     # Diamond
}

# Draw nodes by category with appropriate shapes
for category, shape in node_shapes.items():
    nodelist = [node for node in G.nodes() if G.nodes[node]['category'] == category]
    nx.draw_networkx_nodes(
        G, pos, 
        nodelist=nodelist,
        node_color=[color_map[category]] * len(nodelist),
        node_size=2500,
        node_shape=shape,
        alpha=0.9,
        edgecolors='black',
        linewidths=1
    )

# Draw edges with slight curves and improved visibility
edge_list = list(G.edges())
for u, v in edge_list:
    arrow = FancyArrowPatch(
        pos[u], pos[v],
        connectionstyle='arc3,rad=0.1',
        arrowstyle='-|>',
        mutation_scale=15,
        linewidth=1.5,
        color='gray',
        alpha=0.7
    )
    plt.gca().add_patch(arrow)

# Draw node labels with improved visibility
for node, (x, y) in pos.items():
    # Shorten the node label for display
    short_label = node.split(':')[0] + ': ' + ' '.join(node.split(':')[1].strip().split()[:2])
    if len(short_label) > 15:
        short_label = short_label[:15] + '...'
    
    text = plt.text(
        x, y, short_label,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=9,
        fontweight='bold',
        bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', boxstyle='round,pad=0.2')
    )
    # Add outline effect for better visibility
    text.set_path_effects([PathEffects.withStroke(linewidth=3, foreground='white')])

# Create legend for categories
legend_elements = []
for category, color in color_map.items():
    shape = node_shapes[category]
    if shape == 'o':
        legend_elements.append(plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color,
                                         markersize=10, label=category))
    elif shape == 's':
        legend_elements.append(plt.Line2D([0], [0], marker='s', color='w', markerfacecolor=color,
                                         markersize=10, label=category))
    elif shape == '^':
        legend_elements.append(plt.Line2D([0], [0], marker='^', color='w', markerfacecolor=color,
                                         markersize=10, label=category))
    elif shape == 'd':
        legend_elements.append(plt.Line2D([0], [0], marker='d', color='w', markerfacecolor=color,
                                         markersize=10, label=category))

# Add the legend
plt.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, 1.05),
          ncol=3, fontsize=10)

# Add category labels to the left side of each group
for category, (x_center, y_pos) in category_positions.items():
    plt.text(
        0.02, y_pos, 
        category, 
        fontsize=12, 
        fontweight='bold',
        verticalalignment='center',
        horizontalalignment='left',
        bbox=dict(facecolor='white', alpha=0.7, edgecolor=color_map[category], boxstyle='round,pad=0.2')
    )

plt.title('Typhoon Disaster Chain Bayesian Network', fontsize=16, pad=20)
plt.axis('off')
plt.tight_layout()
plt.savefig('typhoon_disaster_chain_diagram.png', dpi=300, bbox_inches='tight')
plt.show()