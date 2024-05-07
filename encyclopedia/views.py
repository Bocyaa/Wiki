import markdown2
import random
from django.http import HttpResponse
from django.shortcuts import render, redirect

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    # Use the get_entry function to retrieve the entry content
    entry_content = util.get_entry(title)

    if entry_content is None:
        return redirect('encyclopedia:message', message="The requested page was not found.")

    # Convert Markdown to HTML
    html_content = markdown2.markdown(entry_content)

    return render(request, "encyclopedia/entry.html", {
        "html_content": html_content,
        "title": title
    })


def search(request):
    # Retrieve the query from the GET request
    query = request.GET.get('q', '')

    # Retrieve all entry names
    entries = util.list_entries()

    results = []
    
    if query:
        # Check for an exact match
        for entry in entries:
            if query.lower() == entry.lower():
                return redirect('encyclopedia:info', title=entry)
            
        # If no exact match, find entries that contain the query as a substring
        results = [entry for entry in entries if query.lower() in entry.lower()]

    return render(request, "encyclopedia/search.html", {
        "query": query, 
        "results": results
    })


def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        if util.get_entry(title) is not None:
            return redirect('encyclopedia:message', message="An entry with this title already exists.")
        
        util.save_entry(title, content)
        return redirect('encyclopedia:info', title=title)
    
    return render(request, "encyclopedia/create.html")


def edit(request, title):
    if request.method == 'POST':
        # Save changes
        content = request.POST['content']
        util.save_entry(title, content)
        return redirect('encyclopedia:info', title=title)
    
    content = util.get_entry(title)

    if content is None:
        return redirect('encyclopedia:message', message="The requested page was not found.")
    
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": content
    })


def random_page(request):
    entries = util.list_entries()
    if not entries:
        return redirect('encyclopedia:message', message="No entries available.")
    title = random.choice(entries)
    return redirect('encyclopedia:info', title=title)

def message(request, message):
    return render(request, "encyclopedia/message.html", {
        "message": message
    })