from django.http import HttpResponse
from django.shortcuts import render
from googletrans import Translator

def index(request):
    return render(request, 'index.html')

def analyse(request):
    if request.method == 'POST':
        text1 = request.POST.get('text', 'default')
        removepunc = request.POST.get('removepunc', 'off')
        capitalize = request.POST.get('capitalize', 'off')
        newlineremover = request.POST.get('newlineremover', 'off')
        extraspaceremover = request.POST.get('extraspaceremover', 'off')
        translate_to = request.POST.get('translate_to', 'off')

        if not (removepunc == 'off' and capitalize == 'off' and newlineremover == 'off' and extraspaceremover == 'off' and translate_to == 'off'):
            if removepunc == 'on':
                punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
                text1 = ''.join(char for char in text1 if char not in punctuations)

            if capitalize == 'on':
                text1 = text1.upper()

            if newlineremover == 'on':
                text1 = text1.replace('\n', '').replace('\r', '')

            if extraspaceremover == 'on':
                text1 = ' '.join(text1.split())

            if translate_to == 'on':
                translator = Translator()
                translated = translator.translate(text1, dest='mr')
                text1 = translated.text

            params = {'purpose': 'Text Analysis', 'analysed_text': text1}
            return render(request, 'analyse.html', params)

    return HttpResponse("Error: Please select at least one text analysis option")
