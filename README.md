# Selenium-Website-Mapper
> Creates a tree of a website iteratively using selenium in python with anytree module

## Prerequisites
```
pip install selenium
pip install anytree
```

With python installed, there shouldn't be any problems.

Will also need to install the geckodriver for firefox, or the chromedriver for chrome. This script I'm using firefox, but there should be any difference once you change the inital lines at the top.

## Running/using

Change your link that you want to use in start-tree.json, and your driver path in the page-traverser.py

Copy start-tree.json into the tree.json file you will be using, and you're good to go.

For each depth of search, run page-traverser.py. This will look at each href in each page on the last layer of the tree. If you wanted to go to depth 3 for instance, run it 3 times.
