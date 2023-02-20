# One Punch Man Downloader
A very simple python script to download One Punch Man manga chapters in .cbz format.\
Chapters are downloaded from https://gist.githubusercontent.com/funkyhippo/1d40bd5dae11e03a6af20e5a9a030d81/raw/?

## Installation
Just download `opmd.exe` from the latest release.

## Usage
Open a terminal where you saved the .exe and run the script.
```bash
./opmd.exe [-a] [-f FIRSTCHAPTER] [-l LASTCHAPTER] [-p TARGETPATH] [-h]
```

## Arguments
Use `-h` or `--help` for command usage.\
Use `-a` or `--all` to download every chapter that is missing in the target path.\
Use `-f` or `--first` to choose the first or only chapter to be downloaded. `FIRSTCHAPTER` should be an integer or a decimal number.\
Use `-l` or `--last` to choose the last chapter to be downloaded. Don't use this if you only want to download one chapter. `LASTCHAPTER` should be an integer or a decimal number.\
Use `-p` or `--path` to choose the target path where the chapters will be downloaded to. Will be OnePunchMan by default. `TARGETPATH` should be a directory.
