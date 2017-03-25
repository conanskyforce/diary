import hashlib
import os

os.chdir('T2F')
files = os.listdir()
for file in files:
	with open(file,'rb') as f:
		md5obj = hashlib.md5()
		md5obj.update(f.read())
		md5_hash = md5obj.hexdigest()
		print('md5_hash: '+md5_hash)
	with open(file,'a+') as f:
		f.write('#f#u#c&k&y&o%u%')
		f.close()
		with open(file,'rb') as f:
			after_md5obj = hashlib.md5()
			after_md5obj.update(f.read())
			after_md5_hash = after_md5obj.hexdigest()
			print('after_md5_hash: '+after_md5_hash)
print('finished!')