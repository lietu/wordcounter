Word Counter
============

Simple word counting tool. You can provide input data via STDIN and/or in form 
of source filenames. The tool reads all the input data and counts words in them
and then reports the most common words and how many matches there were.


Status
------

[![Build Status](https://travis-ci.org/lietu/wordcounter.svg?branch=master)](https://travis-ci.org/lietu/wordcounter)


Usage
-----

Example usage via STDIN:
```
find / | python wordcounter.py
```

Example usage via filenames:
```
python wordcounter.py testdata.txt /proc/cpuinfo
```

Example combined usage:
```
ps axu | python wordcounter.py /proc/modules
```

The tool should work on both \*nix systems and Windows.


License
-------

The code is licensed with both MIT and new BSD licenses.

Full text available in `wordcounter.py`.


Financial support
=================

This project has been made possible thanks to [Cocreators](https://cocreators.ee) and [Lietu](https://lietu.net). You can help us continue our open source work by supporting us on [Buy me a coffee](https://www.buymeacoffee.com/cocreators).

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/cocreators)
