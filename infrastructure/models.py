from mongoengine import Document, EmbeddedDocument, fields


class Location(EmbeddedDocument):
  type = fields.StringField(required=True)
  coordinates = fields.ListField()


class Infrastructure(Document):
  name = fields.StringField(required=True)
  type_infrastructure = fields.StringField()
  location = fields.EmbeddedDocumentField(Location)
  meta = {
      'indexes': [[("location", "2dsphere")]]
  }

  def __str__(self):
      return self.name
