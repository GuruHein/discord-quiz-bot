from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Question(models.Model):
    LEVEL = {
        (0, _('Any')),
        (1, _('Easy')),
        (2, _('Medium')),
        (3, _('Hard')),
    }
    title = models.CharField(_('Title'), max_length=255)
    points = models.SmallIntegerField(_('Points'), default=0)
    difficulty = models.SmallIntegerField(_('Difficulty'),choices=LEVEL, default=0)
    is_active = models.BooleanField(_('Is active'), default=True)


    def __str__(self) -> str:
        return self.title


class Answer(models.Model):
    question = models.ForeignKey( Question,verbose_name=_('Question'), on_delete=models.CASCADE)
    answer = models.CharField(_('Answer'), max_length=255)
    is_correct = models.BooleanField(_('Is correct'), default=False)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    def __str__(self) -> str:
        return self.answer