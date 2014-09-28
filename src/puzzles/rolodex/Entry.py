class Entry(object):
    """A class for manipulating data contained in a
     valid entry in the rolodex."""

    def __init__(self, color=None, first=None, last=None, phone=None, zip_code=None):
        self.color = color
        self.first_name = first
        self.last_name = last
        self.phone = phone
        self.zip = zip_code

    def last_first(self):
        return self.last_name + ", " + self.first_name

    def __eq__(self, other):
        return self.last_first() == other.last_first()

    def __ne__(self, other):
        return self.last_first() != other.last_first()

    def __lt__(self, other):
        return self.last_first() < other.last_first()

    def __le__(self, other):
        return self.last_first() <= other.last_first()

    def __gt__(self, other):
        return self.last_first() > other.last_first()

    def __ge__(self, other):
        return self.last_first() >= other.last_first()

    def json_prep(self):
        return dict(zip(
            ['color', 'firstname', 'lastname', 'phonenumber', 'zipcode'],
            [self.color, self.first_name, self.last_name, self.phone, self.zip]))