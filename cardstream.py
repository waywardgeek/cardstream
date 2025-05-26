# This is a Python3 version.
from random import randrange

class Deck:
  def __init__(self, length):
    self.length = length
    self.cards = [i for i in range(length)]
    self.pos = 0

  def shuffle(self):
    for i in range(self.length):
      index = i + randrange(self.length - i)
      prevCard = self.cards[i]
      self.cards[i] = self.cards[index]
      self.cards[index] = prevCard

  def incPos(self):
    self.pos += 1
    if self.pos >= self.length:
      self.pos -= self.length

  def addPos(self, card):
    pos = self.pos + card
    if pos >= self.length:
      pos -= self.length
    return pos

  # Generate a random card from the deck.  This is meant to be computationally
  # indistiguishable from random, making this a CPRNG.
  def randCard(self):
    while True:
      card1 = self.cards[self.pos]
      pos1 = self.addPos(card1)
      card2 = self.cards[pos1]
      pos2 = self.addPos(card2)
      card3 = self.cards[pos2]
      if self.pos != pos1:
        break
      self.incPos()
    if self.pos != pos2:
      self.cards[self.pos] = card2
      self.cards[pos1] = card3
      self.cards[pos2] = card1
    self.incPos()
    return card3

def cardName(card):
  if card // 13 == 1:
    color = "R"
  else:
    color = "B"
  cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  return color + cards[card % 13]

numCards = 26
deck = Deck(numCards)
deck.shuffle()
print("Cards =", deck.cards)
while True:
  print(cardName(deck.randCard()))
