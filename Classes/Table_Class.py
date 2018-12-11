class Table:
	header = list()
	content = list()
	associated_file = ""

	def __init__(self, file):
		f = open(file, "r")
		text = f.read().split("\n")
		if(text[-1] == ""):
			text.pop(-1)
		f.close()
		self.header.append(text[0].split(";"))
		for element in text[1:]:		
			self.content.append(element.split(";"))
		acc = [item for sublist in self.header for item in sublist]
		self.header = acc
		self.associated_file = file

	def __str__(self):
		acc = "\t".join(self.header) + "\n\n"
		for line in self.content:
			acc += "\t".join(line) + "\n"
		return acc

	def __getitem__(self, i):
		return "\t".join(self.content[i])

	# returns string if True or prints if False
	def print(self, ret=False):
		if(ret):
			return self.__str__()
		else:
			print(self.__str__())

	# Returns [rows, cols]
	def __len__(self):
		return len(self.content)

	def col(self, key):
		acc = []
		for element in self.content:
			acc.append(element[key])
		return acc

	def add_col(self, lista, key=-1):
		if(key == -1):
			key = len(lista)
		new_head = lista.pop(0)
		lista = tostr(lista)
		self.header.insert(key, new_head)
		for i in range(0, len(self)):
			self.content[i].insert(key, lista[i])

	def del_col(self, key):
		self.header.pop(key)
		for i in range(0, len(self)):
			self.content[i].pop(key)

	def save_table(self, file=""):
		if(file == ""):
			f = open(self.associated_file, "w")
		else:
			f = open(file, "w")

		f.write(";".join(self.header) + "\n")
		for i in range(0, len(self)):
			f.write(";".join(self.content[i]) + "\n")
		f.close()
		

def read_table(file):
	return Table(file)

def scalarsum(num, lista):
	lista = toint(lista)
	for i in range(0,len(lista)):
		lista[i] += num
	lista = toint(lista)
	return lista

def scalarmult(num, lista):
	lista = toint(lista)
	for i in range(0,len(lista)):
		lista[i] = lista[i] * num
	lista = toint(lista)
	return lista	

def bitwisesum(lista1, lista2):
	out_list = []
	lista1 = toint(lista1)
	lista2 = toint(lista2)
	for i in range(0,len(lista1)):
		out_list.append(lista1[i] + lista2[i])
	out_list = toint(out_list)
	return out_list

def bitwisemult(lista1, lista2):
	lista1 = toint(lista1)
	lista2 = toint(lista2)
	out_list = []
	for i in range(0,len(lista1)):
		out_list.append(lista1[i] * lista2[i])
	out_list = toint(out_list)
	return out_list

def toint(lista):
	return [ int(x) for x in lista ]

def tostr(lista):
	return [ str(x) for x in lista ]
