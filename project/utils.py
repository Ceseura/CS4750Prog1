def print2(data):
	if len(data) < 1:
		return
	keys = list(data[0].keys())
	title = ""
	divider = ""
	for key in keys:
		title += "{}\t|".format(key)
		divider += "-----------"

	print(divider)
	print(title)
	print(divider)

	for item in data:
		line = ""
		for key in keys:
			if len(key) > 8:
				line += "{}\t\t|".format(item[key])
			else:
				line += "{}\t|".format(item[key])
		print(line)

	print(divider)
	print("\n\n")