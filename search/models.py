from django.db import models

# Create your models here.
class RecordMemory(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    type_document = models.TextField(help_text="Тип документа")
    content = models.TextField(help_text="Содержимое")
    period = models.TextField(help_text="Период")
    authors = models.TextField(help_text="Авторы")
    date_document = models.TextField(help_text="Дата документа")
    archive = models.TextField(help_text="Архив")
    fond = models.TextField(help_text="Фонд")
    opis = models.TextField(help_text="Опись")
    case = models.TextField(help_text="Дело")
    link = models.TextField(help_text="Ссылка на документ")
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name
