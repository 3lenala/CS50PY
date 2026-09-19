""" This program aims to get the youtube link of a video embedded in an HTML iframe element.
 The returned link will be modified so that it is given in a shorten youtu.be version."""

import re

SHORT_URL = r'https://youtu.be/'  # regular expression for the shorten URL
# regular expression for the original URL
YOUTUBE_EMBED = r'(?:https?://)?(?:www\.)?youtube\.com/embed/'
# regular expression for an HTML iframe element
HTML_URL = rf'^<iframe.+({YOUTUBE_EMBED}[\w-]+).+</iframe>$'


def main():
    """Prompt the user for an HTML iframe and print the shortened YouTube URL."""
    print(parse(input("HTML: ")))


def parse(s):
    """Extract a YouTube URL from an HTML iframe and return its shortened version."""
    if url := extract(s):
        return shorten(url)
    return None


def extract(iframe_str):
    """Extract and return the YouTube embed URL from an HTML iframe string."""
    if match := re.search(HTML_URL, iframe_str):
        return match.group(1)
    return None


def shorten(url):
    """Convert a YouTube embed URL into its shortened youtu.be format."""
    return re.sub(YOUTUBE_EMBED, SHORT_URL, url)


if __name__ == "__main__":
    main()
