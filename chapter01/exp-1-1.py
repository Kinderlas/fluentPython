# -*- coding: utf-8 -*-
# @author: Kinderlas (Kinderlas@gmail.com)
# @date: 2017/9/28 16:51
import collections
from random import choice

Card = collections.namedtuple("Card", ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                        for rank in self.ranks]

    # len(deck)
    def __len__(self):
        return len(self._cards)

    def show(self):
        for card in self._cards:
            print(card, end=', ')

    # deck[i]
    # card in deck
    # for i in deck
    def __getitem__(self, item):
        return self._cards[item]


def main():
    deck = FrenchDeck()
    print(len(deck))

    print(deck[0])
    print(deck[-1])
    print(deck[:3])

    for card in deck:
        print(card, end=', ')
    print('')

    for card in reversed(deck):
        print(card, end=', ')
    print('')

    print(Card('Q', 'hearts') in deck)
    print(Card('W', 'hearts') in deck)

    print(choice(deck))

    def spades_high(card):
        suits_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
        rank_value = FrenchDeck.ranks.index(card.rank)
        return suits_values[card.suit] + rank_value * len(suits_values)
        #return suits_values[card.suit] * len(FrenchDeck.ranks) + rank_value

    for card in sorted(deck, key=spades_high):
        print(card, end=',')


if __name__ == '__main__':
    main()
