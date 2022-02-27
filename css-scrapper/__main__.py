from email.policy import default
import sys
import click
from scrapper import scrapping


@click.group()
@click.version_option("1.0.0")
def main():
    """A simple scrapper for get the css structure of a website"""
    pass

@main.command()
@click.option('-u', '--url', 'website', required=True)
@click.option('--show-output', 'show_output', is_flag=True)
@click.option('--element', 'element', required=True)
@click.option('--output', 'output', required=False, default="results.sass")
def scrap(website, show_output, element, output):
    scrapping(website, show_output, element, output)

if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("CSS Scrapper")
    main()
