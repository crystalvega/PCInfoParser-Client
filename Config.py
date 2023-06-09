from pathlib import Path
check_lines = ['ip','port','key','iv']
name = "C:\\Program Files\\ConfigNKU\\Main\\client.cfg"

def Parse():
    config = [None]*len(check_lines)
    if Path(name).is_file() == False:
        default_lines = ['ip = Не задан','port = Не задан','key = Не задан','iv = Не задан']
        with open(name, "w") as file:
            for line in default_lines:
                file.write(line+'\n')
    with open(name, "r") as file:
        for line in file:
            for index, check  in enumerate(check_lines):
                if check+' = ' in line:
                    if line != check +' = Не задан\n':
                        config[index] = line.replace(check+' = ','').replace('\n','')

    return config

def Check():
    config = Parse()
    check = True
    Return = 'Укажите в '+ name +': '
    for index in range(0,len(config)-1):
        if config[index] == None and Return.endswith(': '):
            Return = Return + check_lines[index]
            check = False
        elif config[index] == None:
            Return = Return + ', ' + check_lines[index]
    return check, Return, config