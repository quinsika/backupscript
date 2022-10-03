import subprocess

def backupfunc():
    print ("starting backup")
    subprocess.run(["sleep", "5"])
    print ("backup complete")

def move_to_s3():
    print("moving to s3")

if __name__ == "__main__":
    backupfunc()
    move_to_s3()

