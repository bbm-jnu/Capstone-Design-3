from urllib.request import urlopen
from html.parser import HTMLParser
import os
from http.client import HTTPConnection
from urllib.parse import urljoin, urlunparse
from urllib.request import urlretrieve
from html.parser import HTMLParser

class ImageParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result = []
        for name, value in attrs:
            if name == 'src':
                if not value.find('/image/jnu/icons/icon') == -1:
                    self.result.append(value)

def download_image(url, data):
    if not os.path.exists('jejunu'):
        os.makedirs('jejunu')
    parser = ImageParser()
    parser.feed(data)
    dataSet = set(x for x in parser.result)
    for x in sorted(dataSet) :
        imageUrl = urljoin(url, x)
        basename = os.path.basename(imageUrl)
        targetFile = os.path.join('jejunu', basename)
        print("Downloading...", imageUrl)
        urlretrieve(imageUrl, targetFile)

def main():
    url = "http://www.jejunu.ac.kr"
    data = urlopen(url).read().decode('utf-8')
    print("\n>>>>>>>>> Download Images from", url)
    download_image(url, data)


if __name__ == '__main__':
    main()



