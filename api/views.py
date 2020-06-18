from django.http import Http404
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from man.models import Man
from .serializers import ManSerializers, SendSerializers


class ManAPIView(generics.ListAPIView):
    queryset = Man.objects.all()
    serializer_class = ManSerializers


class NumberAPI(generics.RetrieveAPIView):
    queryset = Man.objects.all()
    serializer_class = SendSerializers

    def get_object(self, number):
        try:
            return Man.objects.get(number=number)
        except Man.DoesNotExist:
            raise Http404

    def get(self, request, number, format=None):
        snippet = self.get_object(number=number)
        serializer = SendSerializers(snippet)
        return Response(serializer.data)