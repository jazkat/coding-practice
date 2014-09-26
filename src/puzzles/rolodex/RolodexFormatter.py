class RolodexFormatter(object):
    """A class for parsing and formatting contacts from a rolodex."""

    def __init__(self):
        self.data = []
        self.errors = []

    def extract(self, filename):
        # TODO
        print "OK"

    def parse(self, line):
        # TODO
        print "OK"


if __name__ == "__main__":
    import sys
    formatter = RolodexFormatter()
    formatter.extract(sys.argv[1])