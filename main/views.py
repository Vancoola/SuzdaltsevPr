from django.shortcuts import render
from .models import ItemModels
from django.http import JsonResponse
import stripe


# Create your views here.

def index(request, pk):
    if request.method == 'GET':
        return render(request, 'index.html', {'items': ItemModels.objects.filter(id=pk)})
    else:
        return JsonResponse({'error': 'only GET!'})


def buy(request, pk):
    item = ItemModels.objects.get(id=pk)
    stripe.api_key = 'sk_test_51OPTgAHzaSo6OINVPmF0zIYQIgpBqcqZxhFdyzQ81NNIjSMxHe3nOCdzx3siBpT2B9aEe84IC5ApSHixMG8Z8DA8009HaKGVkr'
    return JsonResponse(dict(stripe.checkout.Session.create(success_url="https://example.com/success",
                                                            line_items=[{"price": item.item_token, "quantity": 1}],
                                                            mode="payment", ))['id'], safe=False)
