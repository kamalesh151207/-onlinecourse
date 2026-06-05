from django.shortcuts import get_object_or_404, render
from .models import Course, Enrollment, Question, Choice, Submission

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    questions = Question.objects.filter(course=course)
    selected_choices = []

    for question in questions:
        choice_ids = request.POST.getlist(str(question.id))
        selected_choices.extend(choice_ids)

    enrollment = Enrollment.objects.first()

    submission = Submission.objects.create(
        enrollment=enrollment,
    )

    submission.choices.set(selected_choices)

    context = {
        'course': course,
        'submission': submission,
    }

    return render(request, 'exam_result_bootstrap.html', context)


def show_exam_result(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    submission_id = request.GET.get('submission-id')
    submission = Submission.objects.get(id=submission_id)

    choices = submission.choices.all()

    total = 0
    correct = 0

    for choice in choices:
        if choice.is_correct:
            correct += 1
        total += 1

    grade = 0
    if total > 0:
        grade = round((correct / total) * 100, 2)

    context = {
        'course': course,
        'submission': submission,
        'grade': grade,
    }

    return render(request, 'exam_result_bootstrap.html', context)
