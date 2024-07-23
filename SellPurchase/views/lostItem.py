from django.shortcuts import render,redirect
from SellPurchase.models.student import Student

def lostItem(request):
    return render(request, 'lostItems.html')



def addLostItem(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        information_about_item = request.POST.get('information_about_item')
        if request.FILES:
            lost_item=request.FILES['lostItem']
       
        student = Student(item_name=item_name, information_about_item=information_about_item, lostItem=lost_item)
        student.save()

    # Retrieve all items from the model
    all_items = Student.objects.all()
    return render(request,'addLostItem.html')
  


def searchItem(request):
      all_items = Student.objects.all()
      print(all_items)
      return render(request, 'searchItem.html', {'all_items': all_items})
