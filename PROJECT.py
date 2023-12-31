#Simulate how a computer works, partly(register->mem simulation via py)
#https://colab.research.google.com/drive/1Kg_Bqzo2VkXeCGV1a6QAMfge3zky4DnA?usp=sharing

M = [0,0,0,0,0,0,0,0]  #memory

R = [0,0,0,0,0,0,0,0]  #register

PC = 0
#listOfInstructions =[(0, "C", 1),
# (1, "C", 1),(0, "LD", 1),(0, "ST", 1),
# (0, "+", 1, 2),(0, "+", 2, 3),(0, "+", 3, 4),(0, "+", 4, 5),(0, "+", 5, 6),(0, "+", 6, 7)]
# 0, "LD", 1
# 0, "ST", 1
#print(R[0],R[1],R[2],R[3])
#print(M)

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def evalListOfInstructions(listOfInstructions, R, M, PC):
  print("eval")
  while (PC < len(listOfInstructions)):
    instr = listOfInstructions[PC]
    print(R)
    print(M)
    print(instr)
    if len(instr) == 3:
       op = instr[1]
       if op == "C":
        addr = instr[0]
        const = instr[2]
        R[addr] = const
       elif op == "LD": # Move from memory to register
        addrMem  = instr[0]
        addrReg = instr[2]
        R[addrReg] = M[addrMem]
       elif op == "ST": # Move from register to memory
        addrReg = instr[0]
        addrMem = instr[2]
        M[addrMem] = R[addrReg]
       PC += 1
    elif len(instr) == 4:
      addr1 = instr[0]
      addr2 = instr[2]
      addr3 = instr[3]
      op = instr[1]
      if op == "+":
       R[addr3] = R[addr1] + R[addr2]
      elif op == "-":
       R[addr3] = R[addr1] - R[addr2]
      elif op == "*":
       R[addr3] = R[addr1] * R[addr2]
      elif op == "/":
       R[addr3] = R[addr1] / R[addr2]
      PC += 1
    elif len(instr) == 5:
       addr1 = instr[0]
       addr2 = instr[2]
       pcIf = instr[3]
       pcElse = instr[4]
       if M[addr1] > M[addr2]:
        PC = pcIf
       else:
        PC = pcElse
    # Code that evaluates instruction by instruction in listOfInsructions
  return R
#evalListOfInstructions(listOfInstructions, R, M)
#print(R)

listOfInstructions = []
str="""a = 5
b = 3
c = a
a = b + c
a = b - c
a = b * c
a = b / c
if a > b
a = 11
else
b = 8
c = 12
"""
pythStr = str.split("\n")
print(pythStr)
addrFree = 0
dicVarAddr = {}
lineIdx = 0
while lineIdx < len(pythStr):

  # Extract operands
  # 
  line = pythStr[lineIdx]
  ops = line.split(" ")
  print(ops)
  # Constan operation
  if len(ops) == 3:
    if isInt(ops[2]):
      if ops[0] in dicVarAddr:
        addr1 = dicVarAddr[ops[0]]
      else:
        addr1 = addrFree
        addrFree += 1
        dicVarAddr[ops[0]] = addr1
      instr1 = (0, "C", int(ops[2]))
      instr2 = (0, "ST", addr1)
      listOfInstructions.append(instr1)
      listOfInstructions.append(instr2)
    
    else:
      # Variable assigned to variable
      if ops[0] in dicVarAddr:
        addr1 = dicVarAddr[ops[0]]
      else:
        addr1 = addrFree
        addrFree += 1
        dicVarAddr[ops[0]] = addr1
      
      if ops[2] in dicVarAddr:
        addr2 = dicVarAddr[ops[2]]
      else:
        addr2 = addrFree
        addrFree += 1
        dicVarAddr[ops[2]] = addr1
      instr1 = (addr2, "LD", 0)
      instr2 = (0, "ST", addr1)
      listOfInstructions.append(instr1)
      listOfInstructions.append(instr2) 
    lineIdx+= 1
    # map to constant
  elif len(ops) == 4:
    if ops[1] in dicVarAddr:
      addr1 = dicVarAddr[ops[1]]
    else:
        addr1 = addrFree
        addrFree += 1
        dicVarAddr[ops[1]] = addr1 
    
    if ops[3] in dicVarAddr:
      addr2 = dicVarAddr[ops[3]]
    else:
        addr2 = addrFree
        addrFree += 1
        dicVarAddr[ops[3]] = addr1 
    # Take if block instruction and map it
    pcIf = len(listOfInstructions)
    instr1 = (addr1, "IF", addr2, pcIf, 0)
    # when we come to else instruction, go over listOfInsturctions, find first if 
    # then set this pcelse to curent PC
    lineIdx += 1
  elif len(ops) == 1:
    for i in range(1, len(listOfInstructions) + 1):
      if (listOfInstructions[-i][1] == "IF"):
       instr = listOfInstructions[-i]
       print("INSTR BEFORE", instr)
       listOfInstructions[-i] =  (instr[0], 
        instr[1], instr[2], instr[3], len(listOfInstructions))
       print("INSTRUCTION AFTER", listOfInstructions[-i])
       break
    lineIdx += 1
    # Handle else case
  elif len(ops) == 5:
   
    if ops[0] in dicVarAddr:
      addr1 = dicVarAddr[ops[0]]
    else:
        addr1 = addrFree
        addrFree += 1
        dicVarAddr[ops[0]] = addr1 
    
    if ops[2] in dicVarAddr:
      addr2 = dicVarAddr[ops[2]]
    else:
        addr2 = addrFree
        addrFree += 1
        dicVarAddr[ops[2]] = addr1 
    
    if ops[4] in dicVarAddr:
      addr3 = dicVarAddr[ops[4]]
    else:
        addr3 = addrFree
        addrFree += 1
        dicVarAddr[ops[4]] = addr1  
    instr1 = (addr2, "LD", 0)
    instr2 = (addr3, "LD", 1)
    if ops[3] == "+":
      instr3 = (0, "+", 1, 1)
    elif ops[3] == "-":
      instr3 = (0, "-", 1, 1)
    elif ops[3] == "*":
      instr3 = (0, "*", 1, 1)
    elif ops[3] == "/":
      instr3 = (0, "/", 1, 1)
    instr4 = (1, "ST", addr1)
    listOfInstructions.append(instr1)
    listOfInstructions.append(instr2) 
    listOfInstructions.append(instr3)
    listOfInstructions.append(instr4)
    lineIdx += 1
  else: 
    pass
  print(listOfInstructions)
evalListOfInstructions(listOfInstructions, R, M, PC)
print("Memory is", M)
    # map to classical operation
