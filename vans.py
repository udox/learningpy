import urllib
from BeautifulSoup import BeautifulSoup

"""
    TASK
    Write a function that uses BeautifulSoup to get titles and summaries of posts on
    vans.com's news search: http://www.vans.com/news/search/?search_keywords=KEYWORDHERE

    Try http://www.vans.com/news/search/?search_keywords=rowley and you'll get news posts.
    You want to grab the titles and summary from the results returned. Send them back in a
    list like:

    [('Title 1', 'Im the summary'), ('Post #2', 'Hey, im content from post 2...')]

    See http://www.crummy.com/software/BeautifulSoup/documentation.html#Parsing a Document
    for more information on how BS. works. Use the function below as a starting point.

    Things to do:

    1. Make the function load the html of *any* page that it's given (so add an argument)
    2. Use the BeautifulSoup function findAll to get all the result links out - you'll
        need to see if there's a common name to them in the google result html source.
    3. Extract just the href and put that into a list. Return that list.

    Things to remember:

    1. Your code should be generic as much as possible - a function that just loads *one*
        specifc url isn't as usful as a function that loads any
    2. You should break your code into chunks - functions should be small and do one task
        rather than handle a group of only semi-related items (i.e. could the part of teh code
        that reads the url and then pulls out certain tags be split in two distinct bits?)
"""

def load_vans():
    """
        Loads up the u-dox page using urllib and reads it into a variable.
        Then we turn that content into some soup that lets us pull out html.
        As an example we find all the meta tags and print them
    """

    url = 'http://www.vans.com/news/search/?search_keywords=skate'
    page_html = urllib.urlopen(url).read()
    page_soup = BeautifulSoup(page_html)
    posts = page_soup.findAll(attrs={'class':'post'})
    results = []
    for post in posts:
        header = post.find('h3').string
        sentence = unicode(post.find('p'))
        results.append (header + sentence)
    return results

# This is a special thing in python. When you call the script with "python SCRIPTNAME.py" it
# will execute the code below when it runs.
if __name__=='__main__':
    results = load_vans()
    print "\n\n".join(results)
    