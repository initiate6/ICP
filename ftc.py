import requests
from random import choice, randint

#pip install fake-factory
from faker import Faker


#all his domains are here: http://pastie.org/private/7vibznjr5e75j1wxddyglq

#FuckTheChinese
def ftc(username, password):
	try:
		
		#url = 'http://apple-ios-icloud-verify.com/Home/Save'
		url = 'http://02246.poruzstw.cn/Home/Save'
		data = { 'u' : username, 'p' : password }

		s = requests.session()
		r = s.post(url, data, verify=False)

		print r.status_code
		
	except Exception as e:
		print e.read()
		pass

# top-level domains
TLDS = ('com com com com com com net org mil edu com').split()

domain = ('apple gmail hotmail me iCloud').split()

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

	#Run forever
	while True:
		
		ftc(fake_address(), choice(f).strip('\n'))
