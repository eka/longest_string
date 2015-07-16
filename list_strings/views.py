from django.shortcuts import render

# Create your views here.
from list_strings.forms import ListStringsForm
from list_strings.utils import longest_substring
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


def home(request):
    res = ''
    if request.method == 'POST':
        form = ListStringsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['strings']
            data = data.strip().split("\n")
            res = longest_substring(data)
    else:
        form = ListStringsForm()

    dd = {
        'form': form,
        'res': res,
    }

    return render(request, 'list_strings/index.html', dd)

class LongestStringRESTView(APIView):

    def _process(self, data):
        print("**** data {}".format(data))
        data = data.strip().split("\n")
        res = longest_substring(data)
        return res

    def post(self, request, *args, **kw):
        print("request.POST {}".format(request.POST))
        result = self._process(request.POST.get('data', ''))
        result = {'result': result}
        response = Response(result, status=status.HTTP_200_OK)
        return response

    def get(self, request, *args, **kw):
        print("request.GET {}".format(request.GET))
        # Process any get params that you may need
        # If you don't need to process get params,
        # you can skip this part
        result = self._process(request.GET.get('data', ''))
        result = {'result': result}
        response = Response(result, status=status.HTTP_200_OK)
        return response

