import os
import datetime
#input-------------------------------------
direction = input('Your direction: ')
# direction = 'd:\\lovemachine'

#defs----------------------------------------------------
def authnew():
            name = input('Name: ')
            version = input('Version: ')
            author = input('Author: ')
            datecreated = input('Date created: ')
            datefixed = input('Date fixed: ')
            
            file = open(authdir+'\\auth.txt','w')
            
            if name == '':
                names = authdir.split('\\')
                name = names[len(names)-2]
            file.write('Name: '+name)
            
            if version == '':
                version = '0.0.0'
            file.write('\nVersion: '+version)
            
            if author == '':
                author = 'NULL'
            file.write('\nAuthor: '+author)
            
            if datecreated == '':
                datecreated = datetime.date.today().strftime('%d/%m/%Y')+'-'+datetime.datetime.now().strftime('%H.%M.%S')
            file.write('\nDate created: '+datecreated)
            
            if datefixed == '':
                datefixed = datetime.date.today().strftime('%d/%m/%Y')+'-'+datetime.datetime.now().strftime('%H.%M.%S')
            file.write('\nDate fixed: '+datefixed)
            
            file.close()
            
            file = open(authdir+'\\log.txt','w')
            file.close()


def authold():
    file = open(authdir+'\\auth.txt','w')
    name = input('Name: ')
    version = input('Version: ')
    author = input('Author: ')
    datecreated = input('Date created: ')
    datefixed = input('Date fixed: ')
    
    if name == '':
        name = stuff[0]
    file.write('Name: '+name)
    
    if version == '':
        version = stuff[1]
    file.write('\nVersion: '+version)
    
    if author == '':
        author = stuff[2]
    file.write('\nAuthor: '+author)
    
    if datecreated == '':
        datecreated = stuff[3]
    file.write('\nDate created: '+datecreated)
    
    if datefixed == '':
        datefixed = datetime.date.today().strftime('%d/%m/%Y')+'-'+datetime.datetime.now().strftime('%H.%M.%S')
    file.write('\nDate fixed: '+datefixed)
    
    file.close()
    
    log = input('Write your log: ')
    file = open(authdir+'\\log.txt','a')
    file.write(f'\nVersion {version}: \n{log}')
    file.close()


#main-----------------------------------------------
if os.path.exists(direction):
    authdir = os.path.join(direction,'auth')
    print(authdir)
    
    #write data---------------------------------------
    try:
        os.mkdir(authdir)
        authnew()
    except:
        print('Already auth.\nYour last data:')
        
        file = open(authdir+'\\auth.txt','r')
        stuff = [line.split(':')[1].split('\n')[0].split(' ')[1] for line in file]
        print(stuff)
        file.close()
        
        #quest---------------------------------------------
        quest = ''
        while quest != 'y' and quest != 'n':
            quest = input('Do you want to auth new? (y/n): ')
        if quest == 'y':
            authnew()
        else:
            authold()
        
        file = open(authdir+'\\auth.txt','r')
        os.system('cls')
        print('Your data: \n')
        for line in file:
            print(line)
else:
    print('No such file or directory')
    
#end--------------------------------------------------