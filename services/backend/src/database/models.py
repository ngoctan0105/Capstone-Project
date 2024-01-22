from tortoise import fields, models

class Plant_Diseases(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    plant = fields.CharField(max_length=255)
    disease = fields.CharField(max_length=255)
    symptoms = fields.JSONField()
    causes = fields.JSONField()
    measures = fields.JSONField()

    def __str__(self):
        return str(self.id)