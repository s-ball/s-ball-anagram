import sys
from dataclasses import dataclass
from itertools import permutations as pr
from pathlib import Path
from typing import Generator

import unicodedata

ref = None


def clean(s: str) -> str:
    """Filter out any diacritics from a string.

    It uses the Unicode normal form KD to decompose each character to its
    compatibility version, and then filter out non alpha characters.
    """
    k = unicodedata.normalize('NFKD', s)
    return ''.join(i for i in k if (i == '_' or i.isalpha()))


@dataclass
class Jardin:
    mot: str

    def search(self, mask: str, refs) -> Generator[str]:
        """Build a generator of strings matching a mask.

        "_" character is used as a one character wild char.
        """
        ln = len(mask)
        for t in sorted(set(pr(self.mot, ln))):
            if refs and (t not in refs):
                continue
            for i, c in enumerate(mask):
                if c != '_' and c != t[i]:
                    break
            else:
                yield t

    def process(self):
        while True:
            hint = input('A rechercher (_ pour une position vide. Exemple _A_) : ')
            hint = clean(hint).upper()
            x = hint.split()
            if len(x) == 0:
                break
            if len(x) == 2 and x[1].upper() == 'X':
                r = None
            else:
                r = ref
            hint = x[0]
            if len(hint) == 0:
                break
            for i in self.search(hint, r):
                print(''.join(i))


def main():
    global ref
    d = Path(sys.prefix)/'share'/'dict'
    try:
        ref = set(tuple(w.strip().upper()) for w in
                  open(d/'dict-fr-AU-DELA-common-words.ascii'))
    except OSError:
        print(f'Dossier dictionnaire vide : {d}')
        ref = None
    while True:
        mot = input('Lettres : ')
        mot = clean(mot).upper()
        if len(mot) == 0:
            break
        j = Jardin(mot)
        j.process()
