from django.db.models import Model, CharField, SlugField, ImageField, DecimalField, ForeignKey, CASCADE, JSONField, \
    TextField, PositiveIntegerField, FileField


class Category(Model):
    name = CharField(max_length=100)
    slug = SlugField(max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=100)
    image = ImageField(upload_to='products', null=True, blank=True)
    year = PositiveIntegerField()
    engine_size = DecimalField(max_digits=5, decimal_places=2)
    mileage = PositiveIntegerField(default=0)
    transmission = CharField(max_length=100)
    price = DecimalField(max_digits=10, decimal_places=2)
    category = ForeignKey(Category, on_delete=CASCADE)

    def __str__(self):
        return self.name


class CharactererAvto(Model):
    user_id = CharField(max_length=100)
    title = CharField(max_length=100)
    description = JSONField()
    status = TextField()
    price = DecimalField(max_digits=5, decimal_places=2, default=0)


class ElonCharacter(Model):
    elon = CharField(max_length=100)
    parametres = ForeignKey('Parametres', on_delete=CASCADE)
    parametres_item = ForeignKey('ParametresItem', on_delete=CASCADE)
    parametres_value = CharField(max_length=100)


class Parametres(Model):
    name = CharField(max_length=100)
    param_type = CharField(max_length=100)
    measure = ForeignKey('Measure', on_delete=CASCADE)

    def __str__(self):
        return self.name


class Type(Model):
    name = CharField(max_length=100)
    code = PositiveIntegerField()

    def __str__(self):
        return self.name


class Measure(Model):
    name = CharField(max_length=100)
    short_name = CharField(max_length=100)

    def __str__(self):
        return self.name


class ParametresItem(Model):
    parametres = ForeignKey(Parametres, on_delete=CASCADE)
    name = CharField(max_length=100)
    value = CharField(max_length=100)
    file = ForeignKey('Files', on_delete=CASCADE)

    def __str__(self):
        return self.name


class Files(Model):
    file = FileField(upload_to='files')

    def __str__(self):
        return str(self.file)


class ElonFiles(Model):
    elon = ForeignKey('ElonCharacter', on_delete=CASCADE)
    file = ForeignKey(Files, on_delete=CASCADE)


class Status(Model):
    name = CharField(max_length=100)
    description = JSONField()
    code = PositiveIntegerField()

    def __str__(self):
        return self.name


class User(Model):
    name = CharField(max_length=100)
    phone_number = CharField(max_length=100)
    photo = ForeignKey(Files, on_delete=CASCADE)

    def __str__(self):
        return self.name

