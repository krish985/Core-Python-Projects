from pathlib import Path
import glob
import os

# Helper func to list all files and folder.
def listAllFileAndFolder() :
    all_file = glob.glob("*")
    
    for i in range(len(all_file)) :
        print(f"{i+1} : {all_file[i]}")


# 1. create file function.
def createFile() :
    listAllFileAndFolder()
    try :
        name = input("Enter a new file name :-")
        p = Path(name)
        if not p.exists() :
            text = input("Write content :-")
            with open(name , 'w') as f :
                f.write(text)
                print(f'file : {name} created succesfull!')

        else :
            print("file already exist")
    except Exception as err :
        print(f"Error while creating a file : {err}")
  

# 2. Update the file.
def updateFile() :
    listAllFileAndFolder()
    try :
        print("Press 1 to Override the file")
        print("Press 2 Append data into same file")
        file = input("First enter the file name :-")
        instruction = int(input("Enter number what you want :-"))
        p = Path(file)
        if p.exists() :
            if instruction == 1 :
                with open(file , 'w') as f :
                    text = input("What you want to write :-")
                    f.write(text)
                    print(f"File : {file} Override succesfull!")
            elif instruction == 2 :
                with open(file , 'a') as f :
                    text = input("What you want to write :-")
                    f.write("\n"  + text)
                    print(f"File : {file} Append data succesfull!")

        else :
            print(f"{file} does not exist")
    except Exception as err :
        print(f"Error while updating files : {err}")
        

# 3. Read file func.
def readFile() :
    listAllFileAndFolder()
    try :
        file = input("Which file you want to read enter :-")
        p = Path(file) 
        if p.exists() :
            with open(file , 'r') as f :
                data = f.read()
                print(f"\nContent\n" , data)
        else :
            print("File does not exist!")
            readFile()
    except Exception as err :
        print(f"Error while Reading a file : {err}")


# 4. Delete file func.
def deleteFile() :
    listAllFileAndFolder()
    try :
        file = input("Which files you want to delete enter name :-")
        p = Path(file) 
        if  p.exists() :
            os.remove(file)
            print(f"File : {file} Deleted succesfull!")
        else :
            print("Sorry input file is not exist!")
    except Exception as err :
        print(f"Error while deleting a file : {err}")



print("Press 1 to Create a File -:")
print("Press 2 to Update a File -:")
print("Press 3 to Read a File -:")
print("Press 4 to Delete a File -:")

steps = int(input("Enter a Number what you want to do : "))

if steps == 1 :
    createFile()
elif steps == 2 :
    updateFile()
elif steps == 3 :
    readFile()
elif steps == 4 :
    deleteFile()
else :
    print("Invalid Choice")