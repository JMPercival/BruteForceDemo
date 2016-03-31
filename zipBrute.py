import zipfile
import sys
from time import sleep

wordlist = open('wordlist.txt').read().split('\n')
z = zipfile.ZipFile('SSN.zip')

for password in wordlist:
	try:
		print '( + ) Trying '+ password
		z.extract(z.namelist()[0],pwd=password)
		print '( + ) ' + password + ' actually worked! Copying the files out!'
		sys.exit()
	except Exception:
		pass