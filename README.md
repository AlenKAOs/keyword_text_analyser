# keyword_text_analyser
keyword_text_analyser is a library which extracts keywords from a given string using the TextRank algorithm which is based on the PageRank algorithm.

### Tech

keyword_text_analyser uses a number of open source projects to work properly:

* [numpy] - The fundamental package for scientific computing with Python.
* [scipy] - Open-source software for mathematics, science, and engineering.

### Installation

keyword_text_analyser requires [pip](https://pypi.org/) to run.

Install the dependency.

```sh
$ pip install keyword_text_analyser
```

### Usage

Simply import keyword_text_analyser in the py file you want to use it:

```sh
from keyword_text_analyser import TextRank4Keyword
```

Then instantiate the TextRank4Keyword class where you access these functions to extract the keywords from the string provided

```sh
text = 'Some String to extract keywords from'

tr4w = TextRank4Keyword()
tr4w.analyze(text)

keywords = tr4w.get_keywords()
```

License
----

MIT
