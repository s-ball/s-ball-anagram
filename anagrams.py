""" This is intended to be a starting point for nuitka compilation.

As such it includes nuitka configuration comments and simply
launches the anagram package.
"""

from s_ball_anagram.anagram import main
from s_ball_anagram.__about__ import __version__


# nuitka-project: --mode=onefile
# nuitka-project: --product-name=s-ball-anagram
# nuitka-project: --product-version=0.1.0
# nuitka-project: --file-description=Build anagrams matching a pattern
# nuitka-project: --copyright=Copyright s-ball 2025-current - MIT License
# nuitka-project: --onefile-tempdir-spec={CACHE_DIR}/temp

if __name__ == '__main__':
    main()