import os

def getBlacklist():
    blacklist = list()
    blacklistFile = os.path.expanduser("~") + "/.config/holoBlacklist"

    if (os.path.isfile(blacklistFile)):
        with open(blacklistFile, "r") as f:
            for x in f.read().splitlines():
                if(x == "fubuki" or x == "shirakami"):
                    blacklist.append("フブキ")
                elif (x == "akirose" or x == "aki" or x == "rosenthal"):
                    blacklist.append("アキロゼ")
                else:
                    blacklist.append(x)

    return blacklist

def getIcon(name):
    abspath = os.path.dirname(os.path.abspath(__file__)) + "/Icons/"

    # JP
    if ("フブキ" in name):
        return abspath + "fubuki.jpg"
    elif ("pekora" in name):
        return abspath + "pekora.jpg"
    elif ("polka" in name):
        return abspath + "polka.jpg"
    elif ("rushia" in name):
        return abspath + "rushia.jpg"
    elif ("kanata" in name):
        return abspath + "kanata.jpg"
    elif ("sora" in name):
        return abspath + "sora.jpg"
    elif ("roboco" in name):
        return abspath + "roboco.jpg"
    elif ("miko" in name):
        return abspath + "miko.jpg"
    elif ("夜空メルチャンネル" in name):
        return abspath + "mel.jpg"
    elif ("アキロゼ" in name):
        return abspath + "akirose.jpg"
    elif ("haachama" in name):
        return abspath + "haachama.jpg"
    elif ("matsuri" in name):
        return abspath + "matsuri.jpg"
    elif ("aqua" in name):
        return abspath + "aqua.jpg"
    elif ("shion" in name):
        return abspath + "shion.jpg"
    elif ("ayame" in name):
        return abspath + "ayame.jpg"
    elif ("choco" in name):
        return abspath + "choco.jpg"
    elif ("subaru" in name):
        return abspath + "subaru.jpg"
    elif ("mio" in name):
        return abspath + "mio.jpg"
    elif ("okayu" in name):
        return abspath + "okayu.jpg"
    elif ("korone" in name):
        return abspath + "korone.jpg"
    elif ("azki" in name):
        return abspath + "azki.jpg"
    elif ("suisei" in name):
        return abspath + "suisei.jpg"
    elif ("flare" in name):
        return abspath + "flare.jpg"
    elif ("marine" in name):
        return abspath + "marine.jpg"
    elif ("noel" in name):
        return abspath + "noel.jpg"
    elif ("watame" in name):
        return abspath + "watame.jpg"
    elif ("towa" in name):
        return abspath + "towa.jpg"
    elif ("luna" in name):
        return abspath + "luna.jpg"
    elif ("lamy" in name):
        return abspath + "lamy.jpg"
    elif ("nene" in name):
        return abspath + "nene.jpg"
    elif ("botan" in name):
        return abspath + "botan.jpg"

    # JP col cazzo
    elif ("shien" in name):
        return abspath + "shien.jpg"
    elif ("oga" in name):
        return abspath + "oga.jpg"
    elif ("holostars" in name):
        return abspath + "holostars.jpg"
    elif ("miyabi" in name):
        return abspath + "miyabi.jpg"
    elif ("izuru" in name):
        return abspath + "izuru.jpg"
    elif ("aruran" in name):
        return abspath + "aruran.jpg"
    elif ("rikka" in name):
        return abspath + "rikka.jpg"
    elif ("temma" in name):
        return abspath + "temma.jpg"
    elif ("astel" in name):
        return abspath + "astel.jpg"
    elif ("roberu" in name):
        return abspath + "roberu.jpg"

    # EN
    elif ("gura" in name):
        return abspath + "gura.jpg"
    elif ("kiara" in name):
        return abspath + "kiara.jpg"
    elif ("calliope" in name):
        return abspath + "calliope.jpg"
    elif ("ina'nis" in name):
        return abspath + "ina.jpg"
    elif ("amelia" in name):
        return abspath + "amelia.jpg"
    elif ("irys" in name):
        return abspath + "irys.jpg"
    elif ("tsukumoto" in name):
        return abspath + "sana.jpg"
    elif ("fauna" in name):
        return abspath + "fauna.jpg"
    elif ("baelz" in name):
        return abspath + "baelz.jpg"
    elif ("nanashi" in name):
        return abspath + "nanashi.jpg"
    elif ("kronii" in name):
        return abspath + "kronii.jpg"
    
    # ID
    elif ("ollie" in name):
        return abspath + "ollie.jpg"
    elif ("risu" in name):
        return abspath + "risu.jpg"
    elif ("moona" in name):
        return abspath + "moona.jpg"
    elif ("airani" in name):
        return abspath + "airani.jpg"
    elif ("hololive indonesia" in name):
        return abspath + "indonesia.jpg"
    elif ("pavolia" in name):
        return abspath + "pavolia.jpg"
    elif ("anya" in name):
        return abspath + "anya.jpg"
