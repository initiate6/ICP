import requests
from random import choice, randint
import time
#pip install fake-factory
from faker import Faker
import threading

COUNT = 20

#all his domains are here: http://pastie.org/private/7vibznjr5e75j1wxddyglq

#urls = ('02246.poruzstw.cn 22i28.poruzstw.cn 40624.rjmolgbl.cn 02460.khfnwbzb.cn 202i2s.mupijeri.cn 46266.mupijeri.cn 4ukqy.ldxqlwyu.cn 600844.icfzjyyk.cn 64468.mupijeri.cn 662268.ckspbfms.cn 68066.poruzstw.cn 6a400.icfzjyyk.cn 6iqg8.rjmolgbl.cn 800420.mupijeri.cn 82480.icfzjyyk.cn 8288u.brhlbskz.cn 84868.rjmolgbl.cn 8gko88.rjmolgbl.cn 8ikig.ajegujwg.cn a64g0.ldxqlwyu.cn e8mk8y.mrpiwewm.cn ekqc48.poruzstw.cn emkuq.khfnwbzb.cn g22qmi.ckspbfms.cn gwogy4.mrpiwewm.cn wyei8e.ajegujwg.cn y46i8g.icfzjyyk.cn q68ium.baike.icfzjyyk.cn us6yo.brhlbskz.cn yy6ig.poruzstw.cn').split()
urls = ('ckspbfms.cn brhlbskz.cn ajegujwg.cn rjmolgbl.cn poruzstw.cn khfnwbzb.cn mupijeri.cn icfzjyyk.cn mrpiwewm.cn ldxqlwyu.cn').split()
#Lets turn up the heat and thread this bitch. :D
class ftc_manager(object):
	def new_thread(self, url, username, password):
		return ftc(url, username, password, parent=self)
			
	def on_thread_finished(self, thread, data):
		print thread, data
		
class ftc(threading.Thread):
	def __init__(self, url, username, password, parent=None):
		super(ftc, self).__init__()
		self.url = url
		self.username = username
		self.password = password
		
	def run(self):
        	try:
                	url = 'http://%s/Home/Save' % (self.url)
                	data = { 'u' : self.username, 'p' : self.password }
                	print(url)
                	print(data)
                	s = requests.session()
                	r = s.post(url, data, verify=False)

                	print(r.status_code, r.content )
                	print('-----------------------------------------------------')

        	except Exception as e:
                	print(e)
                	pass
                
                #self.parent and self.parent.on_thread_finished(self, 'done')

# top-level domains
TLDS = ('com edu com net com org mil com com com com').split()

domain = ('apple me gmail hotmail iCloud').split()

def gen_name(length):
        return '.'.join(fake.name().split())

def gen_domain():
        return choice(domain)

def fake_address():
        user = gen_name(randint(3, 15))
        host = gen_domain()
        return '%s@%s.%s' % (user, host, choice(TLDS))

if __name__ == "__main__":
	
        #Create Faker object
        fake = Faker()

        #Read file once and hold in memory
        fp = open('passwords.txt', 'r')
        f = fp.readlines()

	threads = len(urls)
	fm = ftc_manager()
	
        while True:
		count = COUNT
        	for url in urls:
        		thread = fm.new_thread(url, fake_address(), choice(f).strip('\n'))
        		
        		print('Start threading for url: %s') % (url)
        		thread.start()
			count -= 1
			if count <= 0:
				count = COUNT
				time.sleep(5)
