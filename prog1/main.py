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
	fds = fds[1:-1].replace(' ', '').split(',')
	func_deps = []
	for fd in fds:
		LHS = fd[:fd.find('-')]
		RHS = fd[fd.find('>')+1:]
		if LHS not in attributes:
			print("Invalid functional dependency {}, {} is not a valid attribute".format(fd, LHS))
		elif RHS not in attributes:
			print("Invalid functional dependency {}, {} is not a valid attribute".format(fd, RHS))
		else:
			func_deps.append((LHS, RHS))

	return func_deps

def fd_isTrivial(LHS, RHS):
	return LHS in RHS

def to_str(set):
	out = ''
	for i in set:
		out += i
	return out

def fd_LHSisSuperkey(LHS, attributes, fds):
	LHS_closure = set()
	for attr in LHS:
		LHS_closure.add(attr)

	running = True
	while running:
		prev_LHS_closure = to_str(LHS_closure)
		for fd_LHS in fds:
			if fd_LHS in to_str(LHS_closure):
				for attr in fds[fd_LHS]:
					LHS_closure.add(attr)
		if to_str(LHS_closure) == prev_LHS_closure:
			running = False
	return len(LHS_closure) == len(attributes)


#relation = input("Input a relation in the form 'r(a, b, c, d)': ")
relation = 'r(A, B, C)'
attributes = parse_relation(relation)
print(attributes)

#fds = input("Input a set of functional dependencies in the form '{A -> B, B -> C}': ")
fds = '{A -> B, B -> C, B -> A}'
func_deps = parse_fds(fds, attributes)
fd_dict = parse_fds2(func_deps)
print(func_deps)


for fd in func_deps:
	# unpack the fd tuple
	LHS = fd[0]
	RHS = fd[1]
	# Check if BCNF
	if fd_isTrivial(LHS, RHS) or fd_LHSisSuperkey(LHS, attributes, fd_dict):
		# yes this is BCNF
		print('{} is BCNF'.format(fd))

	else:
		# not BCNF
		print('{} is not BCNF'.format(fd))
		# TODO: decompose









