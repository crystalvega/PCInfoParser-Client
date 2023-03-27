import os, asyncio

from command_runner.elevate import elevate

import Config
import GUI
import ZIP
import CheckDate
from GetConfiguration import GetConfiguration as gc
from OutputConfiguration import Client

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
        datefile = 'C:\\Program Files\\ConfigNKU\\Main\\lastsend.txt'
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