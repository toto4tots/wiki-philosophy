import sys
from bs4 import BeautifulSoup
import requests
from constants import WIKIPEDIA, WIKIPATH



def _get_first_link_helper(html, visited):

    """
    The helper function extracts the first link in the content body of the wikipedia page

    Implementation doesn't consider italics or parenthesis.
    Heavily relies on Wikipedia structure to not change

    """

    def is_valid(path):
        if (
            ":" in path
            or "#" in path
            or not path.startswith(WIKIPATH)
            or WIKIPEDIA + path in visited
        ):
            return False
        return True

    soup = BeautifulSoup(html, "html.parser")
    p_elements = soup.find("div", class_="mw-parser-output").find_all("p")
    for p_elem in p_elements:
        a_elements = p_elem.find_all("a")
        for a_elem in a_elements:
            if is_valid(a_elem["href"]):
                return WIKIPEDIA + a_elem["href"]
    return None  # no valid urls


def get_first_link(url, visited):
    html = requests.get(url).text
    return _get_first_link_helper(html, visited)
