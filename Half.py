def mcp_neuron(inputs,weights,threshold):
    total=0
    for i in range(len(weights)):
        total+=inputs[i]*weights[i]
    if total>=threshold:
        return 1
    return 0

def half_adder(A,B):
    carry = mcp_neuron([A,B],[1,1],2)
    NAND=mcp_neuron([A,B],[-1,-1],-1)
    OR=mcp_neuron([A,B],[1,1],1)
    Sum = mcp_neuron([NAND,OR],[1,1],2)
    return Sum,carry

print("A B SUM CARRY")
for A in [0,1]:
    for B in [0,1]:
        Sum,carry = half_adder(A,B)
        print(A,B,Sum,carry)
