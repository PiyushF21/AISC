# def mp_neuron(inputs, weights, threshold):
#     total = sum(i * w for i, w in zip(inputs, weights))
#     return 1 if total >= threshold else 0


# def half_adder(A, B):

#     carry = mp_neuron(
#         [A, B],
#         [1, 1],
#         2
#     )

#     OR = mp_neuron(
#         [A, B],
#         [1, 1],
#         1
#     )

#     NAND = mp_neuron(
#         [A, B],
#         [-1, -1],
#         -1
#     )

#     Sum = mp_neuron(
#         [OR, NAND],
#         [1, 1],
#         2
#     )

#     return Sum, carry


# def full_adder(A, B, Cin):

#     Sum1, Carry1 = half_adder(A, B)

#     Sum, Carry2 = half_adder(Sum1, Cin)

#     Cout = mp_neuron(
#         [Carry1, Carry2],
#         [1, 1],
#         1
#     )

#     return Sum, Cout


# print("Full Adder")
# print("A B Cin | Sum Cout")
# print("-------------------")

# for A in [0, 1]:
#     for B in [0, 1]:
#         for Cin in [0, 1]:
#             Sum, Cout = full_adder(A, B, Cin)
#             print(A, B, Cin, "| ", Sum, "   ", Cout)



def mp_neuron(inputs,weights,treshold):
    total =0
    for i in range(len(inputs)):
        total+=inputs[i]*weights[i]

    if total>=treshold:
        return 1
    return 0

def half_adder(A,B):
    carry = mp_neuron([A,B],[1,1],2)
    NAND = mp_neuron([A,B],[-1,-1],-1)
    OR = mp_neuron([A,B],[1,1],1)
    Sum = mp_neuron([NAND,OR],[1,1],2)
    return Sum,carry

def full_adder(A,B,Cin):

    sum1,carry1 = half_adder(A,B)
    sum2,carry2 = half_adder(sum1,Cin)
    Cout = mp_neuron([carry1,carry2],[1,1],1)
    return sum2,Cout
print("A B Cin SUM Cout")
for A in [0,1]:
    for B in [0,1]:
        for Cin in [0,1]:
            Sum,Cout = full_adder(A,B,Cin)
            print(A,B,Cin,Sum,Cout)
        