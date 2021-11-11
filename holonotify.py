#!/usr/bin/env python

import os
import time
import platform

import urllib.request
import json

import utils

liveAnnouced = list()
live = list()
ended = list()
blacklist = list()
running = True
checkedPs = False
psCount = 0

def updateValues():
    global live, ended, blacklist
    blacklist = utils.getBlacklist()

    with urllib.request.urlopen("https://api.holotools.app/v1/live") as url:
        holoapi = json.loads(url.read().decode())
        live = holoapi["live"]
        ended = holoapi["ended"]

def main():
    updateValues()
    for ch in live:
        notBlacklist = True
        chName = ch["channel"]["name"].lower()

        # check if the vtuber is in the blacklist
        for name in blacklist:
            if (name in chName):
                notBlacklist = False
                break
        # check if the live has already been announces and its not blacklisted
        if(chName not in liveAnnouced and notBlacklist):
            chIcon = utils.getIcon(chName)

            if(platform.system() == "Windows"):
                from plyer import notification
                notification.notify(title=chName + " is live!", message=ch["title"])
            else:
                os.system(f'''notify-send -i {chIcon} "{chName} is live!" "{ch["title"]}"''')

            liveAnnouced.append(chName)
        # check if the live has ended and remove it from the live already announced
        if(ch["yt_video_key"] in ended):
            liveAnnouced.remove(ch["channel"]["name"])

def linuxCheckProc():
    global checkedPs, psCount, running

    if checkedPs == False and platform.system() == "Linux":
        import psutil
        for pid in psutil.pids():
            try:
                p = psutil.Process(pid)
                if p.name() == "python":
                    if psCount >= 1:
                        running = False
                        break
                    if "holonotify" in p.cmdline()[1]:
                        psCount +=  1
            except:
                continue
        checkedPs = True

def windowsCheckProc():
    # TODO
    pass

if __name__ == "__main__":
    while running:
        main()

        # If there's another instance running, show who's live and quit
        linuxCheckProc()
        windowsCheckProc()
        
        if running:
            time.sleep(60*5)
