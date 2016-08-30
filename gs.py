''' gs.py

Code by Evan Cook
August 29, 2016

Module for perfoming regular Gale-Shapley algorithm based on randomly generated
preferences
'''

from __future__ import print_function

import random
import copy
import numpy as np



def get_preferences(count=5):

    start = range(count)
    buyer_prefs = list()
    seller_prefs = list()

    for i in range(count):
        random.shuffle(start)
        buyer_prefs.append(start[:])
        random.shuffle(start)
        seller_prefs.append(start[:])

    return buyer_prefs, seller_prefs



def get_matches(buyer_prefs, seller_prefs):

    buyer_prefs = copy.deepcopy(buyer_prefs)
    seller_prefs = copy.deepcopy(seller_prefs)
    seller_matches = [None] * len(buyer_prefs)

    while None in seller_matches:

        for buyer, buyer_pref in enumerate(buyer_prefs):

            if buyer not in seller_matches:

                seller = buyer_pref.pop(0)
                prev_buyer = seller_matches[seller]

                if prev_buyer is None:
                    # If seller hasn't been matched yet, do it
                    seller_matches[seller] = buyer

                else:
                    # Seller has been matched... replace if new buyer preferred
                    seller_pref = seller_prefs[seller]
                    if seller_pref.index(buyer) < seller_pref.index(prev_buyer):
                        seller_matches[seller] = buyer

    return seller_matches



def check_stability(buyer_prefs, seller_prefs, seller_matches):

    for seller, buyer in enumerate(seller_matches):

        seller_pref = seller_prefs[seller]
        better_buyers = seller_pref[0:seller_pref.index(buyer)]

        for bb in better_buyers:
            matched_seller = seller_matches.index(bb)
            print(bb)
            print(buyer_prefs[bb])
            if buyer_prefs[bb].index(seller) < buyer_prefs[bb].index(matched_seller):
                # A buyer preferred by a seller over their match also prefers
                # the seller over their match
                return False

    return True





buyer_prefs, seller_prefs = get_preferences(5)
seller_matches = get_matches(buyer_prefs, seller_prefs)

'''
print(buyer_prefs)
print(seller_prefs)
print(seller_matches)
print(check_stability(buyer_prefs, seller_prefs, seller_matches))
'''
