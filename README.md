# One Punch Man Downloader
A very simple python script to download One Punch Man manga chapters in .cbz format.

## Installation
Clone or download the repository and cd into it
```bash
git clone https://github.com/mamertowo/opmdpy
cd opmdpy
```
Make a new virtual environment
```bash
python -m venv .venv
```
Activate the virtual environment
```bash
.\.venv\Scripts\Activate.ps1
```
Install dependencies
```bash
pip install -r requirement.txt
```

## Usage
Activate the virtual environment
```bash
.\.venv\Scripts\Activate.ps1
```
Run the script
```bash
python opmd.py [-a] [-f FIRSTCHAPTER] [-l LASTCHAPTER] [-p TARGETPATH] [-h]
```

## Arguments
Use `-h` or `--help` for command usage.\
Use `-a` or `--all` to download every chapter that is missing in the target path.\
Use `-f` or `--first` to choose the first or only chapter to be downloaded. `FIRSTCHAPTER` should be an integer or a decimal number.\
Use `-l` or `--last` to choose the last chapter to be downloaded. Don't use this if you only want to download one chapter. `LASTCHAPTER` should be an integer or a decimal number.\
Use `-p` or `--path` to choose the target path where the chapters will be downloaded to. Will be OnePunchMan by default. `TARGETPATH` should be a directory.
