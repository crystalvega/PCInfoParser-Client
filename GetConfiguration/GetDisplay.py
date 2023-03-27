from winreg import *
import pyedid
from math import hypot

registry = ConnectRegistry(None, HKEY_LOCAL_MACHINE)

def openRegistryA(dir):
    key = None
    try:
        rawKeyA = OpenKey(registry, "SYSTEM\\CurrentControlSet\\Enum\\" + dir + "\\Device Parameters")
        i = 0
        while 1:
            name, value, type = EnumValue(rawKeyA, i)
            key = value
            i += 1

    except:
            Exception
    return key

def get(dir):
    edid_hex = openRegistryA(dir)
    edid_result = ["Не найдено", "Не найдено"]
    if edid_hex != None:
        edid_hex = edid_hex.hex()
        edid = pyedid.parse_edid(edid_hex)
        edid_result[0] = edid.manufacturer + " " + edid.name
        edid_result[1] = round(round(hypot(edid.width, edid.height), 1)*0.393701, 1)
        json_str = str(edid)
    return edid_result