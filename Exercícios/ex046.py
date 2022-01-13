# contagem regressiva
from time import sleep
import emoji
for c in range(5, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize(':party_popper:'*10, variant='emoji_type'))
