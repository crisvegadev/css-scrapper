# css scrapper

A simple css scraper that can be used to extract the style structure of website.

## Features

* Extract the style structure of website.
* output the style structure in sass format.

# Installation

## Manual
```bash
  $ git clone https://github.com/crisvegadev/css-scrapper
  $ cd css-scrapper
  $ python setup.py install
```

# Usage
```bash
$ python css-scrapper scrap --url https://www.google.com --element body --output output.sass --show-output
```
This will output the style structure of the website and saved in the directory:

```bash
'./output/results.sass'.
```

## Options

* --url:The url of the website that you want to extract the style structure.
* --element:The element that you want to extract the style structure.
* --output: The output file name.
* --show-output: Show the output of the scrapper in console.
* --help: Show the help.

## Example
Content of the file:

```
'./output/results.sass'
```

```sass
.container
  .row
    .col-md-4
    .col-md-4
    .col-md-4

 ```




