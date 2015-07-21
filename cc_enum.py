import json, urllib2, argparse

def luhn(n):
	r = [int(ch) for ch in str(n)][::-1]
	return (sum(r[0::2]) + sum(sum(divmod(d*2,10)) for d in r[1::2])) % 10 == 0

def binlistQuery(iin):
	website = "http://www.binlist.net/json/%s" % (str(iin))
	headers = { 'User-Agent' : 'Mozilla/5.0' }
	req = urllib2.Request(website, None, headers)
	data = json.load(urllib2.urlopen(req))
	return data

def main(cardnumber):
	unks = cardnumber.count('?')
	seek = int("9" * unks)

	print "PAN, Brand, Sub-brand, Country Code, Country Name, Bank, Card Type, Card Category"

	for i in range(seek + 1):
		testcard = cardnumber
		
		for x in str(i).zfill(unks):
			testcard = testcard.replace("?",x,1)
		
		if luhn(testcard):
			try:
				data = binlistQuery(testcard[0:6])
				print "%s, %s, %s, %s, %s, %s, %s, %s" % (testcard, data['brand'], data['sub_brand'], data['country_code'], data['country_name'], data['bank'], data['card_type'], data['card_category'])				
			
			except:
				pass

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Brute Force an incomplete card number and validate by luhn and IIN')
	parser.add_argument('-c', '--cardnumber',
						dest='cardnumber',  
						help='Credit Card number. Use ? in place of unknown numbers\nExample: 41012321??31??',
						required=True)
	args = parser.parse_args()
	main(args.cardnumber)