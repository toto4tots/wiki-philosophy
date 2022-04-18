# Getting to Philosophy

Given a valid wikipedia url, the program takes the first link of the page and repeats this process until it reaches the philosophy page.

- https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy
- https://en.wikipedia.org/wiki/Philosophy

## Installing Dependencies

Uses Requests library for sending HTTP requests and Beautiful Soup for parsing.
To install:

```bash
pip3 install -r requirements.txt
```

## Running the Program

```bash
python3 getting_to_philosophy.py '<WIKI_URL>'
```

For example

```bash
python3 getting_to_philosophy.py 'https://en.wikipedia.org/wiki/Get_It_Together_(The_Jackson_5_song)'
```

## Testing

Tests rely on pre-downloaded files found in the `downloaded` folder. Currently there is one valid (`epistemology.txt`) and one invalid (`invalid.txt`). To run

```bash
python3 get_first_link_test.py
```
