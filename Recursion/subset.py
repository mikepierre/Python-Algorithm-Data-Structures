def subset(subset_list):
	result = [[]]
	for item in subset_list:
		result += [combo+[item] for combo in result]
	return result

subset_list = ['A','B','C']
print subset(subset_list)
