

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .models import Trader, TraderData
from .serializers import TraderDataSerializer, TraderSerializer


class TraderDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            trader = request.user.trader
            subjects = Trader.objects.filter(name=trader.name)
            serializer = TraderSerializer(subjects, many=True)
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


class GraphDataViews(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            trader = request.user.trader
            graph_data = TraderData.objects.filter(trader=trader)
            serializer = TraderDataSerializer(graph_data, many=True)
            return Response(serializer.data)

        except Exception as e:

            return Response(
                {"message": f"An error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class AdminDashboardView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        traders = Trader.objects.all()
        trader_data = []
        for trader in traders:
            # Fetch the performance data for each trader
            trader_data_queryset = TraderData.objects.filter(trader=trader)
            trader_data_serializer = TraderDataSerializer(
                trader_data_queryset, many=True)

            # Access the total_balance field of the Trader object
            total_balance = trader.total_balance

            # Extract necessary information from the User object
            # Access the `username` field of the related User object
            trader_name = trader.name.username
            trader_data.append({
                'trader_name': trader_name,
                'total_balance': total_balance,  # Include total_balance in the response
                'data': trader_data_serializer.data
            })

        return Response(trader_data)
