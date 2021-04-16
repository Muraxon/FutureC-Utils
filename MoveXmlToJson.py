import xml.etree.ElementTree as ET 
import os

file = ET.parse('scriptautocompletedefs.xml') 

root = file.getroot()
contextD = ""
contextH = ""
contextF = ""
contextS = ""
contextP = ""
contextCString = ""
contextCMoney = ""
contextCTable = ""

completeJsonStructure = "{"
for snippet in root:
    j = 0
    currentContext = -1

    oneSnippet = ""

    contextID = -1
    for childNodes in snippet:
        if(j > 0):
            oneSnippet += ","
        if(childNodes.tag == "keyword"):
            oneSnippet += "\""+str(childNodes.text)+"\":{"
        elif(childNodes.tag == "context"):
            oneSnippet += "\""+str(childNodes.tag)+"\":\""+childNodes.text+"\""
            if(childNodes.text == "CString"):
                contextID = 0
            elif(childNodes.text == "CTable"):
                contextID = 1
            elif(childNodes.text == "CMoney"):
                contextID = 2
            elif(childNodes.text == "D"):
                contextID = 3
            elif(childNodes.text == "F"):
                contextID = 4
            elif(childNodes.text == "P"):
                contextID = 5
            elif(childNodes.text == "H"):
                contextID = 6
            elif(childNodes.text == "S"):
                contextID = 7
        elif (childNodes.tag != "notes"):
            oneSnippet += "\""+str(childNodes.tag)+"\":\""+str(childNodes.text)+"\""
            j += 1
        else:
            textSplit = childNodes.text.split(sep="\n")
            oneSnippet += "\"notes\":["

            x = 0
            for text in textSplit:
                text = text.replace("\t", "")
                text = text.replace("\n", "")
                text = text.replace("\r", "")
                text = text.replace("\"", "\\\"")
                text = text.strip()
                if(x > 0):
                    oneSnippet += "\n,"
                oneSnippet += "\""+text+"\""
                x += 1

            j += 1
            oneSnippet += "]"
    
    oneSnippet += "}"

    if(contextID == 0):
        if(len(contextCString) > 0):
            contextCString += ","
        contextCString += "\n" + oneSnippet
    elif(contextID == 1):
        if(len(contextCTable) > 0):
            contextCTable += ","
        contextCTable += "\n" + oneSnippet
    elif(contextID == 2):
        if(len(contextCMoney) > 0):
            contextCMoney += ","
        contextCMoney += "\n" + oneSnippet
    elif(contextID == 3):
        if(len(contextD) > 0):
            contextD += ","
        contextD += "\n" + oneSnippet
    elif(contextID == 4):
        if(len(contextF) > 0):
            contextF += ","
        contextF += "\n" + oneSnippet
    elif(contextID == 5):
        if(len(contextP) > 0):
            contextP += ","
        contextP += "\n" + oneSnippet
    elif(contextID == 6):
        if(len(contextH) > 0):
            contextH += ","
        contextH += "\n" + oneSnippet
    elif(contextID == 7):
        if(len(contextS) > 0):
            contextS += ","
        contextS += "\n" + oneSnippet


completeJsonStructure += "\"CString\": {" + contextCString
completeJsonStructure += "},\"CTable\": {" + contextCTable
completeJsonStructure += "},\"CMoney\": {" + contextCMoney
completeJsonStructure += "},\"D\": {" + contextD
completeJsonStructure += "},\"F\": {" + contextF
completeJsonStructure += "},\"P\": {" + contextP
completeJsonStructure += "},\"H\": {" + contextH
completeJsonStructure += "},\"S\": {" + contextS + "}"
completeJsonStructure += "}"

if(os.path.exists("./scriptautocompletetest.json")):
    os.remove("./scriptautocompletetest.json")
f = open("scriptautocompletetest.json", mode="w", encoding="utf-8")
f.write(completeJsonStructure)
f.close()