def luhn(n):
  r = [int(ch) for ch in str(n)][::-1]
  return (sum(r[0::2]) + sum(sum(divmod(d*2,10)) for d in r[1::2])) % 10 == 0

#build the card lookup table: V,MC,AMEX,DISC,OTHER
visa = {'brand':'VISA', 'length':16, 'start':[4]}
amex = {'brand':'AMEX', 'length':15, 'start':[34,37]}
mc = {'brand':'MASTERCARD', 'length':16, 'start':[ i for i in range(51,56) ]}
disc = {'brand':'DISCOVER', 'length':16, 'start':[6011,64] + range(622126,622926) + range(644,650) }
jcb = {'brand':'JCB', 'length':16, 'start':range(3528,3590)}

CC_Lookup = [visa, amex, mc, disc, jcb]


card_number = raw_input("Enter a card number: ")

for card in CC_Lookup:
  length = card['length']

  for prefix in card['start']:
    if card_number.startswith(str(prefix)) and card_number.isdigit(): 

      brand = card['brand']
      luhn = bool(luhn(card_number))
      record = {'pan':card_number, 'brand':brand, 'luhn':luhn}

      print record
              
