from threading import Thread
from bs4 import BeautifulSoup

class BeatifulThread(type):
    def __new__(cls, name, bases, dct):
        # Ensure that the class inherits from threading.Thread
        if Thread not in bases:
            bases = (Thread,) + bases

        # Ensure that the class has a 'soup' attribute
        if 'soup' not in dct:
            dct['soup'] = None

        return super().__new__(cls, name, bases, dct)

class MyThreadedClass(metaclass=BeatifulThread):
    def __init__(self, url):
        self.url = url
        super().__init__()

    def run(self):
        # Your threading logic here
        print(f"Fetching and parsing data from {self.url}")
        # Create BeautifulSoup object and store it in 'soup'
        self.soup = BeautifulSoup("<html><body><p>Example HTML</p></body></html>", "html.parser")
        print("Data fetched and parsed.")

# Example usage:
if __name__ == "__main__":
    instance = MyThreadedClass("https://example.com")
    instance.start()
    instance.join()

    # Accessing the BeautifulSoup object
    print("Soup object:", instance.soup)
