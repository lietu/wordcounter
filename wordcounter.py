#!/usr/bin/env python

"""
WordCounter
===========

Counts most common words in text data.

Distributed with the MIT and new BSD licenses. Exact license text below.


The "New" BSD License:
----------------------

Copyright (c) 2015, Janne Enberg
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

  * Redistributions of source code must retain the above copyright notice, this
    list of conditions and the following disclaimer.
  * Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.
  * Neither the name of the project nor the names of its contributors
    may be used to endorse or promote products derived from this software
    without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


MIT License
-----------

Copyright (c) 2015, Janne Enberg

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

USAGE = """
You can invoke this tool by giving it the names of files to process:
{name} filename [filename...]

Alternatively pipe in data to process:
cat filename | {name}

This tool will calculate the most used words in the input data and report it's
findings.
"""

import sys
import re
import time

# How many of the top words to show at most
MAX_MATCHES = 50

# How to match words
WORD_MATCH = re.compile('[A-Za-z0-9]+')


def usage():
    """
    Show application usage
    """

    print(USAGE.format(
        name=sys.argv[0]
    ))


def have_stdin():
    """
    Check if we have data in STDIN
    :return bool:
    """

    return not sys.stdin.isatty()


def process_line(line, counters):
    """
    Process a single line of input into counters

    :param str line: The line to process
    :param dict counters: An existing counters object
    """

    words = 0
    for word in WORD_MATCH.findall(line):
        words += 1
        if not word in counters:
            counters[word] = {
                "word": word,
                "count": 1
            }
        else:
            counters[word]["count"] += 1

    return words


def process_data(data_sources):
    """
    Process all the data sources

    :param list data_sources: List of readable data sources
    :return dict: The word counts
    """

    words = 0
    counters = {}
    for data_source in data_sources:
        for line in data_source:
            words += process_line(line, counters)

    return words, counters


def report(counters, extra_data):
    """
    Print out the report of the counters

    :param dict counters:
    """

    print("Most used words in the source data:")

    index = 0
    for key in sorted(counters, reverse=True,
                      key=lambda key: counters[key]["count"]):
        item = counters[key]
        index += 1

        print("#{i}: {word} ({count})".format(
            i=index,
            word=item["word"],
            count=item["count"]
        ))

        if index >= MAX_MATCHES:
            break

    print("Time elapsed: {0:.3f} seconds".format(extra_data["time_elapsed"]))
    print("Total of {0:,} words in input data".format(extra_data["words"]))


if __name__ == "__main__":

    data_sources = []
    if have_stdin():
        data_sources = [sys.stdin]
        print("Reading data from STDIN")

    if len(sys.argv) >= 2:
        for fname in sys.argv[1:]:
            print("Opening file {0}".format(fname))

            try:
                f = open(fname)
            except IOError:
                usage()
                print("ERROR: Failed to open file {0}".format(fname))
                sys.exit(1)

            data_sources.append(f)

    if len(data_sources) == 0:
        usage()
        sys.exit(1)

    extra_data = {}

    start_time = time.time()
    words, counters = process_data(data_sources)
    end_time = time.time()

    extra_data["time_elapsed"] = end_time - start_time
    extra_data["words"] = words
    report(counters, extra_data)
