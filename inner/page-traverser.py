from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC # Selenium imports
import selenium.common.exceptions
from anytree import AnyNode, LevelOrderGroupIter
from anytree.exporter import JsonExporter
from anytree.importer import JsonImporter
import json
import time

def gethref(a, maxtries):
    tries = 0
    while tries < maxtries:
        try:
            href = a.get_attribute("href")
            return href
        except selenium.common.exceptions.StaleElementReferenceException:
            tries += 1
    return ""

with open("inner/tree.json", "r") as f:
    jsontree = json.load(f)

with open("inner/links.json", "r") as f:
    jsonlinks = json.load(f)
    startlink = jsonlinks[0]
    linklength = len(startlink)

options=Options()
options.headless = True
service = Service(r'DRIVER LOCATION') # path of firefox driver
driver = Firefox(service=service, options=options)

importer = JsonImporter()
tree = importer.import_(jsontree)

PrevLevel = [[node for node in children] for children in LevelOrderGroupIter(tree)]

for link in PrevLevel[-1]:
    t1 = time.time()
    try:
        driver.get(link.name) # Start the window
    except selenium.common.exceptions.InvalidArgumentException:
        print("Invalid url", link.name)

    try:
        links = ui.WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//a[@href]")))
    except selenium.common.exceptions.UnexpectedAlertPresentException:
        print("Expected sign-in at", link.name)

    print(f"{len(links)} links found {link.name}, node {PrevLevel[-1].index(link)} of {len(PrevLevel[-1])} links. ", end='')
    for a in links:
        href = gethref(a, 3)
        if href == "":
            continue
        if len(href.split("#")) == 2:
            href = href.split("#")[0]
        try:
            if href[:linklength] != startlink:
                continue
        except IndexError:
            continue
        if href not in jsonlinks:
            AnyNode(name=href, parent=link)
            jsonlinks.append(href)
    print(str(time.time()-t1)[:5])
            
exporter = JsonExporter(sort_keys=True)
exporttree = exporter.export(tree)
with open("inner/tree.json", "w") as f:
    json.dump(exporttree, f)
with open("inner/links.json", "w") as f:
    json.dump(jsonlinks, f)
