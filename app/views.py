

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework import status
from .models import Trader, TraderData
from .serializers import TraderDataSerializer


class TraderDetailsView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            trader = request.user.trader
            subjects = Trader.objects.filter(name=trader.name)
            serializer = TraderDataSerializer(subjects, many=True)
            return Response(serializer.data)
        except AttributeError:
            return Response(
                {"message": "You are not authorized to view this resource."},
                status=status.HTTP_403_FORBIDDEN,
            )
        except Exception as e:
            return Response(
                {"message": f"An error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
