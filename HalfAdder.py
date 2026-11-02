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


# print("Half Adder")
# print("A B | Sum Carry")
# print("----------------")

# for A in [0, 1]:
#     for B in [0, 1]:
#         Sum, Carry = half_adder(A, B)
#         print(A, B, "|", Sum, "  ", Carry)


def mp_neuron(input,weights,treshold):
    total =0
    for i in range(len(input)):
        total += input[i]*weights[i]
    if total>=treshold:
        return 1
    return 0

def half_adder(A,B):
    carry = mp_neuron([A,B],[1,1],2)
    NAND = mp_neuron([A,B],[-1,-1],-1)
    OR = mp_neuron([A,B],[1,1],1)
    Sum = mp_neuron([NAND,OR],[1,1],2)
    return Sum,carry

print('A B SUM CARRY')
for A in [0,1]:
    for B in [0,1]:
        Sum,carry = half_adder(A,B)
        print(A, B ,Sum , carry)