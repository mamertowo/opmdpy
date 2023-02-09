import requests
import json
import os
import shutil
from clint.textui import progress
import sys, getopt
import math
from decimal import *

#Downloads every page to a new folder, zips it, changes the extension to .cbz and finally deletes the folder.
def downloadChapter(chapter, index, targetPath):
    print("Downloading chapter " + index)

    chapterDir = os.path.join(targetPath, index)

    #Delete the temporal folder if it already exists
    if (os.path.isdir(chapterDir)):
        shutil.rmtree(chapterDir)
    os.makedirs(chapterDir)

    #Download every page
    i = 1
    for pageURL in progress.bar(chapter, expected_size=len(chapter)):
        page = requests.get(pageURL)
        pageFile = open(os.path.join(chapterDir, str(i) + ".png"), "wb") 
        pageFile.write(page.content)
        pageFile.close()
        i += 1

    #Zip the folder, change the extension to .cbz and delete the folder
    shutil.make_archive(chapterDir, "zip", chapterDir)
    os.rename(chapterDir + ".zip", chapterDir + ".cbz")
    shutil.rmtree(chapterDir)


def downloadChapters(targetPath, firstChapter, lastChapter, sourcePaths):
    #Self explanatory
    while (firstChapter <= lastChapter):
        if (firstChapter == math.floor(firstChapter)):
            chapterIndex = str(int(firstChapter))
        else:
            chapterIndex = str(firstChapter)
        if (os.path.exists(os.path.join(targetPath, chapterIndex + '.cbz'))):
            print("Chapter " + chapterIndex + " is already in target path")
        elif (chapterIndex in sourcePaths["chapters"]):
            chapter = sourcePaths["chapters"][chapterIndex]["groups"]["/r/OnePunchMan"]
            downloadChapter(chapter, chapterIndex, targetPath)
        else:
            if (firstChapter == math.floor(firstChapter)):
                print("Couldn't find chapter " + chapterIndex)
        firstChapter += Decimal(0.1)
        firstChapter = round(firstChapter, 1)


def main(argv):
    #Self explanatory
    sourceURL = "https://gist.githubusercontent.com/funkyhippo/1d40bd5dae11e03a6af20e5a9a030d81/raw/?"
    sourcePaths = json.loads(requests.get(sourceURL).content)
    totalChapters = 0
    for chapter in sourcePaths["chapters"]:
        if (float(chapter) > totalChapters):
            totalChapters = float(chapter)
    firstChapter = Decimal(0)
    lastChapter = Decimal(0)
    targetPath = ""
    try:
        opts, args = getopt.getopt(argv, "ahf:l:p:", ["first=","last=","path=","help","all"])
    except getopt.GetoptError:
        print('Syntax error. Use "opmd.py -h" for help')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-a", "--all"):
            firstChapter = Decimal(1)
            lastChapter = totalChapters
        elif (opt in ("-f", "--first")) and (firstChapter == 0):
            firstChapter = Decimal(arg)
        elif ((opt in ("-l", "--last")) and (lastChapter == 0)):
            lastChapter = Decimal(arg)
        elif opt in ("-p", "--path"):
            targetPath = arg
        elif opt in ("-h", "--help"):
            print("Usage: python opmd.py [-a] [-f FIRSTCHAPTER] [-l LASTCHAPTER] [-p TARGETPATH] [-h]\n\n")
            print("-a, --all:   Downloads every chapter that is missing in the target path\n")
            print("-f, --first: Choose the first or only chapter to be downloaded\n")
            print("-l, --last:  Choose the last chapter to be downloaded. Don't use this if you only want to download one chapter\n")
            print("-p, --path:  The target path where the chapters will be downloaded to. Will be OnePunchMan by default\n")
            print("-h, --help:  Shows this message")
            sys.exit()
    if lastChapter < firstChapter:
        lastChapter = firstChapter
    if targetPath == "":
        targetPath = "OnePunchMan"
    downloadChapters(targetPath, firstChapter, lastChapter, sourcePaths)
    print("Done!")
    sys.exit()


if __name__ == "__main__":  #Not imported
   main(sys.argv[1:])