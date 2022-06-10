from django import forms
from pybo.models import Question

class QuestionForm(forms.ModelForm): # 장고 폼은 2개의 폼으로 구분되는데 forms.Form을 상속받으면 폼, forms.ModelForm을 상속받으면 모델 폼이라 함
    class Meta: # 장고 모델폼은 내부 클래스로 Meta 클래스를 반드시 가져야 함, 모델과 모델 필드를 작성해야 함
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }

