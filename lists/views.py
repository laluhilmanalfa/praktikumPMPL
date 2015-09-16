
from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item


#def home_page(request):
 #   if request.method == 'POST':
  #      return HttpResponse(request.POST['item_text'])
   # return render(request, 'home.html')
#def home_page(request):
 #   return render(request, 'home.html', {
  #      'new_item_text': request.POST.get('item_text',''),
   # })
def home_page(request):
#    item = Item()
#    item.text = request.POST.get('item_text', '')
#    item.save()
#
#    return render(request, 'home.html', {
#        'new_item_text': request.POST.get('item_text', ''),
#    })
#     if request.method == 'POST':
#        new_item_text = request.POST['item_text']  #1
#        Item.objects.create(text=new_item_text)  #2
#     else:
#        new_item_text = ''  #3
#
#     return render(request, 'home.html', {
#        'new_item_text': new_item_text,  #4
#     })

     if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

     items = Item.objects.all()
     return render(request, 'home.html', {'items': items})

