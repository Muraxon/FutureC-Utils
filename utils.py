import os, shutil

def replaceTypes(text):
	if(text == "double" or text == "int" or text == "TYPE_DOUBLE" or text == "TYPE_INT" or text == "BYTE" or text == "long" or text == "short" or text == "DWORD" or text == "TYPE_BYTE" or text == "TYPE_SHORT"):
		text = "number"
	elif(text == "CString" or text == "TYPE_CSTRING" or text == "char"):
		text = "string"
	elif(text == "CTable" or text == "TYPE_CTABLE"):
		text = "CTable"
	elif(text == "CMoney" or text == "TYPE_CMONEY" or text == "TYPE_MONEY"):
		text = "CMoney"
	elif(text == "BOOL" or text == "TYPE_BOOL"):
		text = "boolean"
	elif(text == "TYPE_CDATETIME" or text == "CDateTime" or text == "TYPE_DATETIME"):
		text = "CDateTime"
	return text

def deleteFileIfPossible():
	if(os.path.exists("./declaration/main.d.ts")):
		os.remove("./declaration/main.d.ts")

def deleteDirIfPossible():
	if(os.path.exists("./output")):
		shutil.rmtree("./output")

def createDirStructure(subDir :str):
	if(not os.path.exists("./output/" + subDir)):
		os.makedirs("./output/" + subDir)

	if(not os.path.exists("./src")):
		os.mkdir("./src")

def createFile(filename :str):
	found = filename.rfind("/")
	subDir = ""
	if(found >= 0):
		subDir = filename[:found]
	
	createDirStructure(subDir)
	f = open("./output/" + filename, "w", 4096, "utf-8")
	return f

def createDeclarationFile(filename):
	if(not os.path.exists("./declaration/")):
		os.mkdir("./declaration")
	f = open("./declaration/" + filename, "w", 4096, "utf-8")
	return f

def transposeFunction(line :str):
	found = line.find("FUNCTION:")
	if(found >= 0):
		line = line.replace("&", " ")
		line = line.replace("  ", " ")
		line = line.replace(";", "")
		foundStartReturnType = line.find(" ", found + 1)
		found2 = line.find(" ", foundStartReturnType + 1)

		returnType = line[foundStartReturnType + 1: found2]
		returnType = replaceTypes(returnType.strip())
		line = line[found2 + 1:]

		newParam = ""
		found = line.find("(", found + 1)
		if(found >= 0):
			found2 = line.find(")", found + 1)
			if(found2 >= 0):
				linetmp = line[found + 1: found2]
				linetmp = linetmp.split(",")
				for x in linetmp:
					x = x.strip()
					y = x.split(" ")
					if(len(y) > 1):
						if(len(newParam) > 0):
							newParam = newParam + ", "
						newParam = newParam + y[1] + " :" + replaceTypes(y[0])

		fnc = line[:found]
		line = "export function " + fnc + "(" + newParam + ") :" + returnType + " {\n" 


	found = line.find("ENDFUNCTION")
	if(found >= 0):
		line = "}"
	return line
