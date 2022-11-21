import shutil
import glob
import os
import time
import datetime

# In seconds e.g. 10 minute autosave intervals = 600 (default value)
autosave_frequency=600
# Number of backup save files to keep. Default value is 5, maximum value is 9.
# Exceeding the maximum number will result in this script failing unless adjustments are made to the code ;)
backups_num=5

print("Running ironman autosave script..\nAutosave frequency set to: "+str(datetime.timedelta(seconds=autosave_frequency)))

def CompareModifiedTimes(saveGameFilePath, backupGameFilePath):
    if os.path.exists(backupGameFilePath):
        backupTime = os.path.getmtime(backupGameFilePath)
    else:
        backupTime = 0
    saveTime = os.path.getmtime(saveGameFilePath)
    return (backupTime<saveTime)

def IncrementVersionNumbers(fileName, filePath):
    newVersion=f[:-4]
    newVersion=str(int(newVersion[-1:])+1)
    os.rename(filePath,filePath[:-5]+newVersion+".ck3")

if not os.path.exists("./Auto-Backups"):
    os.makedirs("./Auto-Backups")

while(True):
    savedGameModified=False
    for saveFile in glob.iglob('./*.ck3'):
        saveTitle = saveFile.replace('.\\','')
        saveTitle = saveTitle.replace('.ck3','')
        initialTitle=saveTitle+"/"+saveTitle+"_BACKUP_1.ck3"

        if not os.path.exists("./Auto-Backups/"+saveTitle):
            os.makedirs("./Auto-Backups/"+saveTitle)

        allFiles = [f for f in os.listdir("./Auto-Backups/"+saveTitle+"/")]
        allFiles.sort()

        if CompareModifiedTimes(saveFile,"./Auto-Backups/"+initialTitle):
            savedGameModified=True
            print("Backing up saved game: "+saveTitle)

            if len(allFiles)>(backups_num-1):
                numOverMax=0
                for f in allFiles[(backups_num-1):]:
                    os.remove("./Auto-Backups/"+saveTitle+"/"+f)
                    numOverMax+=1
                allFiles.reverse()
                for i in range(0,numOverMax):
                    allFiles.pop(0)
                for f in allFiles[:(backups_num-1)]:
                    IncrementVersionNumbers(f,"./Auto-Backups/"+saveTitle+"/"+f)
            else:
                allFiles.reverse()
                for f in allFiles:
                    IncrementVersionNumbers(f,"./Auto-Backups/"+saveTitle+"/"+f)
            shutil.copy2("./"+saveFile,"./Auto-Backups/"+initialTitle)
        else:
            continue
    if savedGameModified:
        print("")
    else:
        print("All saved game backups are up-to-date\n")
    for i in range(1,6):
        time.sleep(autosave_frequency/5)
        if i!=5:
            remainingSeconds=autosave_frequency-(autosave_frequency/5*i)
            print("Next backup attempt in "+str(datetime.timedelta(seconds=remainingSeconds)))
