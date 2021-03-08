import os, json, re, sys
import utils

STANDARD_TEMPLATE_FILE = "./src/template_file.tmp"
TEMPLATE_PARAMETER = "-t"
STANDARD_CONFIG_FILE = "./src/config_transpile.json"
STANDARD_TSCONFIG_TEMPLATE_FILE = "./src/template_tsconfig.tmp"
TSCONFIG_TEMPLATE_PARAMETER = "-ts"

CONFIG_PARAMETER = "-c"
JUST_DELETE_PARAMETER = "-jd"
INIT_PARAMETER = "init"

for x in sys.argv:
	if(x == JUST_DELETE_PARAMETER):
		print("Deleting output folder...")
		utils.deleteDirIfPossible()
		print("Deleting output folder done")
		print("Exiting program because parameter "+JUST_DELETE_PARAMETER+" was given ("+JUST_DELETE_PARAMETER+" = just delete)")
		print("\033[K", end='\r')
		sys.exit()

for x in sys.argv:
	if(x == INIT_PARAMETER):
		utils.createDirStructure("")
		print("dir structure created")
		if(not os.path.exists(STANDARD_CONFIG_FILE)):
			f = open(STANDARD_CONFIG_FILE, "w", encoding="utf-8")
			f.write("{\n\
	\"replacements\": {\n\
		\n\
	},\n\
	\"files\": [\n\
		\n\
	],\n\
	\"template\": \".\\\\src\\\\template_file.tmp\",\n\
	\"tsconfig\": \".\\\\src\\\\template_tsconfig.tmp\"\n\
}")
			f.close()
			print(STANDARD_CONFIG_FILE + " file initialized")
		else:
			print(STANDARD_CONFIG_FILE + " already initialized")
		if(not os.path.exists(STANDARD_TEMPLATE_FILE)):
			f = open(STANDARD_TEMPLATE_FILE, "w", encoding="utf-8")
			f.write("<IMPORTS>\n\
\n\
class App<Number> {\n\
	run() :void {\n\
		<TEXT>\n\
		\n\
		return;\n\
	}\n\
}\n\
\n\
let app<Number> = new App<Number>();\n\
try {\n\
	app<Number>.run();\n\
} catch (error) {\n\
	print(error)\n\
}")
			f.close()
			print(STANDARD_TEMPLATE_FILE + " file initialized")		
		else:
			print(STANDARD_TEMPLATE_FILE + " already initialized")

		if(not os.path.exists(STANDARD_TSCONFIG_TEMPLATE_FILE)):
			f = open(STANDARD_TSCONFIG_TEMPLATE_FILE, "w", encoding="utf-8")
			f.write("{\n\
  \"compilerOptions\": {\n\
    /* Visit https://aka.ms/tsconfig.json to read more about this file */\n\
\n\
    /* Basic Options */\n\
    // \"incremental\": true,                         /* Enable incremental compilation */\n\
    \"target\": \"ESNEXT\",                                /* Specify ECMAScript target version: 'ES3' (default), 'ES5', 'ES2015', 'ES2016', 'ES2017', 'ES2018', 'ES2019', 'ES2020', or 'ESNEXT'. */\n\
    \"module\": \"ESNext\",                           /* Specify module code generation: 'none', 'commonjs', 'amd', 'system', 'umd', 'es2015', 'es2020', or 'ESNext'. */\n\
    \"lib\": [\"ESNext\"],                                   /* Specify library files to be included in the compilation. */\n\
    // \"allowJs\": true,                             /* Allow javascript files to be compiled. */\n\
    // \"checkJs\": true,                             /* Report errors in .js files. */\n\
    // \"jsx\": \"preserve\",                           /* Specify JSX code generation: 'preserve', 'react-native', 'react', 'react-jsx' or 'react-jsxdev'. */\n\
    // \"declaration\": true,                         /* Generates corresponding '.d.ts' file. */\n\
    // \"declarationMap\": true,                      /* Generates a sourcemap for each corresponding '.d.ts' file. */\n\
    \"sourceMap\": true,                           /* Generates corresponding '.map' file. */\n\
    // \"outFile\": \"./\",                             /* Concatenate and emit output to single file. */\n\
    // \"outDir\": \"./\",                              /* Redirect output structure to the directory. */\n\
    // \"rootDir\": \"./\",                             /* Specify the root directory of input files. Use to control the output directory structure with --outDir. */\n\
    // \"composite\": true,                           /* Enable project compilation */\n\
    // \"tsBuildInfoFile\": \"./\",                     /* Specify file to store incremental compilation information */\n\
    // \"removeComments\": true,                      /* Do not emit comments to output. */\n\
    // \"noEmit\": true,                              /* Do not emit outputs. */\n\
    // \"importHelpers\": true,                       /* Import emit helpers from 'tslib'. */\n\
    // \"downlevelIteration\": true,                  /* Provide full support for iterables in 'for-of', spread, and destructuring when targeting 'ES5' or 'ES3'. */\n\
    // \"isolatedModules\": true,                     /* Transpile each file as a separate module (similar to 'ts.transpileModule'). */\n\
\n\
    /* Strict Type-Checking Options */\n\
    \"strict\": true,                                 /* Enable all strict type-checking options. */\n\
    \"noImplicitAny\": true,                       /* Raise error on expressions and declarations with an implied 'any' type. */\n\
    // \"strictNullChecks\": true,                    /* Enable strict null checks. */\n\
    // \"strictFunctionTypes\": true,                 /* Enable strict checking of function types. */\n\
    // \"strictBindCallApply\": true,                 /* Enable strict 'bind', 'call', and 'apply' methods on functions. */\n\
    // \"strictPropertyInitialization\": true,        /* Enable strict checking of property initialization in classes. */\n\
    // \"noImplicitThis\": true,                      /* Raise error on 'this' expressions with an implied 'any' type. */\n\
    // \"alwaysStrict\": true,                        /* Parse in strict mode and emit \"use strict\" for each source file. */\n\
\n\
    /* Additional Checks */\n\
    \"noUnusedLocals\": true,                      /* Report errors on unused locals. */\n\
    \"noUnusedParameters\": true,                  /* Report errors on unused parameters. */\n\
    \"noImplicitReturns\": true,                   /* Report error when not all code paths in function return a value. */\n\
    \"noFallthroughCasesInSwitch\": true,          /* Report errors for fallthrough cases in switch statement. */\n\
    \"noUncheckedIndexedAccess\": true,            /* Include 'undefined' in index signature results */\n\
    \"noPropertyAccessFromIndexSignature\": true,  /* Require undeclared properties from index signatures to use element accesses. */\n\
\n\
    /* Module Resolution Options */\n\
    // \"moduleResolution\": \"node\",                  /* Specify module resolution strategy: 'node' (Node.js) or 'classic' (TypeScript pre-1.6). */\n\
    // \"baseUrl\": \"./\",                             /* Base directory to resolve non-absolute module names. */\n\
    // \"paths\": {},                                 /* A series of entries which re-map imports to lookup locations relative to the 'baseUrl'. */\n\
    // \"rootDirs\": [],                              /* List of root folders whose combined content represents the structure of the project at runtime. */\n\
    // \"typeRoots\": [],                             /* List of folders to include type definitions from. */\n\
    // \"types\": [],                                 /* Type declaration files to be included in compilation. */\n\
    // \"allowSyntheticDefaultImports\": true,        /* Allow default imports from modules with no default export. This does not affect code emit, just typechecking. */\n\
    // \"esModuleInterop\": true,                        /* Enables emit interoperability between CommonJS and ES Modules via creation of namespace objects for all imports. Implies 'allowSyntheticDefaultImports'. */\n\
    // \"preserveSymlinks\": true,                    /* Do not resolve the real path of symlinks. */\n\
    // \"allowUmdGlobalAccess\": false,                /* Allow accessing UMD globals from modules. */\n\
\n\
    /* Source Map Options */\n\
    // \"sourceRoot\": \"\",                            /* Specify the location where debugger should locate TypeScript files instead of source locations. */\n\
    // \"mapRoot\": \"\",                               /* Specify the location where debugger should locate map files instead of generated locations. */\n\
    // \"inlineSourceMap\": true,                     /* Emit a single file with source maps instead of having a separate file. */\n\
    // \"inlineSources\": true,                       /* Emit the source alongside the sourcemaps within a single file; requires '--inlineSourceMap' or '--sourceMap' to be set. */\n\
\n\
    /* Experimental Options */\n\
    // \"experimentalDecorators\": true,              /* Enables experimental support for ES7 decorators. */\n\
    // \"emitDecoratorMetadata\": true,               /* Enables experimental support for emitting type metadata for decorators. */\n\
\n\
    /* Advanced Options */\n\
    \"skipLibCheck\": true,                           /* Skip type checking of declaration files. */\n\
    \"forceConsistentCasingInFileNames\": true,        /* Disallow inconsistently-cased references to the same file. */\n\
    \"watch\": true\n\
  },\n\
  \"files\": [<FILES>]\n\
  <EXTENDS>\n\
}")
			f.close()
			print(STANDARD_TSCONFIG_TEMPLATE_FILE + " initialized")
		else:
			print(STANDARD_TSCONFIG_TEMPLATE_FILE + " already initialized")
		sys.exit()

templateConfigTranspileFilename = STANDARD_CONFIG_FILE
try:
	ind = sys.argv.index(CONFIG_PARAMETER)
	sys.argv.remove(CONFIG_PARAMETER)
	if(ind < len(sys.argv)):
		templateConfigTranspileFilename = sys.argv[ind]
		del sys.argv[ind]
	else:
		print("no filename given with parameter "+CONFIG_PARAMETER+". Proceeding with default config file " + templateConfigTranspileFilename)
except:
	print("parameter "+CONFIG_PARAMETER+" not found. Proceeding with default config file " + templateConfigTranspileFilename)


templateFilename = ""
try:
	ind = sys.argv.index(TEMPLATE_PARAMETER)
	sys.argv.remove(TEMPLATE_PARAMETER)
	if(ind < len(sys.argv)):
		templateFilename = sys.argv[ind]
		del sys.argv[ind]
	else:
		print("no filename given with parameter "+TEMPLATE_PARAMETER+". Looking for template file in config file...")
except:
	print("parameter "+TEMPLATE_PARAMETER+" not found. Looking for template file in config file...")

tsConfigFilename = ""
try:
	ind = sys.argv.index(TSCONFIG_TEMPLATE_PARAMETER)
	sys.argv.remove(TSCONFIG_TEMPLATE_PARAMETER)
	if(ind < len(sys.argv)):
		tsConfigFilename = sys.argv[ind]
		del sys.argv[ind]
	else:
		print("no filename given with parameter "+TSCONFIG_TEMPLATE_PARAMETER+". Looking for tsconfig file in config file...")
except:
	print("parameter "+TSCONFIG_TEMPLATE_PARAMETER+" not found. Looking for tsconfig file in config file...")

jsonFile = ""
try:
	configFile = open(templateConfigTranspileFilename, "r")
	jsonFile = json.load(configFile)
	configFile.close()
except:
	print("")
	print("no "+templateConfigTranspileFilename+" file found. Start with \"python transpile.py init\" first to create the base structure")
	print("")
	sys.exit()

if(len(templateFilename) <= 0):
	try:
		templateFilename = str(jsonFile["template"])
		templateFilename = templateFilename.strip()
		if(len(templateFilename) <= 0):
			templateFilename = STANDARD_TEMPLATE_FILE
			print("config file: \"template\" is empty - Proceeding with default template file " + templateFilename)
		else:
			print("config file: template found - Proceeding with file " + templateFilename)
	except:
		templateFilename = STANDARD_TEMPLATE_FILE
		print("config file: does not include part \"template\": \"<FileName>\" - Proceeding with default template file " + templateFilename)

templateFile = open(templateFilename, "r")
templateText = templateFile.read()
templateFile.close()

if(len(tsConfigFilename) <= 0):
	try:
		tsConfigFilename = str(jsonFile["tsconfig"])
		tsConfigFilename = tsConfigFilename.strip()
		if(len(tsConfigFilename) <= 0):
			tsConfigFilename = STANDARD_TSCONFIG_TEMPLATE_FILE
			print("config file: \"tsconfig\" is empty - Proceeding with default tsconfig file " + tsConfigFilename)
		else:
			print("config file: tsconfig found - Proceeding with file " + tsConfigFilename)
	except:
		tsConfigFilename = STANDARD_TSCONFIG_TEMPLATE_FILE
		print("config file: does not include part \"tsconfig\": \"<FileName>\" - Proceeding with default tsconfig file " + tsConfigFilename)

tsConfigTemplateFile = open(tsConfigFilename, "r", encoding="utf-8")
tsConfigFileText = tsConfigTemplateFile.read()
tsConfigTemplateFile.close()

try:
	configFiles = jsonFile["files"]
	if(len(configFiles) > 0):
		for x in configFiles:
			sys.argv.append(str(x))
	else:
		print("config file: does not include any files - nothing to append")
except:
	print("config file: does not include part \"files\": [...] - skip appending")


if(len(sys.argv) <= 1):
	print("ERROR: no filenames given, nothing to do!")
	print("    usage: python .\\transpile.py <Filename2> <Filename2> <FilenameN> for creating the *.ts files")
	print("    usage: python .\\transpile.py "+JUST_DELETE_PARAMETER+" for deleting the output file")
	print("")
	print("Parameter:")
	print("    "+TEMPLATE_PARAMETER+" <FileName> template file for creating the *.ts files.")
	print("    "+CONFIG_PARAMETER+" <FileName> config file for replacing arbitrary words or identifier.")
	print("    "+TSCONFIG_TEMPLATE_PARAMETER+" <FileName> tsconfig file to create the structure from.")
	print("    "+JUST_DELETE_PARAMETER+" if given, it JUST DELETES ("+JUST_DELETE_PARAMETER+") the output folder and does nothing else.")
	print("")
	print("examples:")
	print("    python .\\transpile.py .\\src\\test.txt .\\src\\test2.txt")
	print("    python .\\transpile.py "+JUST_DELETE_PARAMETER)
	print("")
	sys.exit()

print("Deleting output folder...")
utils.deleteDirIfPossible()
print("Deleting output folder done")

try:
	possibleType = ["CDateTime", "CMoney", "CTable", "int", "double", "CString", "BOOL"]

	filesAlreadyUsed = []
	for x in sys.argv:
		if(x == JUST_DELETE_PARAMETER or x == sys.argv[0]):
			continue
		ind = -1
		try:
			ind = filesAlreadyUsed.index(str(x))
		except:
			pass
		
		if(ind >= 0):
			print(str(x) + " already used - skipping this file")
			continue

		basePath = os.path.dirname(x)
		if(len(basePath) > 0):
			if(basePath[-1:] != "\\" and basePath[-1:] != "/"):
				basePath = basePath + "/"

		f = open(str(x), "r", 4096, "utf-8")
		filesAlreadyUsed.append(str(x))

		# create base tsconfig file
		if(not os.path.exists(basePath + "tsconfig.json")):
			baseTSConfigFile = utils.createFile(basePath + "tsconfig.json")
			TSConfigFileTextTmp = tsConfigFileText
			TSConfigFileTextTmp = TSConfigFileTextTmp.replace("<EXTENDS>", "")
			TSConfigFileTextTmp = TSConfigFileTextTmp.replace("<FILES>", "")
			baseTSConfigFile.write(TSConfigFileTextTmp)
			baseTSConfigFile.close()

		t = f.read()
		t = t.splitlines()
		f.close()
		allScripts = []

		actScript = ""
		scriptName = ""
		scriptNumber = ""
		i = 0
		for s in t:
			s = s.strip()
			start = s.find("SCRIPT:")
			end = s.find("ENDSCRIPT")
			if(start == 0):
				endScriptNumber = s.find(",", start + 1)
				try:
					scriptNumbertmp = int(s[7:endScriptNumber])
					if(scriptNumbertmp > 0):
						scriptNumber = str(scriptNumbertmp)
				except:
					pass
				
				endScriptName2 = s.find(",", endScriptNumber + 1)
				if(endScriptName2 >= 0):
					scriptName = s[endScriptNumber+1:endScriptName2]
				else:
					scriptName = s[endScriptNumber+1:]

				scriptName = scriptName.replace(">", "")
				scriptName = scriptName.replace("/", "-")
				scriptName = scriptName.replace(":", "-")

				actScript = ""
				continue
			if(end == 0 and len(scriptNumber) > 0):
				allScripts.append([actScript, scriptName, scriptNumber])
				continue
			i = i + 1
			actScript += s + "\n"

		i = 0
		for actScript in allScripts:
			scriptNumber = actScript[2]
			currentScriptName = scriptNumber + actScript[1] + ".ts"
			currentFunctionScriptName = scriptNumber + "Functions" + actScript[1] + ".ts"
			f = utils.createFile(basePath + currentScriptName.split(".")[0].strip() + "/" + currentScriptName)

			print("creating ", scriptNumber, actScript[1], "...\033[K", end='\r', flush=True)
			if(f):
				temp = templateText
				script = ""
				actScript = actScript[0].splitlines()
				isFunction = False
				functions = ""
				for actLine in actScript:
					
					transposedLine = utils.transposeFunction(actLine)
					if(transposedLine != actLine):
						functions = functions + "\n" + transposedLine
						isFunction = not isFunction
						continue

					actLine = transposedLine
					replacements = jsonFile["replacements"]
					for x in replacements:
						actLine = actLine.replace(x, replacements[x])
					
					actLine = actLine.replace("Call:", "Utils" + str(scriptNumber) + ".")
					actLine = actLine.replace("==", "TEMPUNDSOHAHAHAHAHAHA")
					actLine = actLine.replace(">=", "GRÖßERGLEICH")
					actLine = actLine.replace("<=", "KLEINERGLEICH")
					actLine = actLine.replace("==", "TEMPUNDSOHAHAHAHAHAHA")
					actLine = actLine.replace("!=", "UNGLEIUCHUNDSOHAHA")
					actLine = actLine.replace("=", " =")
					actLine = actLine.replace(",", ", ")
					actLine = actLine.replace("  ", " ")
					actLine = actLine.replace("UNGLEIUCHUNDSOHAHA", "!=")
					actLine = actLine.replace("TEMPUNDSOHAHAHAHAHAHA", "==")
					actLine = actLine.replace("GRÖßERGLEICH", ">=")
					actLine = actLine.replace("KLEINERGLEICH", "<=")

					actLine = actLine.split(" ")
					j = 0
					while(j < len(actLine)):
						act = actLine[j].strip()
						if(len(act) > 0):
							try:
								ind = possibleType.index(act)
								if(j + 1 < len(actLine)):

									tmp = utils.replaceTypes(act)
									tmp = " :" + tmp.strip()

									act = "let " + actLine[j + 1].strip(";")
									
									if(j + 2 >= len(actLine)):
										tmp = tmp + ";"
									actLine[j + 1] = tmp
							except:
								try:
									act = replacements[act]
								except:
									found1 = act.find("D.")
									found2 = act.find("F.")
									found3 = act.find("S.")
									found4 = act.find("H.")
									if((found1 == 0) or (found2 == 0) or (found3 == 0) or (found4 == 0)):
										act = act[2:]
						if(not isFunction):
							script = script + act + " "
						else:
							functions = functions + act + " "

						j = j + 1
					if(not isFunction):
						script = script + "\n"
					else:
						functions = functions + "\n"

				
				includesText = ""
				if(len(functions) > 0):
					t = utils.createFile(basePath + currentScriptName.split(".")[0].strip() + "/" + currentFunctionScriptName)
					t.write(functions)
					t.close()
					if(len(includesText) > 0):
						includesText = includesText + "\n"
					includesText = includesText + "import * as Utils" + str(scriptNumber) + " from \"./" + currentFunctionScriptName.split(".")[0].strip() + ".js\""

				# create extending config file
				if(not os.path.exists(basePath + currentScriptName.split(".")[0].strip() + "/" + "tsconfig.json")):
					baseTSConfigFile = utils.createFile(basePath + currentScriptName.split(".")[0].strip() + "/" + "tsconfig.json")
					TSConfigFileTextTmp = tsConfigFileText
					TSConfigFileTextTmp = TSConfigFileTextTmp.replace("<EXTENDS>", ",\t\"extends\":\"./../tsconfig.json\"")
					TSConfigFileTextTmp = TSConfigFileTextTmp.replace("<FILES>", "")
					baseTSConfigFile.write(TSConfigFileTextTmp)
					baseTSConfigFile.close()

				temp = temp.replace("<TEXT>", script)
				temp = temp.replace("<Number>", scriptNumber)
				temp = temp.replace("<IMPORTS>", includesText)
				f.write(temp)
				f.close()
			i = i + 1
			if(i > 1):
				pass


except Exception as e:
	print(e)

print("Finished transpiling\033[K")