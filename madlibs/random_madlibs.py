from sample_madlibs import arcade, coder, zombie, homealone
import random

if __name__ == "__main__":
    m = random.choice([arcade, coder, zombie, homealone])
    m.madlib()