# Implementation of AND, OR, NOT, XOR based on Perceptrons
# ===========================================================

def dot(arg_1, arg_2):
	"""
	inputs arg_1 and arg_2: array-like or integer:
	==============================================

	This function calculates the sum of element-wise product of the
	given input arrays.

	If the passed arguments are both integers,
	the function returns product of the 2 inputs

	"""
	prod_sum = 0
	if type(arg_1) != type(arg_2):
		raise Exception(f"Both the input arguments must be of type int or list/tuple same lengths. First input has type : {type(arg_1)} and second input has type : {type(arg_2)}")
	if type(arg_1) == type(arg_2) == int:
		return arg_1*arg_2
	elif len(arg_1) != len(arg_2):
		raise Exception(f"inconsistent lengths of array_1 and array_2: {len(arg_1)} and {len(arg_2)} respectively.")
	else:
		for i in range(len(arg_1)):
			prod_sum += (arg_1[i]*arg_2[i])

	return prod_sum


def step_function(x):
	return 1 if x>=0 else 0


def perceptron_output(weights, bias, x):
	"""
	returns 1 if the perceptron 'fires'.
	0 if not...

	"""
	calculation = dot(weights, x) + bias
	return step_function(calculation)


"""
With properly chosen weights, perceptrons can solve a number of simple problems.
For example, we can create an AND gate (which returns 1 if both its
inputs are 1 but returns 0 if one (or both) of its inputs is/are 0) with:

# For 2 input AND logic:
=======================
weights = [2,2] 
bias = -3

If both inputs are 1, the calculation equals 2 + 2 - 3 = 1, and the output is 1. If only
one of the inputs is 1, the calculation equals 2 + 0 - 3 = -1, and the output is 0. And
if both of the inputs are 0, the calculation equals -3, and the output is 0.
"""


def AND_function(input_1, input_2, *args):
	"""
	Input Description:
	=================

	input_1: integer type, required
	- First input of logic

	input_2: integer, required
	- 2nd input of logic

	*args: optional and additional inputs,
	- all are integer types

	Returns
	=======
	The result of AND logic of the inputs, either 0 or 1


	"""
	inputs = [input_1, input_2] + list(args)

	for i in set(inputs):
		if (i != 0) and (i != 1):
			raise Exception('Inputs must contain only 0s and 1s')

	weights = [2]*len(inputs)
	bias = -(sum(weights) - 1)

	return perceptron_output(weights, bias, inputs)


def OR_function(input_1, input_2, *args):
	"""
	Input Description:
	=================

	input_1: integer type, required
	- First input of logic

	input_2: integer, required
	- 2nd input of logic

	*args: optional and additional inputs,
	- all are integer types

	Returns
	=======
	The result of OR logic of the inputs, either 0 or 1


	"""
	inputs = [input_1, input_2] + list(args)

	for i in set(inputs):
		if (i != 0) and (i != 1):
			raise Exception('Inputs must contain only 0s and 1s')

	weights = [2]*len(inputs)
	bias = -1

	return perceptron_output(weights, bias, inputs)


def NOT_function(input_):
	"""
	Input Description:
	=================

	input_: integer type, required
	- element whose NOT is to be found

	Returns
	=======
	The result of NOT logic of the input, either 0 or 1


	"""
	if (input_ != 0) and (input_ != 1):
		raise Exception('Inputs must contain only 0s and 1s')

	weights = 2
	bias = -1

	return perceptron_output(weights, bias, input_)


def XOR_function(input_1, input_2):
	"""
	Input Description:
	=================

	input_1: integer type, required
	- 1st input of XOR logic

	input_2: integer type, required
	- 2nd input of XOR logic

	Returns
	=======
	The result of XOR logic of the input, either 0 or 1

	A XOR B = A'B + AB'
	
	or simply, 
		A XOR B = (A AND NOT(B)) OR (NOT(A) AND B)
	"""
	inputs = [input_1, input_2]
	for i in set(inputs):
		if (i != 0) and (i != 1):
			raise Exception('Inputs must contain only 0s and 1s')

	a = input_1
	b = input_2

	return OR_function(AND_function(a, NOT_function(b)), AND_function(NOT_function(a), b)) 




if __name__ == '__main__':
	print(AND_function(1,1,0,1,0))
	print(OR_function(0,0,1,1,0))
	print(NOT_function(0))
	print(XOR_function(1,1))



