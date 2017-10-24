def parse_relation(r):
	start = r.find('(')
	end = r.find(')')
	attributes = r[start+1:end].replace(' ', '').split(',')
	return attributes

def parse_fds2(fds):
	func_deps = {}
	for fd in fds:
		if fd[0] in func_deps:
			func_deps[fd[0]] += fd[1]
		else:
			func_deps[fd[0]] = fd[1]
	return func_deps

def parse_fds(fds, attributes):
	fds = fds[1:-1].replace(' ', '').split(';')
	func_deps = []
	for fd in fds:
		LHS = fd[:fd.find('-')].split(',')
		RHS = fd[fd.find('>')+1:].split(',')
		valid = True
		for attr in LHS:
			if attr not in attributes:
				print("Invalid functional dependency {}, {} is not a valid attribute".format(fd, LHS))
				valid = False
		for attr in RHS:
			if attr not in attributes:
				print("Invalid functional dependency {}, {} is not a valid attribute".format(fd, RHS))
				valid = False
		if valid:
			func_deps.append((LHS, RHS))

	return func_deps

def fd_isTrivial(LHS, RHS):
	out = True
	for attr in RHS:
		if attr not in LHS:
			out = False
	return out

def to_str(set):
	out = ''
	for i in set:
		out += i
	return out

# LHS 			- is a list of attributes
# attributes 	- is a list of attributes
# fds 			- is a list of tuples with the format ([LHS], [RHS])
def fd_LHSisSuperkey(LHS, attributes, fds):
	LHS_closure = set()
	for attr in LHS:
		LHS_closure.add(attr)

	running = True
	while running:
		# Save the previous closure to test against at the end to see if there was a change
		prev_LHS_closure = to_str(LHS_closure)

		# Checks func dependency LHS - if it is in LHS_closure, add RHS to LHS_closure
		for fd in fds:
			# unpack the LHS and RHS
			fd_LHS = fd[0]
			fd_RHS = fd[1]

			in_closure = True
			# Iterate through each attribute in LHS (for multi-valued LHS)
			for attr in fd_LHS:
				# Check if every attribute is in LHS_closure
				if attr not in to_str(LHS_closure):
					in_closure = False

			# if LHS in LHS_closure, add RHS to LHS_closure
			if in_closure:
				for attr in fd_RHS:
					LHS_closure.add(attr)

		# If no change, we have finished calculating closure
		if to_str(LHS_closure) == prev_LHS_closure:
			running = False

	# True if LHS_closure and attributes are the same length (assumes they have the same elements)
	return len(LHS_closure) == len(attributes)


#relation = input("Input a relation in the form 'r(a, b, c, d)': ")
relation = 'r(A, B, C)'
attributes = parse_relation(relation)
print(attributes)

#fds = input("Input a set of functional dependencies in the form '{A -> B; B -> A,C}': ")
fds = '{A -> B; B -> C; B -> A, C}'
func_deps = parse_fds(fds, attributes)
#fd_dict = parse_fds2(func_deps)
print(func_deps)


def decompose(func_deps, attributes):

	for fd in func_deps:
		# unpack the fd tuple
		LHS = fd[0]
		RHS = fd[1]
		print(LHS)
		# Check if LHS, RHS are valid in the relation
		if LHS in attributes and RHS in attributes:
			# Check if BCNF
			if fd_isTrivial(LHS, RHS) or fd_LHSisSuperkey(LHS, attributes, fd_dict):
				# yes this is BCNF
				print('{} is BCNF'.format(fd))

			else:
				# not BCNF
				print('{} is not BCNF'.format(fd))

				# Recursively decompose
				# decompose(func_depx, fd_dict, )
		
#decompose(func_deps, fd_dict, attributes)








