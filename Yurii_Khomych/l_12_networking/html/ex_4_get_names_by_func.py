from bs4 import BeautifulSoup

from funcs import simple_get


def get_names(url):
    """
    Downloads the page where the list of mathematicians is found
    and returns a list of strings, one per mathematician
    """
    response = simple_get(url)

    if response is not None:
        html = BeautifulSoup(response, "html.parser")
        names = set()
        for li in html.select("li"):
            for name in li.text.split("\n"):
                if len(name) > 0:
                    names.add(name.strip())
        return list(names)

    # Raise an exception if we failed to get any data from the url
    raise Exception("Error retrieving contents at {}".format(url))


if __name__ == "__main__":
    url = "http://www.fabpedigree.com/james/mathmen.htm"
    result = get_names(url=url)
    with open("names.txt", "a") as file:
        file.writelines(result)
