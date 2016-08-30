# Gale-Shapley Algorithm Variation

Code by Evan Cook

---------------------------------------

## Running instructions

To run simply cd into the repo and run the `gs_mod.py` script


## Prompt

Your task is to implement a variation of the Gale-Shapley algorithm, which is a solution to the Stable Marriage Problem[https://en.wikipedia.org/wiki/Stable_marriage_problem]. Use whatever language is best suited to the problem given your comfort in that language. If you pick something weird (Outside top 10 on Github) then be prepared to justify it. Your solution must fit the following criteria:


1. It has to run. A reasonably competent developer should be able to get it running without too much trouble. If there are any dependencies then some sort of requirements file or instructions should be provided.

2. It should demonstrate your solution using non-trivial inputs of your creation. 

3. It should be at a quality level style-wise that you would expect in a team project.


The variation on Gale-Shapley is I want a solution that works in a "polygamous" situation. (Let's swap husband/wife language for buyer/seller for the rest of the description).  Buyers want up to be matched with up to three sellers. Some want one, some two, some three. There are enough sellers to satisfy all the buyer's desired sellers but no more.


Like vanilla Gale-Shapley each buyer has a ranked list of preferred sellers and each seller has a ranked list preferred buyers. Your goal is to create stable matchings where every buyer has been matched with their desired number of sellers and every seller is match with at exactly one buyer.
