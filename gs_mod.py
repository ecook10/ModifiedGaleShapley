''' gs_mod.py

Code by Evan Cook
August 29, 2016

Perform modified Gale-Shapley algorithm allowing for a "polygamous" situation
where a buyer can be matched to up to three sellers
'''

from __future__ import print_function

import sys
import random
import copy
import numpy as np



def get_preferences(buyer_count=5):
    """ Returns lists of random preference orders for a specified # of buyers.

    Arguments
    ---------
    buyer_count (int) : number of buyers to return preferences for.

    Returns
    -------
    buyer_prefs (list) : list containing lists representing the preference
        order of each buyer. Each preference list contains exactly one
        reference to each seller.
    seller_prefs (list) : lists containing lists representing prefence order of
        each seller. Each list contains exactly onne reference to each buyer.
    buyer_wants (list) : list containing an integer between 1 and 3 of the same
        size as `buyer_prefs` that specifies how many sellers are desired by that
        buyer.
    """


    buyer_wants = np.random.randint(1, 4, buyer_count)
    seller_count = sum(buyer_wants)

    buyer_start = range(seller_count)
    seller_start = range(buyer_count)

    buyer_prefs = list()
    seller_prefs = list()

    for i in range(buyer_count):
        random.shuffle(buyer_start)
        buyer_prefs.append(buyer_start[:])

    for i in range(seller_count):
        random.shuffle(seller_start)
        seller_prefs.append(seller_start[:])

    return buyer_prefs, seller_prefs, buyer_wants



def get_matches(buyer_prefs, seller_prefs, buyer_counts):
    """ Matches each seller to a buyer with no unstable matches.

    Arguments
    ---------
    buyer_prefs (list) : list of lists representing how each buyer's ranks the
        prospective sellers (highest first)
    seller_prefs (list) : list of lists representing how each seller ranks the
        prospective buyers (highest first)
    buyer_counts (list) : list of integers representing how many sellers each
        buyer is seeking

    Returns
    -------
    seller_matches (list) : list matching each seller (index) to a buyer (value)
    """

    buyer_prefs = copy.deepcopy(buyer_prefs)
    seller_prefs = copy.deepcopy(seller_prefs)

    buyer_matches = []
    for i in range(len(buyer_prefs)):
        buyer_matches.append([])

    seller_matches = [None] * len(seller_prefs)

    while None in seller_matches:

        for buyer, buyer_pref in enumerate(buyer_prefs):

            sellers_needed = buyer_counts[buyer] - len(buyer_matches[buyer])
            for i in range(sellers_needed):

                seller = buyer_pref.pop(0)
                prev_buyer = seller_matches[seller]

                if prev_buyer is None:
                    # If seller hasn't been matched yet, do it
                    seller_matches[seller] = buyer
                    buyer_matches[buyer].append(seller)

                else:
                    # Seller has been matched... replace if new buyer preferred
                    seller_pref = seller_prefs[seller]
                    if seller_pref.index(buyer) < seller_pref.index(prev_buyer):
                        seller_matches[seller] = buyer
                        buyer_matches[prev_buyer].remove(seller)
                        buyer_matches[buyer].append(seller)


    return seller_matches



def check_stability(buyer_prefs, seller_prefs, seller_matches):
    """ Check the stability of a list of matches.

    Stability is defined as a matching where no buyer prefers a seller they are
    not matched to who  also prefers said buyer.

    Arguments
    ---------
    buyer_prefs (list) : list of lists representing how each buyer's ranks the
        prospective sellers (highest first)
    seller_prefs (list) : list of lists representing how each seller ranks the
        prospective buyers (highest first)
    seller_matches (list) : list matching each seller (index) to a buyer (value)

    Returns
    -------
    is_stable (bool) : boolean value of whether the matches provided are stable
        given the two lists of preferences
    """

    for seller, buyer in enumerate(seller_matches):

        seller_pref = seller_prefs[seller]
        better_buyers = seller_pref[0:seller_pref.index(buyer)]

        for bb in better_buyers:
            matched_seller = seller_matches.index(bb)
            if buyer_prefs[bb].index(seller) < buyer_prefs[bb].index(matched_seller):
                # A buyer preferred by a seller over their match also prefers
                # the seller over their match
                return False

    return True



def run_tests(test_count=1000, buyer_count=10):
    """ Perform several matching operations from random sets of preference data
    and report if a matching error occurs

    Arguments
    ---------
    test_count (int) : number of tests to run
    buyer_count (int) : number of buyers to use on each test run
    """

    found_error = False

    for i in range(test_count):

        bp, sp, bw = get_preferences(buyer_count)
        matches = get_matches(bp, sp, bw)

        if not check_stability(bp, sp, matches):
            print('ERROR!!!')
            found_error = True

    if not found_error:
        print('Executed {} tests without errors'.format(test_count))



''' MAIN CODE '''
run_tests()
