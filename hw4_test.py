
#########################################
##### Name: Victoria Cope           #####
##### Uniqname: copev               #####
#########################################

import unittest
import hw4_cards as cards

# SI 507 Winter 2020
# Homework 4 - Code

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

class TestCard(unittest.TestCase):
    # this is a "test"
    def test_0_create(self):
        card = cards.Card()
        self.assertEqual(card.suit_name, "Diamonds")
        self.assertEqual(card.rank, 2)

    # Add methods below to test main assignments.
    def test_1_queen(self):
        card = cards.Card(rank=12)
        self.assertEqual(card.rank_name, "Queen")

    def test_2_clubs(self):
        card = cards.Card(suit=1)
        self.assertEqual(card.suit_name, "Clubs")

    def test_3_king_of_spades(self):
        card = cards.Card(suit=3, rank=13)
        self.assertEqual(card.__str__(), "King of Spades")

    def test_4_52_pickup(self):
        card = cards.Deck()
        self.assertEqual(len(card.cards), 52)

    def test_5_deal_card(self):
        deck = cards.Deck()
        card = cards.Card()
        self.assertIsInstance(deck.deal_card(), type(card))

    def test_6_deal_cards_left(self):
        deck = cards.Deck()
        deck.deal_card()
        self.assertEqual(len(deck.cards), 51)

    def test_7_replace_card(self):
        deck = cards.Deck()
        card_dealt = deck.deal_card()
        deck.replace_card(card_dealt)
        self.assertEqual(len(deck.cards), 52)

    def test_8(self):
        deck = cards.Deck()
        card_dealt = deck.deal_card() # deck = 51
        deck.replace_card(card_dealt) # deck = 52
        deck.replace_card(card_dealt) # attempt at adding the same card again
        self.assertEqual(len(deck.cards), 52) # deck = 52


############
### The following is a line to run all of the tests you include:
if __name__ == "__main__":
    unittest.main()
