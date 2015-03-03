Word Counter
============

Simple word counting tool. You can provide input data via STDIN and/or in form 
of source filenames. The tool reads all the input data and counts words in them
and then reports the most common words and how many matches there were.

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
