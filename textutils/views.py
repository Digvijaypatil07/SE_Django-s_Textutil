#i have created this file
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    # return HttpResponse('''<a href="https://moodle.coep.org.in/moodle/login/index.php">COEP MOODLE</a>''')
    
    return render(request,'index.html')
    
def analyse(request):
    #get the text
    text1 = request.POST.get('text','default')
    # check checkbox value
    removepunc = request.POST.get('removepunc','off')
    capitilize = request.POST.get('capitilize','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    # print(text1)
    # print(removepunc)
    
    if (removepunc == 'on'):
    
          punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
          analysed =''
          for char in text1:
               if char not in punctuations:
                  analysed = analysed + char
          params ={'purpose':'Removed Punctuations','analysed_text':analysed,}
          text1=analysed
        #   return render(request,'analyse.html',params)
    
    if (capitilize=="on"):
        analysed=''
        for char in text1:
            analysed=analysed+char.upper()
        params ={'purpose':'Capitilse text','analysed_text':analysed,}
        text1=analysed
        # return render(request,'analyse.html',params)
    
    if (newlineremover=="on"):
        analysed=""
        for char in text1:
            if char !="\n" and char !='\r':
                analysed=analysed +char
        params ={'purpose':'New Line Remover','analysed_text':analysed,}
        text1=analysed
        # return render(request,'analyse.html',params)                      
    
    if (extraspaceremover =="on"):
        analysed=""
        for index,char in enumerate(text1):
            if not(text1[index] ==" " and text1[index +1] ==" "):
                analysed=analysed +char
        params ={'purpose':'extra space Remover','analysed_text':analysed,}
        text1=analysed
        # return render(request,'analyse.html',params)
    
    if(extraspaceremover !="on" and newlineremover !="on" and capitilize !="on" and removepunc !="on"):
        return HttpResponse("Error")
    return render(request,'analyse.html',params)

# def spaceremover(request):
#     return HttpResponse("space remover")
