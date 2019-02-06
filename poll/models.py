from django.db import models


class QuestionSet(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name or "Zestaw Pytań"

    def which_set_element(self, question):
        for index, s in enumerate(self.question_set.all()):
            return index


class Question(models.Model):
    question_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now_add=True)
    open_question = models.BooleanField()
    question_set = models.ForeignKey(QuestionSet, blank=True, null=True, on_delete=models.SET_NULL)
    audio_file = models.FileField(upload_to='audio', blank=True, null=True)

    def __str__(self):
        return self.question_text

    def which_set_element(self):
        return self.question_set.which_set_element(self)

    def get_next_question(self):
        return self.question_set.question_set.all()[self.which_set_element() + 1]


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=500)

    def __str__(self):
        return self.choice_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, editable=False)
    open_answer = models.CharField(max_length=500, blank=True, editable=False)
    closed_answer = models.ForeignKey(Choice, on_delete=models.CASCADE, blank=True, null=True, editable=False)
    person = models.CharField(max_length=50, editable=False)

    @staticmethod
    def create_closed(person, closed_answer, question):
        Answer(person=person, closed_answer=closed_answer, question=question).save()

    @staticmethod
    def create_open(person, open_answer, question):
        Answer(person=person, open_answer=open_answer, question=question).save()

    def __str__(self):
        if self.closed_answer:
            return f"{self.person}, {self.question}, {self.closed_answer}"
        return f"{self.person}, {self.question}, {self.open_answer}"
