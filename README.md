# One-Offs
One-Off utility scripts for miscellaneous purposes

## Contents
<details>
    <summary>ironman_autosave.py</summary>

A python script to automatically back up Crusador Kings 3 savefiles in order to circumvent ironman-mode restrictions.
It should be saved to and run from the CK3 savefile directory (Windows Default: [dir]:/Users/[User]/Documents/Paradox Interactive/Crusader Kings III/save games) via a console: 
```
cd [dir]:/Users/[User]/Documents/Paradox Interactive/Crusader Kings III/save games
python ironman_autosave.py
```
***It has not been extensively tested and there may be some operational issues.***

Two that I am pretty sure may be a problem are:
* The game overwriting/loading a save whilst it is being backed-up may cause the script to fail or save-file corruption
> To combat this, it is recommended that the autosave interval is set to be reasonably spaced apart, the more often you create a backup the more likely the game might be trying to save at the same time.
* Trying to retain more than 9 backups
> This script is not written to handle more than that due to how the backup filenames are overwritten. This *could* be easily remedied with a little bit of extra code but I didn't need more than 5 (the default) for my purposes so it's left as an exercise for the reader..
</p></details>
