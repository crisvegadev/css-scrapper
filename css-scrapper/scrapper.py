from bs4 import BeautifulSoup
import requests
import sys
import re
from termcolor import cprint, colored

tabulations = ""
counter = 0
console = False
global file


def scrapping(url, show_console, element, file_output):
    global console, file
    console = show_console

    file = open('./output/'+file_output+'.sass', "w+")

    try:
        response = requests.get(url)
    except requests.exceptions.Timeout:
        sys.exit("Timeout error")
    except requests.exceptions.TooManyRedirects:
        sys.exit("Too many redirects")
    except requests.exceptions.RequestException as e:
        raise SystemExit("Error trying to connect to the url: " + url)

    content_html = BeautifulSoup(response.content, "html.parser")
    show_classes(element, content_html)

    print("\n")
    print("Successfully scraped the url: " + url)
    print("output saved on: " + file_output+".sass")

    file.close()


def write_output(text):
    file.write(text)
    file.write("\n")


def get_classes(list_of_classes):
    classes = ""

    for single_class in list_of_classes:
        classes = classes + "." + single_class

    return classes


def get_names(element):
    name = ""

    if element.has_attr("class") and element.has_attr("id"):
        name = tabulations + element.name + get_classes(element["class"]) + "#" + element["id"]

        if console:
            print(tabulations + colored(element.name, 'red') + colored(get_classes(element["class"]),
                                                                       'green') + "#" + colored(element["id"], 'cyan'))

    elif element.has_attr("class") and not element.has_attr("id"):
        name = tabulations + element.name + get_classes(element["class"])

        if console:
            print(tabulations + colored(element.name, 'red') + colored(get_classes(element["class"]), 'green'))

    elif element.has_attr("id") and not element.has_attr("class"):
        name = tabulations + element.name + "#" + element["id"]

        if console:
            tabulations + colored(element.name, 'red') + "#" + element["id"]

    else:
        name = tabulations + element.name

        if console:
            tabulations + colored(element.name, 'red')

    write_output(name)

    if console:
        print(name)


def get_tabs(count):
    global tabulations

    tabulations = ""

    for x in range(count):
        tabulations = tabulations + "\t"


def clear_contents(element):
    list_of_elements = []
    list_of_elements.extend([c for c in element.contents if c.name != None])

    return list_of_elements


def show_classes(class_name, content_html):
    global counter, console

    if type(class_name) == str:
        element = content_html.find(class_=class_name)

        if not element:
            element = content_html.find(id=class_name)

            if not element:
                element = content_html.find(class_name)

                if not element:
                    sys.exit("No element found with class or id: " + class_name)

    else:
        element = class_name

    children = []
    children.extend([c for c in element.contents if c.name != None])

    for x in range(len(children)):

        get_tabs(counter)

        get_names(children[x])

        temp = counter

        if len(clear_contents(children[x])) > 0:
            counter = counter + 1
            show_classes(children[x], content_html)

        counter = temp
