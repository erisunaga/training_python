from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

# 選択肢カテゴリのコード候補を定義
CODE_CHOICES = [
    ('A', 'radio'),
    ('B', 'check'),
]
class ChoiceCategory(models.Model):
    code = models.CharField(max_length=16, unique=True, choices=CODE_CHOICES)

class Question(models.Model):
    answer_category = models.ForeignKey(
        ChoiceCategory, on_delete=models.PROTECT, related_name="questions", null=True
    )

class QuestionParagraph(models.Model):
    """問題文を段落・設問A/B/C等に分割して順序付きで保持。"""
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="paragraphs"
    )
    paragraph_text = models.TextField()  # 段落の本文を格納
    order = models.PositiveIntegerField(default=0)  # 段落の順番を管理

    class Meta:
        ordering = ['order']  # デフォルトで order 順に並べる

class Choice(models.Model):
    """選択肢（単一/複数選択で使用）。"""
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="choices"
    )

class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True,
        on_delete=models.SET_NULL, related_name="quiz_answers"
    )
    selected_choice = models.ForeignKey(
        Choice, null=True, blank=True, on_delete=models.SET_NULL,
        related_name="single_answers"
    )  # SINGLE 用（MULTIPLEでは使わない）
    # MULTIPLE 用：多対多（中間表 AnswerChoice 経由）
    selected_choices = models.ManyToManyField(
        Choice, through="AnswerChoice", related_name="multi_answers", blank=True
    )
    answer_text = models.TextField()

class AnswerChoice(models.Model):
    """複数選択(MULTIPLE)用の中間表。"""
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    
