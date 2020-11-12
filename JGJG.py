import itertools, re
import pandas as pd


class JGJG():
    col_lookup = {}
    alpha_memo = {}
    df = None
    def alpha(self, s): # Sort string alphabetically and remove duplicates
        if s in self.alpha_memo:
            return self.alpha_memo[s]
        result = re.sub(r"(.)\1", "", ''.join(sorted(s)))
        self.alpha_memo[s] = result
        return result
    
    def flatten(self, ar):
        result = []
        for x in ar:
            result += x
        return result
    
    def apply_rule(self, row, picks, result):
        picks_idxs = self.flatten([self.col_lookup[x] for x in picks])
        return self.alpha("".join([row[x] for x in picks_idxs])) == self.alpha(result)
    
    def check_answer(self, picks, target):
        return 0 == self.df[self.df.apply(lambda row:(not self.apply_rule(row, picks, target)), axis=1)].count()[0]

    def __init__(self, prizes, rules):
        self.col_lookup = dict(zip(prizes,[(i*2,i*2+1) for i in range(len(prizes))]))

        # All possible worlds
        self.df = pd.DataFrame(list(itertools.permutations(prizes + prizes)))
        
        # Eliminate worlds where prizes give themselvs
        for i, prize in enumerate(prizes):
            self.df = self.df[(self.df[i]!=prize)]

        # Eliminate worlds where a prize gives two of the same prize
        for i in range(0, len(prizes)*2, 2):
            self.df = self.df[(self.df[i]!=self.df[i+1])]

        for rule in rules:
            self.df["rule_result"] = self.df.apply(lambda row:self.apply_rule(row, rule[0], rule[1]), axis=1)
            self.df = self.df[self.df["rule_result"]]

        # Try prize combinations where result is CD
        for i in range(len(prizes)):
            options = [x for x in itertools.combinations(prizes, i+1)]
            for option in options:
                if self.check_answer(option, "CD"):
                    print("".join(option))
        print("Done.")

if __name__ == "__main__":
    prizes="BCDGP"
    examples = [("CG","BP"), ("CBP","CBPD")]
    JGJG(prizes, examples)
