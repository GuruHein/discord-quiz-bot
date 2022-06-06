from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serailizers import QuestionSerializer
from .models import Question

# Create your views here.
class QuestionAPIView(generics.GenericAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.filter(is_active=True).order_by('?')

    def get(self, request):
        question = self.queryset.first()
        serailizer = self.serializer_class(question)
        return Response(serailizer.data)
