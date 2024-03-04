from django.db import models
from django.utils.translation import gettext_lazy as _

class Faq(models.Model):
    
    question_fa = models.CharField(_("question_fa"), max_length=50)
    answer_fa = models.TextField(_("answer_fa"))
        
    question_en = models.CharField(_("question_en"), max_length=50)
    answer_en = models.TextField(_("answer_en"))
    
    def __str__(self):
        return f'{self.question_en}'