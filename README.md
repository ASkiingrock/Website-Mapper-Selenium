# Selenium-Website-Mapper
> Creates a tree of a website iteratively using selenium in python with anytree module

## Prerequisites
```
pip install selenium
```
```
pip install anytree
```

With python installed, there shouldn't be any problems.

Will also need to install the geckodriver for firefox, or the chromedriver for chrome. This script I'm using firefox, but there should be any difference once you change the inital lines at the top.

## Running/using

Change your link that you want to use in start-tree.json, and your driver path in the page-traverser.py

Copy start-tree.json into the tree.json file you will be using, and links.json into the links.json into the folder you will be using.

For each depth of search, run page-traverser.py. This will look at each href in each page on the last layer of the tree. If you wanted to go to depth 3 for instance, run it 3 times.

## Full vs Inner

Use the scripts from the approprite folder depending on what you want.

#### Full
Follows any valid link, including those outside the domain of the original link.

#### Inner
Will only record hrefs which are within the domain of the original link

## File purposes

So, there are a fair amount of files for a pretty simple script. 

**Links.json** contains all the mapped links so far.
**Page-traverser.py** is the script that will add nodes to the tree.
**Tree.json** is the tree.

#### Utility files

Most of these are purely for convenience.

**Select-individual-pages.py** will just print a list of all the unique pages under the domain which you have mapped. This doesn't apply to the Full folder really, so it's only in Inner at the moment.
**Tree-render.py** will just use the *RenderTree()* function from Anytree and export it to **tree.txt**
**Tree-image.py** will generate **tree.dot**, which can then be converted into an image using Graphviz

## Graphviz

Download Graphviz, and add it to your path variable. Open command prompt and use:
```dot -DOTFILEPATH -T png -o -OUTPUTFILEPATH```
This will create a graphical representation of the tree. Unfortunately, usually these trees get very wide very quickly, so the graphs often turn out unreadable due to the sheer number of links involved.




