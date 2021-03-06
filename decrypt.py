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


def decryptTrigraph(row, floor, column):
	decriptedText = ""
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

	decriptedText =  cipherFloor[cipherRow][cipherColumn]
	return decriptedText


reconstructedTirpgraphs = []


for trigraph in thingsToDecode:
	firstletter = decryptTrigraph(trigraph[0], trigraph[1],trigraph[2])
	secondLetter = decryptTrigraph(trigraph[1], trigraph[2],trigraph[0])
	thirdLetter = decryptTrigraph(trigraph[2], trigraph[0],trigraph[1])
	reconstructedText = firstletter + secondLetter + thirdLetter
	reconstructedTirpgraphs.append(reconstructedText)

reconstructedPlainText = ""
for i in reconstructedTirpgraphs:
	for j in i:
		reconstructedPlainText = reconstructedPlainText + j


reconstructedPlainText = reconstructedPlainText.replace("x", "")
print(reconstructedPlainText)