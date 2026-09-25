import os
print("type cmds for commands")
while True :
	command=input("Test:>")
	if command=="shutdown" :
		shutdown=input("""Do you want to actually shutdown your computer (it only shut downs the code, not the computer)
		Y or N
		""")
		if shutdown=="y":
			break
		elif shutdown=="Y":
			break
		elif shutdown=="N":
			print("ok, the script is not ended yet")
		elif shutdown=="n":
			print("ok, not ended")
	elif command=="cat":
		cat=input("Make a new text [Y] or [N] : ")
		if cat=="n":
			print("ok, no text files for you")
		elif cat=="N":
			print("Okay, no text files for you (cooler)")
		elif cat=="y" :
			catname=input("name? : ")
			content=input("content? (only one-line) : ")
			catwriter=open(catname, "w+")
			catwriter.write(content)
			catwriter.close()
			print("now look into the directory your python compiler is connected to, the file is there (its real i tested it myself)")
		elif cat=="Y":
			catname=input("name? : ")
			content=input("content? (only one-line) : ")
			catwriter=open(catname, "w+")
			catwriter.write(content)
			catwriter.close()
			print("now look into the directory your python compiler is connected to, the file is there (its real i tested it myself)")
	elif command=="cd":
	    drive = input("Enter drive (C, D, E): ")
	    try:
	        os.chdir(drive + ":\\")
	        print("Now in:", os.getcwd())
	    except FileNotFoundError:
	        print("That drive doesn't exist.")
	elif command=="mkdir":
		di=input("folder name? : ")
		try:
			os.mkdir(di)
			print("folder created")
		except FileExistsError:
			print("that folder already exists!")
	elif command=="bugfix":
		print("""version 1.1.1 - changed typo "shutdowm" to "shutdown", and changed every "if" to "elif" to make it multi-use
version 1.2.1 - fixed "cd" command, it now simply tells you instead of crashing that the drive simply doesn't exist and imported os cuz that's the bigger fish to catch, made it so that read doesn't crash when the file doesn't exist 
version 1.3.1 - fixed "mkdir" meaning in cmds and made mkdir stable with already existing folders""")
	elif command=="version":
		print("idk's cmd 1.4.0")
	elif command=="cmds":
		print("""shutdown - exits the code, does NOT shut down your computer
cat - overwrites, writes and creates files, type it raw and it'll work, else it won't work
read - reads files, read-only, only reads 255 characters, type it raw and it'll work, else it won't work
cd - changes the current drive
mkdir - creates a folder
version - shows the version
cmds - the one you are viewing
added - added stuff throughout the history
pwd - show the current directory
rename - renames a file or folder, type it raw and it'll work, else it won't work
echo - you can now not type it raw like "echo", you now have to "echo Hello, world!"
""")
	elif command=="added":
		print("""added stuff throughout the history :
1.0.0 - shutdown, cat, cd, mkdir
1.1.1 - version, cmds, added, read
1.2.0 - added "type cmds for commands", this was added during the 1.1.1 thing and removed cuz i accidentally didn't save the file and i had to rewrite everything
1.3.0 - mkdir, rename, pwd, and fixed mkdir
1.4.0 - echo, more info about echo in cmds""")
	elif command=="read":
		readname=input("name of the file? (only reads 255 characters) : ")
		try:
			readreader=open(readname, "r")
			print(readreader.read(255))
			readreader.close()
		except FileNotFoundError:
			print("404! that's an error, it doesn't exist!")
	elif command=="help":
		print("""contact the programmer at mrymarfahmdy@gmail.com, contact the idea maker at maryam1358babazade@gmail.com
this is an thing created for fun""")
	elif command=="pwd":
		print(os.getcwd())
	elif command=="rename":
		name=input("what do you wanna rename? : ")
		renameto=input(" and what do you wanna rename it to? : ")
		try:
			os.rename(name, renameto)
		except FileNotFoundError:
			print("that file doesn't exist, 404!")
	elif command.startswith("echo "):
		str=command[5:]
		print(str)
	else:
		print("404! that command doesn't exist")
