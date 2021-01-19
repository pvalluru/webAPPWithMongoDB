# mongo-engine packages
from mongoengine import Document, StringField, IntField



class Cafe(Document):
    """
    Template for a mongoengine document, which represents a Cafereria Creation.
    :param cafeID: unique required 12 Digit number
    :param Name: required string value
    :param Open hrs: starttime and endtime
    :param City: required string value
    :param Address: required string value
    :param pincode: unique required 6 Digit number
    """

    cafeID = IntField(required=True, min_value=12)
    name = StringField()
    city = StringField()
    pincode = IntField(unique=False, min_value=6)
    address = StringField(max_length=240)
    starttime = StringField()
    endtime = StringField()

    def save(self, *args, **kwargs):
        # Overwrite Document save method to generate password hash prior to saving
        try:
            super(Cafe, self).save(*args, **kwargs)
            return True
        except Exception as exc:
            return False


class CafeItems(Document):
    """
    Template for a mongoengine document, which represents a CafeteriaItems Creation.
    :param cafeID: unique required 12 Digit number
    :param itemID: unique required 6 Digit number
    :param Name: required string value
    :param starttime : required string value
    :param endtime : required string value
    """

    cafeID = IntField(required=True, min_value=12)
    itemID = IntField(required=True, min_value=6)
    name = StringField()
    starttime = StringField()
    endtime = StringField()

    def save(self, *args, **kwargs):
        # Overwrite Document save method to generate password hash prior to saving
        try:
            super(CafeItems, self).save(*args, **kwargs)
            return True
        except Exception as exc:
            return False