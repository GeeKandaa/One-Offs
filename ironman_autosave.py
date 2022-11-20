import shutil
import glob
import os
import time
import datetime

# In seconds e.g. 15 minute autosave intervals = 900 (default value)
autosave_frequency=900
# Number of backup save files to keep. Default value is 5, maximum value is 9.
# Exceeding the maximum number will result in this script failing unless adjustments are made to the code ;)
backups_num=5

print("Running ironman autosave script..\nAutosave frequency set to: "+str(datetime.timedelta(seconds=autosave_frequency)))


if not os.path.exists("./Auto-Backups"):
    os.makedirs("./Auto-Backups")
while(True):
    print("Backing up savefiles..")
    for saveFile in glob.iglob('./*.ck3'):
        saveTitle = saveFile.replace('.\\','')
        saveTitle = saveTitle.replace('.ck3','')

        if not os.path.exists("./Auto-Backups/"+saveTitle):
            os.makedirs("./Auto-Backups/"+saveTitle)
        allFiles = [f for f in os.listdir("./Auto-Backups/"+saveTitle+"/")]
        allFiles.sort()
        if len(allFiles)>(backups_num-1):
            numOverMax=0
            for f in allFiles[(backups_num-1):]:
                os.remove("./Auto-Backups/"+saveTitle+"/"+f)
                numOverMax+=1
            allFiles.reverse()
            for i in range(0,numOverMax):
                allFiles.pop(0)
            for f in allFiles[:(backups_num-1)]:
                newVersion=f[:-4]
                newVersion=str(int(newVersion[-1:])+1)
                os.rename("./Auto-Backups/"+saveTitle+"/"+f,"./Auto-Backups/"+saveTitle+"/"+f[:-5]+newVersion+".ck3")
        else:
            allFiles.reverse()
            for f in allFiles:
                newVersion=f[:-4]
                newVersion=str(int(newVersion[-1:])+1)
                os.rename("./Auto-Backups/"+saveTitle+"/"+f,"./Auto-Backups/"+saveTitle+"/"+f[:-5]+newVersion+".ck3")
        shutil.copy2("./"+saveFile,"./Auto-Backups/"+saveTitle+"/"+saveTitle+"_BACKUP_1.ck3")
    print("\n")
    time.sleep(autosave_frequency)