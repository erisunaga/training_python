from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-id")[:5]

    # 各Questionの段落もまとめて渡す
    questions_with_paragraphs = []
    for question in latest_question_list:
        paragraphs = question.paragraphs.all()  # related_name="paragraphs"
        questions_with_paragraphs.append({
            "question": question,
            "paragraphs": paragraphs
        })
    
    context = { "questions_with_paragraphs": questions_with_paragraphs}
    return render(request, "app_20250822/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    paragraphs = question.paragraphs.all()  # ←ここで取得
    answers = question.answers.all()
    
    # 回答形式を切り替えるためにカテゴリを参照
    category = question.answer_category.code if question.answer_category else "text"

    context = {
        "question": question,
        "paragraphs": paragraphs,          # ← context に渡す
        "category": category,
        "answers": answers,
    }
    

    return render(request, "app_20250822/detail.html", context)
