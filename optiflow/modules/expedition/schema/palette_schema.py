from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import validates, ValidationError
from datetime import date
from optiflow.modules.expedition.models import Palette


class PaletteSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Palette
        load_instance = True  # Permet de créer directement un objet Palette
        include_fk = True     # Inclut la clé étrangère client_id
        exclude = ("client",) # Évite la récursion lors des relations

    @validates("nombre_uvc")
    def validate_nombre_uvc(self, value):
        if value < 0:
            raise ValidationError("Le nombre d'UVC doit être positif.")

    @validates("nombre_palette")
    def validate_nombre_palette(self, value):
        if value < 0:
            raise ValidationError("Le nombre de palettes doit être positif.")

    @validates("date_commande")
    def validate_date_commande(self, value):
        if value > date.today():
            raise ValidationError("La date de commande ne peut pas être dans le futur.")