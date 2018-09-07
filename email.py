import json

emails = json.loads(open('emails.json').read())

def start():
    print ("Starting this...")
    fletter = input('Type in the first letter of the email:')
    fletter = fletter.lower()

    if fletter == '1':
    	print (emails['1'])
    elif fletter == '2':
    	print (emails['2'])
    elif fletter == '3':
    	print (emails['3'])
    elif fletter == '4':
    	print (emails['4'])
    elif fletter == '5':
    	print (emails['5'])
    elif fletter == '6':
    	print (emails['6'])
    elif fletter == '7':
    	print (emails['7'])
    elif fletter == '8':
    	print (emails['8'])
    elif fletter == '9':
    	print (emails['9'])
    elif fletter == 'a':
    	print (emails['a'])
    elif fletter == 'b':
    	print (emails['b'])
    elif fletter == 'c':
    	print (emails['c'])
    elif fletter == 'd':
    	print (emails['d'])
    elif fletter == 'e':
    	print (emails['e'])
    elif fletter == 'f':
    	print (emails['f'])
    elif fletter == 'g':
    	print (emails['g'])
    elif fletter == 'h':
    	print (emails['h'])
    elif fletter == 'i':
    	print (emails['i'])
    elif fletter == 'j':
    	print (emails['j'])
    elif fletter == 'k':
    	print (emails['k'])
    elif fletter == 'l':
    	print (emails['l'])
    elif fletter == 'm':
    	print (emails['m'])
    elif fletter == 'n':
    	print (emails['n'])
    elif fletter == 'o':
    	print (emails['o'])
    elif fletter == 'p':
    	print (emails['p'])
    elif fletter == 'q':
    	print (emails['q'])
    elif fletter == 'r':
    	print (emails['r'])
    elif fletter == 's':
    	print (emails['s'])
    elif fletter == 't':
    	print (emails['t'])
    elif fletter == 'u':
    	print (emails['u'])
    elif fletter == 'v':
    	print (emails['v'])
    elif fletter == 'w':
    	print (emails['w'])
    elif fletter == 'x':
    	print (emails['x'])
    elif fletter == 'y':
    	print (emails['y'])
    elif fletter == 'z':
    	print (emails['z'])
    else:
    	print('wot')

start()