import requests
import json
import os
import multiprocessing
from colorama import Fore, Style, init

r = Fore.RED + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
y = Fore.YELLOW + Style.BRIGHT
o = Fore.RESET + Style.RESET_ALL
#API : https://rostovabrothers.com/documentation/
def revR(ip):
	try:
		rev = requests.get('https://api.rostovabrothers.com/api?ip='+ip)
		data = rev.json()
		if data.get('status', 0) == 200 and not data.get('message', True):
			res = data.get('result', [])
			count = len(res)
			print('{} IP {} {} {}Total Domain {}{}'.format(y, ip, o, g, count, o))
			with open('Res_rev.txt', 'a') as file:
				for dom in res:
					file.write(dom + '\n')
		else:
			print('{}IP address not found or invalid {} {}'.format(r, o, ip))
			
	except Exception as e:
		print('{}Unable to establish a connection to the API. The API Host is currently offline.'.format(r))
		pass

if __name__ == '__main__':
	os.system('cls' if os.name == 'nt' else 'clear')
	print("%s RevR  | %sShin Code\n" % (y, c))
	ip_list = open(raw_input(o+'List:~# '),'r').read().splitlines()
	print('{}Total IP List : {}{}'.format(c, o, len(ip_list)))
	num_processes = min(multiprocessing.cpu_count(), len(ip_list))
	pool = multiprocessing.Pool(processes=num_processes)
	pool.map(revR, ip_list)
	pool.close()
	pool.join()
    