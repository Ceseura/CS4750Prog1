# using the networkx library because I don't feel like implementing my own graph/cycle detection
import networkx as nx

# Get input
transactions = input("Please input a set of transactions in the format: {r1(X), w2(Y)} where:\n R: Read\n W: write\n number: transaction id\n variable: variable accessed in transaction.\n")

t1 = '{r1(x), w2(z), w2(x)}'
t2 = '{r1(A), w1(A), r2(A), w2(A), r1(B), w1(B), r2(B), w2(B)}'
t3 = '{r2(A), w2(A), r1(A), w1(A), r1(B), w1(B), r2(B), w2(B)}'
#transactions = t2

# split input into list of transactions
trans_list = transactions.replace(' ', '')[1:-1].split(',')

# helper functions to parse transactions
def get_op(transaction):
	return transaction[0]

def get_id(transaction):
	outstr = ''
	for c in transaction[1:]:
		if c != '(':
			outstr += c
		elif c == '(':
			break;

	return outstr
	
def get_var(transaction):
	outstr = ''
	flag = False
	for c in transaction[1:]:
		if c == ')':
			flag = False
		elif flag:
			outstr += c
		elif c == '(':
			flag = True
	return outstr

# class for nodes (transaction)
class trans_node:
	def __init__(self, tid):
		self.tid = tid

	def __str__(self):
		return "transaction: id={}".format(self.tid)

	def __repr__(self):
		return self.__str__()

g = nx.DiGraph()

#print('List of transactions: {}'.format(trans_list))

# create nodes for each transaction set

# list all of the unique transactions
unique_transactions = []
for trans in trans_list:
	tid = get_id(trans)

	if tid not in unique_transactions:
		unique_transactions.append(tid)

# add all of the unique transactions as nodes
for trans_id in unique_transactions:
	temp = trans_node(trans_id)
	g.add_node(temp)

# helper function to find node id given tid
def find_node_id(tid, graph):
	for item in list(graph):
		if item.tid == tid:
			return item

# Go through trans_list and look for conflicts
for index, trans in enumerate(trans_list):
	#print("working on {}".format(trans))
	# Only check against transactions further down the list
	for other_trans in trans_list[index+1:]:
		#print("Comparing against {}".format(other_trans))
		same_var = get_var(trans) == get_var(other_trans)
		at_least_one_write = get_op(trans) == 'w' or get_op(other_trans) == 'w'
		not_same_transaction_set = get_id(trans) != get_id(other_trans)
		if not_same_transaction_set and same_var and at_least_one_write:
			# A conflict !
			# add edge to graph
			#print("conflict")
			n1 = find_node_id(get_id(trans), g)
			n2 = find_node_id(get_id(other_trans), g)
			g.add_edge(n1, n2)

# now search for cycles and output

if nx.is_directed_acyclic_graph(g):
	print("This graph is conflict serializable")
	order = nx.topological_sort(g)
	schedule = ' -> '.join(map(str, list(order)))
	print("Serial Equivalent Schedule: {}".format(schedule))


else:
	print("This graph is not conflict serializable")
	cycles = []
	try:
		cycles = nx.find_cycle(g)
	except:
		pass

	text_out = ''
	text_out += str(cycles[0][0]) + ' -> '
	text_out += str(cycles[0][1]) + ' -> '
	for e in cycles[1:-1]:
		text_out += str(e[1]) + ' -> '
	text_out += str(cycles[-1][1])
	print("cycle: {}".format(text_out))






