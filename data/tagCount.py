tags = {}

with open('train-fixed-25k.pos', 'rb') as f:
	for line in f:
		tokens = line.split()
		for token in tokens:
			word = token.split('/')[0]
			tag = token.split('/')[1]
			if tag in tags.keys():
				tags[tag] += 1
			else:
				tags[tag] = 1

with open('log.txt', 'wb') as f:
	for tag in tags.keys():
		print tag + " : %d" % tags[tag]
		f.write(tag + " : %d\n" % tags[tag])