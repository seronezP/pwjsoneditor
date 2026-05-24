# PanzerWar JSON Editor
___

This small program helps to edit the `achievements.json` of panzerwar savefile, since simply opening the file is not enough, as it is encrypted.



## Installation

### 1. clone this repository
```bash
git clone https://github.com/seronezP/pwjsoneditor.git
cd pwjsoneditor

```
### 2. install virtual environment

```bash
python3.12 -m venv venv
source venv/bin/activate
``` 
     
### 3. install dependencies
```bash   
pip install -r requirements.txt 
```

## how to use

1. To change a file, you need to specify the path to the file for decryption in the decode.py files, and for reverse encoding, the path to the folder where the file will be saved(its can be any folder would you like) 

2. click button `decode` for decode file

3. change everything you need(Editing instructions will be available later.)

4. click button `encode`

5. move the modified file to game folder 

(editing file now so far only manually)
