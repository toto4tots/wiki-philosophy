import sys
from get_first_link import get_first_link


MAX_HOPS = 100
PHILOSOPHY = "https://en.wikipedia.org/wiki/Philosophy"


def main(curr_url):
    hop_num = 0
    visited = []
    while hop_num <= MAX_HOPS:
        print(curr_url)
        if curr_url == PHILOSOPHY:
            print(f"{hop_num} hops")
            return
        next = get_first_link(curr_url, visited)
        if next:
            hop_num += 1
            visited.append(next)
            curr_url = next
        else:
            print("No valid url to hop to!")
            print(f"{hop_num} hops")
            return
    print("Ran out of hops!")
    print(f"{MAX_HOPS} hops")
    return


starting_url = sys.argv[1]
main(starting_url)
