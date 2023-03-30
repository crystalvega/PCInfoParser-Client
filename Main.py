import asyncio
import os
from pathlib import Path

from command_runner.elevate import elevate

import CheckDate
import Config
import GUI
import ZIP
from GetConfiguration import GetConfiguration as gc
from OutputConfiguration import Client

def save_project_root() -> Path:
    return Path(__file__).parent

abs_path = str(save_project_root())
Config.name = abs_path+'\\client.cfg'

class clientconnect:
    async def start(ip, port):
        global task1
        task1 = asyncio.create_task(Client.connect(ip, port))
        
    async def get():
        returnvalue = await task1
        return returnvalue

def main():
    try:
        config = GUI.start("C:\\Program Files\\ConfigNKU\\confignku.txt")
        check, error, configparse = Config.Check()
        datefile = abs_path+'\\lastsend.txt'
        if check:
            if CheckDate.CheckDate(datefile, 7):
                Client.key = configparse[2]
                Client.iv = configparse[3]
                ZIP.unpack("data.pkg","C:\Windows\Temp\dataofpack1")
                asyncio.run(clientconnect.start(configparse[0], int(configparse[1])))
                print('Происходит сбор данных')
                charters,disk = gc.get_char(config)
                print('Сбор данных произошёл успешно!')
                filename = ['FILENAME',config[4]]
                returnvalue = asyncio.run(clientconnect.get())
                if returnvalue == "0":
                    if Client.Send(charters, disk, filename):
                        CheckDate.CreateDate(datefile)
                else:
                    print(returnvalue)
                
        else:
            print(error)
            os.system("pause")
    except Exception as e:
        print(e)
        os.system("pause")
    
if __name__ == "__main__":
    elevate(main)