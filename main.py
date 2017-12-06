from bitcoin import *
from hashlib import sha256

def try_word(word):
  print('Palabra ' + word)
  priv = sha256(word).hexdigest()
  print('Private Key:' + priv)
  pub = privtopub(priv)
  print('Public Key:' + pub)
  addr = pubtoaddr(pub)
  print('Address:' + addr)
  # h = history(addr)
  # print(h)
  h = unspent(addr)
  print('Cantidad ' + str(len(h)))
  if(len(h) > 0):
    return True
  return False

with open('encontrados.txt', 'w') as output_file:
  with open('smalldict.txt') as f:
    content = f.readlines()
    words = [x.strip() for x in content]
    for word in words:
      output_file.write(word + '\n')
      if try_word(word):
        raise ValueError('Holy shit')
        