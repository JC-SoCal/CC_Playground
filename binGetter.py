import json
import urllib2
import time
import argparse

def luhn(n):
  r = [int(ch) for ch in str(n)][::-1]
  return (sum(r[0::2]) + sum(sum(divmod(d*2,10)) for d in r[1::2])) % 10 == 0

def binlistQuery(iin):
	website = "http://www.binlist.net/json/%s" % (str(iin))
	headers = { 'User-Agent' : 'Mozilla/5.0' }

	req = urllib2.Request(website, None, headers)
	data = json.load(urllib2.urlopen(req))
	return data

def main(filename,delay):
	with open(filename) as cardfile:
		print "PAN, Luhn Pass, Brand, Sub-brand, Country Code, Country Name, Bank, Card Type, Card Category"# Header
		
		for card in cardfile:
			time.sleep(delay)
			# i should add a check to make sure the card is valid: over x digits, only digits, etc
			
			pan = card.strip()
			iin = pan[0:6] 
			
			luhnresult = luhn(pan)
			if luhnresult:
				data = binlistQuery(iin)
				print "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (pan, luhnresult, data['brand'], data['sub_brand'], data['country_code'], data['country_name'], data['bank'], data['card_type'], data['card_category'])				
			else:
				print "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (pan, luhnresult, None, None, None, None, None, None, None)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Get BIN specific information about credit cards.')

	parser.add_argument('-f', '--filename',
						dest='filename',  
						help='Filename which contains the credit cards',
						required=True)
	
	parser.add_argument('-d', '--delay',
						dest='delay',  
						help='How long to sleep between lookups (seconds). Can take decimal i.e .5 seconds',
						default=0,
						required=False)	
	args = parser.parse_args()

	main(args.filename, args.delay)
