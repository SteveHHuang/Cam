#SEMIFINISHED product
#register->mem simulation via py
M = [0,0,0,0,0,0,0,0]  #memory

R = [0,0,0,0,0,0,0,0]  #register
PC = 0
#listOfInstructions =[(0, "C", 1),
#      (1, "C", 1),(0, "LD", 1),(0, "ST", 1),
#      (0, "+", 1, 2),(0, "+", 2, 3),(0, "+", 3, 4),(0, "+", 4, 5),(0, "+", 5, 6),(0, "+", 6, 7)]
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
         if op == "-":
           R[addr3] = R[addr1] - R[addr2]
         if op == "*":
           R[addr3] = R[addr1] * R[addr2]
         if op == "/":
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
if a > b: 
  a = 5
else:
  b = 3
"""
pythStr = str.split("\n")
print(pythStr)
addrFree = 0
dicVarAddr = {}
for line in pythStr:
  # Extract operands
  # 
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
    pass 
    # map to constant
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
    
  else: 
    pass
  print(listOfInstructions)
evalListOfInstructions(listOfInstructions, R, M, PC)
print("Memory is", M)
    # map to classical operation
"""
for i in range()
                                                          

"""
