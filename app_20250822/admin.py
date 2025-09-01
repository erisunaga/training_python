from django.contrib import admin

from .models import Question
from .models import Choice
from .models import ChoiceCategory
from .models import QuestionParagraph
from .models import Answer
from .models import AnswerChoice

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(ChoiceCategory)
admin.site.register(QuestionParagraph)
admin.site.register(Answer)
admin.site.register(AnswerChoice)
