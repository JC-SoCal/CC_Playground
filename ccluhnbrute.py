#luhn function from http://rosettacode.org/wiki/Luhn_test_of_credit_card_numbers#Python
def luhn(n):
  r = [int(ch) for ch in str(n)][::-1]
  return (sum(r[0::2]) + sum(sum(divmod(d*2,10)) for d in r[1::2])) % 10 == 0

start = input("Enter first portion of card: ")
end = input("Enter last portion of card: ")
totalLen = input("Enter card length: ")

reqLen = totalLen - (len(str(start))+len(str(end)))

seek = int("9" * reqLen)
for x in range(seek):
  missing = str(x).zfill(reqLen)
  full_card = int(str(start) + missing + str(end))
  if luhn(full_card):
    #print valid cards
    print str(full_card)