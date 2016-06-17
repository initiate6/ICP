import requests
from random import choice, randint

#pip install fake-factory
from faker import Faker


#all his domains are here: http://pastie.org/private/7vibznjr5e75j1wxddyglq

#FuckTheChinese
def ftc(username, password):
	#url = 'http://apple-ios-icloud-verify.com/Home/Save'
	url = 'http://02246.poruzstw.cn/Home/Save'
	data = { 'u' : username, 'p' : password }

	s = requests.session()
	r = s.post(url, data, verify=False)

	print r.status_code

# top-level domains
TLDS = ('com net org mil edu de biz de ch at ru de tv com').split()

domain = ('apple gmail hotmail').split()

def gen_name(length):
	return '.'.join(fake.name().split())

def gen_domain():
	return choice(domain)

def fake_address():
        user = gen_name(randint(3, 15))
        host = gen_domain()
        return '%s@%s.%s' % (user, host, choice(TLDS))



if __name__ == "__main__":

	fake = Faker()
	
	fp = open('passwords.txt', 'r')
	f = fp.readlines()

	while True:

		password = choice(f)
		ftc(fake_address(), password)
