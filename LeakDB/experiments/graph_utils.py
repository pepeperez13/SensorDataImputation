import enum

import networkx as nx
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, RDFS, XSD
import sys

def networkx(rdf_graph):
    """
    Convert an RDFLib graph to a NetworkX graph.
    - Nodes: All individuals and ontology classes.
    - Edges: Object properties create directed edges between nodes.
    - Attributes: Data properties are stored as node attributes.
    """
    if isinstance(rdf_graph, Graph) or isinstance(rdf_graph, str):
        if isinstance(rdf_graph, Graph):
            rdf_graph = rdf_graph
        elif isinstance(rdf_graph, str):
            if rdf_graph.endswith('.ttl'):
                try:
                    rdf_graph = Graph().parse(rdf_graph, format='turtle')
                except Exception as e:
                    print(f"Error parsing Turtle file: {e}")
                    return None
            else:
                print("Unexpected input format. Provide a Turtle (.ttl) file path.")
    else:
        print("Unexpected input format. Provide an RDFLib Graph or a .ttl file path.")
        return None

    # Initialize the directed graph
    nx_graph = nx.DiGraph()

    # Process the RDF graph
    for s, p, o in rdf_graph:
        s, p = s.toPython(), p.toPython()
        # Ensure subject is a node
        if s not in nx_graph:
            nx_graph.add_node(s)

        # Check if the object is a literal (data property) or an entity (object property)
        if isinstance(o, Literal):  # Data property → store as a node attribute
            nx_graph.nodes[s][p] = o.toPython()
        else:  # Object property → add an edge
            o = o.toPython()
            # in case o is not a hashable type, parse it to string
            if isinstance(o, enum.Enum):
                o = str(o)
            if p == RDF.type.toPython():
                nx_graph.nodes[s][RDF.type.toPython()] = o
            else:
                nx_graph.add_edge(s, o, predicate=p)

    return nx_graph


import re
from rdflib import RDF

def shorten_uri(uri, ontology_base):
    """
    Extract the local name from a full URI. 
    Removes known ontology base and keeps suffix like Pipe_9 or diameter.
    """
    if uri.startswith(ontology_base):
        return uri.replace(ontology_base, "")
    elif "#" in uri:
        return uri.split("#")[-1]
    elif "/" in uri:
        return uri.split("/")[-1]
    else:
        return uri

def extract_features_from_nx_graph(nx_graph, ontology_base, edge_predicates, node_type_filter, attribute_keys):
    # nx_graph: NetworkX graph
    # ontology_base: Base URI of the ontology to shorten URIs
    # edge_predicates: Either LIST or None - edge predicates to include as attributes
    # node_type_filter: Either None or a specific type to filter nodes by
    # attribute_keys: Either LIST or None - of specific attributes to include

    feature_dict = {}
    rdf_type_key = shorten_uri(str(RDF.type), ontology_base)

    for node, data in nx_graph.nodes(data=True):
        #print(f"Processing node: {node}, data: {data}")

        # Shorten RDF.type value and all keys
        cleaned_data = {
            shorten_uri(k, ontology_base): v if not isinstance(v, str) else shorten_uri(v, ontology_base)
            for k, v in data.items()
        }

        #print(f"Cleaned data: {cleaned_data}")

        # Filter by type if specified
        node_type = cleaned_data.get(rdf_type_key)
        if node_type_filter and node_type != node_type_filter:
            continue

        # Shorten node URI
        node_id = shorten_uri(node, ontology_base)

        # Select attributes
        if attribute_keys:
            features = {k: cleaned_data[k] for k in attribute_keys if k in cleaned_data}
        else:
            # Remove rdf:type from features
            features = {k: v for k, v in cleaned_data.items() if k != rdf_type_key}

        # Now add edges as attributes if requested
        if edge_predicates:
            for _, target, edge_data in nx_graph.out_edges(node, data=True):
                pred = shorten_uri(edge_data.get("predicate", ""), ontology_base)
                if pred in edge_predicates:
                    target_id = shorten_uri(target, ontology_base)
                    
                    if pred in features:
                        if isinstance(features[pred], list):
                            features[pred].append(target_id)
                        else:
                            features[pred] = [features[pred], target_id]
                    else:
                        features[pred] = target_id  # or [target_id] if you always want a list

        feature_dict[node_id] = features

    return feature_dict
