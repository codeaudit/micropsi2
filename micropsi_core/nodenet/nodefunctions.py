
def register(nodenet, node=None, **params):
    for type, gate in node.gates.items():
        gate.gate_function(node.get_slot("gen").activation)

def sensor(nodenet, node=None, datasource=None, **params):
    node.gates["gen"].gate_function(nodenet.world.get_datasource(nodenet.uid, datasource))

def actor(nodenet, node=None, datatarget=None, **params):
    node.nodenet.world.set_datatarget(nodenet.uid, datatarget, node.get_slot("gen").activation)
    node.activation = node.get_slot("gen").activation

def concept(nodenet, node=None, **params):
    for type, gate in node.gates.items():
        gate.gate_function(node.get_slot("gen").activation)

def pipe(nodenet, node=None, **params):
    gen = 0.0
    por = 0.0
    ret = 0.0
    sub = 0.0
    sur = 0.0

    sub += node.get_slot("sub").activation
    sub += node.get_slot("por").activation
    sub += node.get_slot("sur").activation
    if sub == 0: sub = -1

    sur += node.get_slot("sur").activation * (1+node.get_slot("sub").activation) * (1+node.get_slot("ret").activation)
    if sur < 0: sur = 0

    por += node.get_slot("sur").activation
    if por == 0: por = -1

    ret += node.get_slot("ret").activation
    if ret == 0: ret = -1

    node.get_gate("gen").gate_function(gen)
    node.get_gate("por").gate_function(por)
    node.get_gate("ret").gate_function(ret)
    node.get_gate("sub").gate_function(sub)
    node.get_gate("sur").gate_function(sur)

def label(nodenet, node, **params):
    for type, gate in node.gates.items():
        gate.gate_function(node.get_slot("gen").activation)

def event(nodenet, node, **params):
    for type, gate in node.gates.items():
        gate.gate_function(node.get_slot("gen").activation)

def activator(nodenet, node, **params):
    nodenet.nodespaces[node.parent_nodespace].activators[node.parameters["type"]] = node.activation