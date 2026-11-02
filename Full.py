def mcp_neuron(input,weights,threshold):
    total =0
    for i in range(len(weights)):
        total+=input[i]*weights[i]
    if total>=threshold:
        return 1
    return 0

def half_adder(A,B):
    carry = mcp_neuron([A,B],[1,1],2)
    NAND=mcp_neuron([A,B],[-1,-1],-1)
    OR=mcp_neuron([A,B],[1,1],1)
    Sum = mcp_neuron([NAND,OR],[1,1],2)
    return Sum,carry

def full_adder(A,B,Cin):
    sum1,carry1=half_adder(A,B)
    sum2 , carry2 = half_adder(sum1,Cin)
    carry = mcp_neuron([carry1,carry2],[1,1],1)
    return sum2,carry

print("A B Cin Sum carry")
for A in [0,1]:
    for B in [0,1]:
        for Cin in [0,1]:
            Sum,carry = full_adder(A,B,Cin)
            print(A,B,Cin,Sum,carry)