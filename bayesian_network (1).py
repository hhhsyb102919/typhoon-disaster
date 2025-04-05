import pydot

# Create a new directed graph
graph = pydot.Dot(graph_type='digraph')

# Define the nodes
nodes = {
    # Typhoon Ontological Properties
    "H1": "Typhoon Class",
    "H2": "Max Sustained Wind Speed",
    "H3": "Min Pressure at Centre",
    "H4": "Typhoon Track",
    "H5": "Radius of Influence",
    "H6": "Rainfall",
    "H7": "Storm Surge Height",
    "H8": "Typhoon Duration",
    "H9": "Sea Surface Temperature",
    "H10": "Atmospheric Vertical Wind Shear",
    "H11": "Preliminary Soil Moisture",
    "H12": "Tidal State",
    
    # Direct Secondary Hazards
    "E1": "Storm Surge Inundation",
    "E2": "Strong Wind Damage",
    "E3": "Short-term Heavy Rainfall",
    "E4": "River Water Level Exceeds Warning Line",
    "E5": "Landslides/Mudslides",
    "E6": "Seawater Back-up",
    "E7": "Paralysis of Traffic Signalling System",
    
    # Indirect Chain of Events
    "E8": "Damage to Power Facilities",
    "E9": "Disruption of Communication Base Stations",
    "E10": "Water Ingress into Underground Space",
    "E11": "Chemical Plant Leakage",
    "E12": "Overloaded Medical System",
    "E13": "Water Supply Network Rupture",
    "E14": "Waste Disposal System Collapse",
    
    # Infrastructure
    "O1": "Low-lying Residential Areas",
    "O2": "Coastal Dykes",
    "O3": "Urban Drainage Network",
    "O4": "Transportation Hubs",
    "O5": "Old Buildings",
    "O6": "Agricultural Land",
    
    # Social Systems
    "O7": "Emergency Stockpile",
    "O8": "Hospital Emergency Carrying Capacity",
    "O9": "School/Gymnasium",
    "O10": "Fishing/Merchant Vessels",
    "O11": "Social Media Public Opinion Heat",
    
    # Preventive Measures
    "M1": "Early Release of Flood Water",
    "M2": "Traffic Control",
    "M3": "Transfer of People from Hazardous Areas",
    "M4": "Reinforcement of Temporary Structures",
    "M5": "Activation of Emergency Power Supply System",
    
    # Rescue Measures
    "M6": "Deployment of Assault Boats",
    "M7": "Drone Inspection",
    "M8": "Medical Team Mobile Response",
    "M9": "Social Media Disinformation",
    "M10": "Cross-regional Power Support",
    
    # Human Losses
    "C1": "Direct Fatalities",
    "C2": "Injured Persons",
    "C3": "Missing Persons",
    "C4": "Psychological Trauma",
    
    # Economic Losses
    "C5": "Infrastructure Repair Costs",
    "C6": "Agricultural Losses",
    "C7": "Losses from Industrial and Commercial Shutdowns",
    "C8": "Amount of Insurance Claims",
    
    # Social Impact
    "C9": "Post-disaster Reconstruction Cycle",
    "C10": "Change in Government Credibility",
    "C11": "Ecological Recovery Index"
}

# Add nodes to the graph
for node in nodes:
    graph.add_node(pydot.Node(node, label=nodes[node]))

# Define the edges
edges = [
    # Typhoon properties influencing direct secondary hazards
    ("H1", "E1"), ("H1", "E2"), ("H1", "E3"), ("H1", "E4"), ("H1", "E5"), ("H1", "E6"), ("H1", "E7"),
    ("H2", "E1"), ("H2", "E2"), ("H2", "E3"), ("H2", "E4"), ("H2", "E5"), ("H2", "E6"), ("H2", "E7"),
    ("H3", "E1"), ("H3", "E2"), ("H3", "E3"), ("H3", "E4"), ("H3", "E5"), ("H3", "E6"), ("H3", "E7"),
    ("H4", "E1"), ("H4", "E2"), ("H4", "E3"), ("H4", "E4"), ("H4", "E5"), ("H4", "E6"), ("H4", "E7"),
    ("H5", "E1"), ("H5", "E2"), ("H5", "E3"), ("H5", "E4"), ("H5", "E5"), ("H5", "E6"), ("H5", "E7"),
    ("H6", "E1"), ("H6", "E2"), ("H6", "E3"), ("H6", "E4"), ("H6", "E5"), ("H6", "E6"), ("H6", "E7"),
    ("H7", "E1"), ("H7", "E2"), ("H7", "E3"), ("H7", "E4"), ("H7", "E5"), ("H7", "E6"), ("H7", "E7"),
    ("H8", "E1"), ("H8", "E2"), ("H8", "E3"), ("H8", "E4"), ("H8", "E5"), ("H8", "E6"), ("H8", "E7"),
    ("H9", "H1"), ("H10", "H1"), ("H11", "H1"), ("H12", "H1"),

    # Direct hazards leading to indirect events
    ("E1", "E8"), ("E1", "E9"), ("E1", "E10"), ("E1", "E11"), ("E1", "E12"), ("E1", "E13"), ("E1", "E14"),
    ("E2", "E8"), ("E2", "E9"), ("E2", "E10"), ("E2", "E11"), ("E2", "E12"), ("E2", "E13"), ("E2", "E14"),
    ("E3", "E8"), ("E3", "E9"), ("E3", "E10"), ("E3", "E11"), ("E3", "E12"), ("E3", "E13"), ("E3", "E14"),
    ("E4", "E8"), ("E4", "E9"), ("E4", "E10"), ("E4", "E11"), ("E4", "E12"), ("E4", "E13"), ("E4", "E14"),
    ("E5", "E8"), ("E5", "E9"), ("E5", "E10"), ("E5", "E11"), ("E5", "E12"), ("E5", "E13"), ("E5", "E14"),
    ("E6", "E8"), ("E6", "E9"), ("E6", "E10"), ("E6", "E11"), ("E6", "E12"), ("E6", "E13"), ("E6", "E14"),
    ("E7", "E8"), ("E7", "E9"), ("E7", "E10"), ("E7", "E11"), ("E7", "E12"), ("E7", "E13"), ("E7", "E14"),

    # Indirect events leading to losses and impacts
    ("E8", "C1"), ("E8", "C2"), ("E8", "C3"), ("E8", "C4"), ("E8", "C5"), ("E8", "C6"), ("E8", "C7"), ("E8", "C8"), ("E8", "C9"), ("E8", "C10"), ("E8", "C11"),
    ("E9", "C1"), ("E9", "C2"), ("E9", "C3"), ("E9", "C4"), ("E9", "C5"), ("E9", "C6"), ("E9", "C7"), ("E9", "C8"), ("E9", "C9"), ("E9", "C10"), ("E9", "C11"),
    ("E10", "C1"), ("E10", "C2"), ("E10", "C3"), ("E10", "C4"), ("E10", "C5"), ("E10", "C6"), ("E10", "C7"), ("E10", "C8"), ("E10", "C9"), ("E10", "C10"), ("E10", "C11"),
    ("E11", "C1"), ("E11", "C2"), ("E11", "C3"), ("E11", "C4"), ("E11", "C5"), ("E11", "C6"), ("E11", "C7"), ("E11", "C8"), ("E11", "C9"), ("E11", "C10"), ("E11", "C11"),
    ("E12", "C1"), ("E12", "C2"), ("E12", "C3"), ("E12", "C4"), ("E12", "C5"), ("E12", "C6"), ("E12", "C7"), ("E12", "C8"), ("E12", "C9"), ("E12", "C10"), ("E12", "C11"),
    ("E13", "C1"), ("E13", "C2"), ("E13", "C3"), ("E13", "C4"), ("E13", "C5"), ("E13", "C6"), ("E13", "C7"), ("E13", "C8"), ("E13", "C9"), ("E13", "C10"), ("E13", "C11"),
    ("E14", "C1"), ("E14", "C2"), ("E14", "C3"), ("E14", "C4"), ("E14", "C5"), ("E14", "C6"), ("E14", "C7"), ("E14", "C8"), ("E14", "C9"), ("E14", "C10"), ("E14", "C11"),

    # Infrastructure and social systems leading to losses and impacts
    ("O1", "C1"), ("O1", "C2"), ("O1", "C3"), ("O1", "C4"), ("O1", "C5"), ("O1", "C6"), ("O1", "C7"), ("O1", "C8"), ("O1", "C9"), ("O1", "C10"), ("O1", "C11"),
    ("O2", "C1"), ("O2", "C2"), ("O2", "C3"), ("O2", "C4"), ("O2", "C5"), ("O2", "C6"), ("O2", "C7"), ("O2", "C8"), ("O2", "C9"), ("O2", "C10"), ("O2", "C11"),
    ("O3", "C1"), ("O3", "C2"), ("O3", "C3"), ("O3", "C4"), ("O3", "C5"), ("O3", "C6"), ("O3", "C7"), ("O3", "C8"), ("O3", "C9"), ("O3", "C10"), ("O3", "C11"),
    ("O4", "C1"), ("O4", "C2"), ("O4", "C3"), ("O4", "C4"), ("O4", "C5"), ("O4", "C6"), ("O4", "C7"), ("O4", "C8"), ("O4", "C9"), ("O4", "C10"), ("O4", "C11"),
    ("O5", "C1"), ("O5", "C2"), ("O5", "C3"), ("O5", "C4"), ("O5", "C5"), ("O5", "C6"), ("O5", "C7"), ("O5", "C8"), ("O5", "C9"), ("O5", "C10"), ("O5", "C11"),
    ("O6", "C1"), ("O6", "C2"), ("O6", "C3"), ("O6", "C4"), ("O6", "C5"), ("O6", "C6"), ("O6", "C7"), ("O6", "C8"), ("O6", "C9"), ("O6", "C10"), ("O6", "C11"),
    ("O7", "C1"), ("O7", "C2"), ("O7", "C3"), ("O7", "C4"), ("O7", "C5"), ("O7", "C6"), ("O7", "C7"), ("O7", "C8"), ("O7", "C9"), ("O7", "C10"), ("O7", "C11"),
    ("O8", "C1"), ("O8", "C2"), ("O8", "C3"), ("O8", "C4"), ("O8", "C5"), ("O8", "C6"), ("O8", "C7"), ("O8", "C8"), ("O8", "C9"), ("O8", "C10"), ("O8", "C11"),
    ("O9", "C1"), ("O9", "C2"), ("O9", "C3"), ("O9", "C4"), ("O9", "C5"), ("O9", "C6"), ("O9", "C7"), ("O9", "C8"), ("O9", "C9"), ("O9", "C10"), ("O9", "C11"),
    ("O10", "C1"), ("O10", "C2"), ("O10", "C3"), ("O10", "C4"), ("O10", "C5"), ("O10", "C6"), ("O10", "C7"), ("O10", "C8"), ("O10", "C9"), ("O10", "C10"), ("O10", "C11"),
    ("O11", "C1"), ("O11", "C2"), ("O11", "C3"), ("O11", "C4"), ("O11", "C5"), ("O11", "C6"), ("O11", "C7"), ("O11", "C8"), ("O11", "C9"), ("O11", "C10"), ("O11", "C11"),

    # Preventive and rescue measures influencing losses and impacts
    ("M1", "C1"), ("M1", "C2"), ("M1", "C3"), ("M1", "C4"), ("M1", "C5"), ("M1", "C6"), ("M1", "C7"), ("M1", "C8"), ("M1", "C9"), ("M1", "C10"), ("M1", "C11"),
    ("M2", "C1"), ("M2", "C2"), ("M2", "C3"), ("M2", "C4"), ("M2", "C5"), ("M2", "C6"), ("M2", "C7"), ("M2", "C8"), ("M2", "C9"), ("M2", "C10"), ("M2", "C11"),
    ("M3", "C1"), ("M3", "C2"), ("M3", "C3"), ("M3", "C4"), ("M3", "C5"), ("M3", "C6"), ("M3", "C7"), ("M3", "C8"), ("M3", "C9"), ("M3", "C10"), ("M3", "C11"),
    ("M4", "C1"), ("M4", "C2"), ("M4", "C3"), ("M4", "C4"), ("M4", "C5"), ("M4", "C6"), ("M4", "C7"), ("M4", "C8"), ("M4", "C9"), ("M4", "C10"), ("M4", "C11"),
    ("M5", "C1"), ("M5", "C2"), ("M5", "C3"), ("M5", "C4"), ("M5", "C5"), ("M5", "C6"), ("M5", "C7"), ("M5", "C8"), ("M5", "C9"), ("M5", "C10"), ("M5", "C11"),
    ("M6", "C1"), ("M6", "C2"), ("M6", "C3"), ("M6", "C4"), ("M6", "C5"), ("M6", "C6"), ("M6", "C7"), ("M6", "C8"), ("M6", "C9"), ("M6", "C10"), ("M6", "C11"),
    ("M7", "C1"), ("M7", "C2"), ("M7", "C3"), ("M7", "C4"), ("M7", "C5"), ("M7", "C6"), ("M7", "C7"), ("M7", "C8"), ("M7", "C9"), ("M7", "C10"), ("M7", "C11"),
    ("M8", "C1"), ("M8", "C2"), ("M8", "C3"), ("M8", "C4"), ("M8", "C5"), ("M8", "C6"), ("M8", "C7"), ("M8", "C8"), ("M8", "C9"), ("M8", "C10"), ("M8", "C11"),
    ("M9", "C1"), ("M9", "C2"), ("