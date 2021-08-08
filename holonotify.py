#!/usr/bin/env python

import os
import threading
import time

import urllib.request
import json

import utils

liveAnnouced = list()
live = list()
ended = list()
blacklist = list()

def updateValues():
    global live, ended
    with urllib.request.urlopen("https://api.holotools.app/v1/live") as url:
        holoapi = json.loads(url.read().decode())
        live = holoapi["live"]
        ended = holoapi["ended"]

    time.sleep(60*5)
    updateValues()


def main():
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

    time.sleep(60*5)

if __name__ == "__main__":
    thread = threading.Thread(target=updateValues)
    thread.start()

    time.sleep(5)
    while True:
        blacklist = utils.getBlacklist()
        main()
