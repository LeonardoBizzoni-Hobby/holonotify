#!/usr/bin/env python

import os
import threading
import time
import psutil

import urllib.request
import json

import utils

liveAnnouced = list()
live = list()
ended = list()
blacklist = list()

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

        for name in blacklist:
            if (name in chName):
                notBlacklist = False
                break
        
        if(chName not in liveAnnouced and notBlacklist):
            chIcon = utils.getIcon(chName)
            os.system(f'''notify-send -i {chIcon} "{chName} is live!" "{ch["title"]}"''')
            liveAnnouced.append(chName)

        if(ch["yt_video_key"] in ended):
            liveAnnouced.remove(ch["channel"]["name"])

if __name__ == "__main__":
    running = True
    checkedPs = False
    psCount = 0

    while running:
        main()

        # If there's another instance running, show who's live and quit
        if checkedPs == False:
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

        if running:
            time.sleep(60*5)
