from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import BoxForm, InventoryItemForm
from .models import Box, InventoryItem


def dashboard(request):
    query = request.GET.get('q', '').strip()
    boxes = Box.objects.prefetch_related('items')
    if query:
        boxes = boxes.filter(Q(box_number__icontains=query) | Q(items__description__icontains=query)).distinct()
    return render(request, 'inventory/dashboard.html', {
        'boxes': boxes,
        'query': query,
        'box_count': Box.objects.count(),
        'item_count': InventoryItem.objects.count(),
    })


def add_box(request):
    form = BoxForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        box = form.save()
        messages.success(request, f'Box {box.box_number} was created.')
        return redirect('box_detail', pk=box.pk)
    return render(request, 'inventory/form.html', {'form': form, 'title': 'Add a box', 'cancel_url': 'dashboard'})


def box_detail(request, pk):
    box = get_object_or_404(Box, pk=pk)
    form = InventoryItemForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        item = form.save(commit=False)
        item.box = box
        item.save()
        messages.success(request, 'Item added to the box.')
        return redirect('box_detail', pk=box.pk)
    return render(request, 'inventory/box_detail.html', {'box': box, 'form': form})


def edit_item(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    form = InventoryItemForm(request.POST or None, instance=item)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Item description updated.')
        return redirect('box_detail', pk=item.box.pk)
    return render(request, 'inventory/form.html', {'form': form, 'title': 'Edit item', 'cancel_url': 'box_detail', 'cancel_pk': item.box.pk})


def delete_item(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    box_pk = item.box.pk
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Item deleted.')
    return redirect('box_detail', pk=box_pk)


def delete_box(request, pk):
    box = get_object_or_404(Box, pk=pk)
    if request.method == 'POST':
        number = box.box_number
        box.delete()
        messages.success(request, f'Box {number} and its items were deleted.')
        return redirect('dashboard')
    return render(request, 'inventory/confirm_delete.html', {'object_name': f'Box {box.box_number}', 'cancel_url': 'box_detail', 'cancel_pk': box.pk})


def reports(request):
    boxes = Box.objects.prefetch_related('items')
    return render(request, 'inventory/reports.html', {'boxes': boxes})


def box_report(request, pk):
    box = get_object_or_404(Box.objects.prefetch_related('items'), pk=pk)
    return render(request, 'inventory/box_report.html', {'box': box})
