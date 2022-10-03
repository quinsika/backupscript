import subprocess

def backupfunc():
    print ("starting backup")
    subprocess.run(["sleep", "5"])
    print ("backup complete")

if __name__ == "__main__":
    backupfunc()

