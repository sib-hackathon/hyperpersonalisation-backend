from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.db.models import IntegerField
from django.db.models import F
from django.db.models import ExpressionWrapper
from .models import Transaction  # Import your Transaction model

class DebitLimitSuggester(APIView):
    def get(self, request):
        # Get the user making the request
        user = request.user

        # Calculate the total amount spent by the user in each month
        monthly_spending = (
            Transaction.objects
            .filter(payed_by=user)
            .annotate(month=TruncMonth('date_created'))
            .values('month')
            .annotate(total_spent=Sum('amount'))
            .order_by('month')
        )

        # Assuming you want to suggest a limit for each month as 80% of the average monthly spending
        monthly_suggestions = []
        for entry in monthly_spending:
            month = entry['month']
            total_spent = entry['total_spent']

            # Calculate the suggested monthly limit (e.g., 80% of the average spending)
            suggested_limit = int(0.8 * total_spent)

            # You can further customize the suggested limit based on your requirements

            monthly_suggestions.append({
                'month': month,
                'total_spent': total_spent,
                'suggested_limit': suggested_limit,
            })

        return Response({
            'suggestions': monthly_suggestions
        })
