floor1 = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
floor2 = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
floor3 = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
floor4 = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
characters = "0123456789abcdefghijklmnopqrstuvwxyz!\"#$%&'()*+,-./:;<=>?@[\\]^_|"
userInput = ""

userInput = "j.manuel_e@hotmail.com"
userInput = userInput.replace(" ", "")
keyword = ""

for i in userInput:
	if i not in keyword:
		keyword = keyword + i

# keyword used to encrypt data
# keyword = "0w%?fg"
# print(characters, len(characters))
for i in keyword:
	characters = characters.replace(i, "")
# print(characters, len(characters))

key = keyword+characters
# print(key, len(key))

if len(key) != 64:
	print("Unexpected character encountered")

leftof = 0
for i in range(len(floor1)):
	for j in range(len(floor1[i])):
		floor1[i][j] = key[i+j+leftof]
		# floor1[i][j] = i + j + leftof
		# print(i + j + leftof)
	leftof = leftof + 3

leftof = 16
for i in range(len(floor2)):
	for j in range(len(floor2[i])):
		floor2[i][j] = key[i+j+leftof]
		# floor1[i][j] = i + j + leftof
		# print(i + j + leftof)
	leftof = leftof + 3

leftof = 32
for i in range(len(floor3)):
	for j in range(len(floor3[i])):
		floor3[i][j] = key[i+j+leftof]
		# floor1[i][j] = i + j + leftof
		# print(i + j + leftof)
	leftof = leftof + 3

leftof = 48
for i in range(len(floor4)):
	for j in range(len(floor4[i])):
		floor4[i][j] = key[i+j+leftof]
		# floor1[i][j] = i + j + leftof
		# print(i + j + leftof)
	leftof = leftof + 3

plainText = input("messagetoEncrypt: ")
plainText = plainText.replace(" ","")
cipherText = ""
count = 0
trigraph = ""
thingsToEncode = []
thingsToDecode = []

# aqui dividimos el texto en 3 segmentos de 3
c = 0
for i in range(len(plainText)):
	c = c + 1
	if c == 4:
		c = 0

	if i + 1 < len(plainText):
		if plainText[i] == plainText[i + 1] and c != 3:
			lastBit = plainText[i+1:]
			firstBit = plainText[:i + 1] + "x"
			fullWord =  firstBit + lastBit
			plainText = fullWord

			
print(plainText)

for i in plainText:
	count = count + 1

	trigraph = trigraph + i
	if count == 3:
		thingsToEncode.append(trigraph)
		trigraph = ""
		count = 0
# checas que no haya queda un ultimo elemento en el tripgraph que no tenga 3.. you get the idea
if trigraph != "":
	if count == 1:
		trigraph = trigraph + "xz"
		thingsToEncode.append(trigraph)
	if count == 2:
	 	trigraph = trigraph + "x"
	 	thingsToEncode.append(trigraph)
				

def encryptTripgraph(row, column, floor):
	cipherTigraph = ""
	cipherFloor = None
	for i in range(len(floor1)):
		for j in range(len(floor1[i])):
			if floor1[i][j] == row:
				cipherRow = i
			if floor1[i][j] == column:
				cipherColumn = j
			if floor1[i][j] == floor:
				cipherFloor = floor1

	for i in range(len(floor2)):
		for j in range(len(floor2[i])):
			if floor2[i][j] == row:
				cipherRow = i
			if floor2[i][j] == column:
				cipherColumn = j
			if floor2[i][j] == floor:
				cipherFloor = floor2

	for i in range(len(floor3)):
		for j in range(len(floor3[i])):
			if floor3[i][j] == row:
				cipherRow = i
			if floor3[i][j] == column:
				cipherColumn = j
			if floor3[i][j] == floor:
				cipherFloor = floor3

	for i in range(len(floor4)):
		for j in range(len(floor4[i])):
			if floor4[i][j] == row:
				cipherRow = i
			if floor4[i][j] == column:
				cipherColumn = j
			if floor4[i][j] == floor:
				cipherFloor = floor4
	
	# print(row, column, floor, cipherFloor)
	cipherTigraph =  cipherFloor[cipherRow][cipherColumn]
	return cipherTigraph

# thisistests = encryptTripgraph("l", "h","e")
# print(thisistests)


# Aqui empieza el ciframiento de las letras

for trigraph in thingsToEncode:
	firstletter = encryptTripgraph(trigraph[0], trigraph[1],trigraph[2])
	secondLetter = encryptTripgraph(trigraph[1], trigraph[2],trigraph[0])
	thirdLetter = encryptTripgraph(trigraph[2], trigraph[0],trigraph[1])
	cipherTigraph = firstletter + secondLetter + thirdLetter
	thingsToDecode.append(cipherTigraph)

for trigraph in thingsToDecode:
	for i in trigraph:
		cipherText = cipherText + i


print(cipherText)

# print(thingsToEncode)


# print(floor1)
# print(floor2)
# print(floor3)
# print(floor4)
