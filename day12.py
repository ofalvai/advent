import json

def walkandsum(node):
    if isinstance(node, int):
        return node
    elif isinstance(node, list):
        return sum(map(walkandsum, node))
    elif isinstance(node, dict):
        if 'red' in node.values():
            return 0
            
        return sum(map(walkandsum, node.values()))

    return 0



with open('day12.txt') as f:
    doc = json.loads(f.readlines()[0])
    print(walkandsum(doc))