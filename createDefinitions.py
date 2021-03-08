import os, json, re
import xml.etree.ElementTree as ET 
import utils

def replaceWithTypescriptAnnotation(text :str, type_ :str, type_replacement :str):
	text = text.split(",")
	newtext = ""
	for param in text:
		param = param.strip()
		param = param.split(" ")
		newType = ""
		newParamName = ""
		i = 0
		while(i < len(param)):
			ident = param[i]
			ident = ident.strip()
			ident = ident.strip("*")
			if(ident == "*"):
				continue

			if(i == 0):
				newType = utils.replaceTypes(ident)
			else:
				newParamName = ident
			i = i + 1

		if(len(newtext) > 0):
			newtext = newtext + ", "
		
		newtext = newtext + newParamName.strip() + " :" + newType.strip()
	return newtext


# Passing the path of the 
# xml document to enable the 
# parsing process 
f = open("./src/scriptautocompletedefs.xml", "r", 4096, "utf-8")
tree = ET.XML(f.read())
f.close()

ctable = "declare class CTable {"
cmoney = "declare class CMoney {"
cdatetime = "declare class CDateTime {"
functions_and_definitions = ""

utils.deleteFileIfPossible()

for elem in tree:
	context = ""
	keyword = ""
	notes = ""
	returnvalue = ""
	signature = ""

	for subelem in elem:
		if(subelem.tag == "keyword"):
			keyword = subelem.text
		elif(subelem.tag == "signature"):
			sign = subelem.text
			if(sign):
				signature = replaceWithTypescriptAnnotation(sign, "CString", "string")
			
		elif(subelem.tag == "context"):
			context = subelem.text
		elif(subelem.tag == "returnvalue"):
			returnvalue = subelem.text
			returnvalue = utils.replaceTypes(returnvalue)
		elif(subelem.tag == "notes"):
			notes = subelem.text


	if(context == "CTable"):
		if(len(notes.strip()) > 0):
			ctable = ctable + "\n/*" + notes + "*/\n"
		else:
			ctable = ctable + "\n"
		ctable = ctable + keyword + "(" + signature + ") :" + returnvalue + ";"
	elif(context == "CDateTime"):
		if(len(notes.strip()) > 0):
			cdatetime = cdatetime + "\n/*" + notes + "*/\n"
		else:
			cdatetime = cdatetime + "\n"

		cdatetime = cdatetime + keyword + "(" + signature + ") :" + returnvalue + ";"
	elif(context == "CMoney"):
		if(len(notes.strip()) > 0):
			cmoney = cmoney + "\n/*" + notes + "*/\n"
		else:
			cmoney = cmoney + "\n"

		cmoney = cmoney + keyword + "(" + signature + ") :" + returnvalue + ";"
	else:
		if(keyword.find("TYPE_") == 0 or keyword.find("WEEK") == 0 or keyword.find("DIR_") == 0):
			returnvalue = "number"
		elif(keyword.find("STRING_") == 0):
			returnvalue = "string"
		elif(keyword.find("m_Rec") == 0):
			returnvalue = "CTable"
		elif(keyword.find("m_Tab") == 0):
			returnvalue = "number"

		if(returnvalue == "0" or len(returnvalue) <= 0):
			returnvalue = "void"

		if(len(notes.strip()) > 0):
			functions_and_definitions = functions_and_definitions + "\n/*" + notes + "*/\n"
		else:
			functions_and_definitions = functions_and_definitions + "\n"
		if(len(signature) > 0 or len(context) > 0):
			functions_and_definitions = functions_and_definitions + "declare function " + keyword + "(" + signature + ") :" + returnvalue + ";"
		else:
			functions_and_definitions = functions_and_definitions + "declare let " + keyword + " :" + returnvalue + ";"

ctable = ctable + "\n}"
cdatetime = cdatetime + "\n}"
cmoney = cmoney + "\n}"

f = utils.createDeclarationFile("main.d.ts")
f.write(ctable+ "\n" + cmoney + "\n" + cdatetime + "\n" + functions_and_definitions)
f.close()