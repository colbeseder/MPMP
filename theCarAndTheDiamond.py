'''
Solution to the MPMP18: JGJG: the car and the diamond
https://youtu.be/hPOi6dKBnh4

Output:
    When the prizes are BCDGP, and you want CD, whilst matching the examples: CG=>BP and CBP=>CBPD, You should ask for:
    >>> CD or BGP

Note: I orginally did this puzzle by hand. And I first found (and submitted) the longer answer :-(

'''

import itertools, re
import pandas as pd


class theCarAndTheDiamond():
    def alpha(self, s): # Sort string alphabetically and remove doubles
        result = re.sub(r"(.)\1", "", ''.join(sorted(s)))
        return result

    def flatten(self, ar):
        result = []
        for x in ar:
            result += [x[0], x[1]]
        return result

    def no_triples(self, row):
        return re.search(r"(.)\1\1", ''.join(sorted(self.flatten(row)))) == None

    def apply_rule(self, row, picks, result):
        given = [row[self.prizes.index(pick)] for pick in picks]
        return self.alpha(self.flatten(given)) == self.alpha(result)

    def check_answer(self, picks, prizes, target):
        # If all rows match, then answer is good (ie. not rows don't match)
        return 0 == self.df[self.df.apply(lambda row:(not self.apply_rule(row[0:len(prizes)], picks, target)), axis=1)].count()[0]

    def __init__(self, prizes, target, rules):
        self.prizes = prizes

        # Create all worlds
        all_givens = list(itertools.combinations(prizes, 2)) #does not contain like-pairs
        self.df = pd.DataFrame(list(itertools.product(all_givens, repeat=5)))

        for i, prize in enumerate(prizes): # Eliminate worlds where prizes give themselvs
            self.df = self.df[self.df.apply(lambda row:(prize not in row[i]) , axis=1 )]

        # Eliminate worlds where same prize is given by more than 2 others
        # (and implicitly, where a prize is given less than twice)
        self.df = self.df[self.df.apply(lambda row:self.no_triples(row[0:len(prizes)]), axis=1 )]

        for rule in rules: # Eliminate worlds that don't match the examples
            self.df = self.df[self.df.apply(lambda row:self.apply_rule(row, rule[0], rule[1]), axis=1)]

        right_answers = [] # Shorted first
        # Try prize combinations where result is target
        for i in range(len(prizes)):
            options = [x for x in itertools.combinations(prizes, i+1)]
            for option in options:
                if self.check_answer(option, prizes, target):
                    right_answers.append("".join(option))
        print("When the prizes are %s, and you want %s, whilst matching the examples: %s, You should ask for:"%(prizes, target, " and ".join(["=>".join(ex) for ex in examples])))
        print(" >>> " + " or ".join(right_answers))


if __name__ == "__main__":
    prizes   = "BCDGP"
    examples = [("CG","BP"), ("CBP","CBPD")]
    theCarAndTheDiamond(prizes, "CD", examples)
