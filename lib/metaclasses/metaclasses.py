from threading import Thread
from bs4 import BeautifulSoup

class ThreadMeta(type(Thread)):
    pass

class BeautifulSoupMeta(type(BeautifulSoup)):
    pass

class MyMeta(ThreadMeta, BeautifulSoupMeta):
    pass

class MyThreadWithBeautifulSoup(metaclass=MyMeta):
    def __init__(self, target, args=(), kwargs=None, soup_html=''):
        if kwargs is None:
            kwargs = {}

        self.thread = Thread(target=target, args=args, kwargs=kwargs)
        self.soup = BeautifulSoup(soup_html, 'html.parser')

    def start(self):
        self.thread.start()

    def join(self):
        self.thread.join()

    def prettify(self):
        return self.soup.prettify()

# Example usage
    # Create an instance of MyThreadWithBeautifulSoup
my_instance = MyThreadWithBeautifulSoup(
    target=lambda: print("Hello, I am a thread!"),
    args=(),
    kwargs={},
    soup_html='<html><body><p>Hello, I am BeautifulSoup!</p></body></html>'
)

# Start the thread
my_instance.start()
my_instance.join()

# Access attributes from Thread and BeautifulSoup
print(my_instance.prettify())
