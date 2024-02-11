from django.shortcuts import render, redirect
from markdown2 import Markdown
from . import util
from django import forms
import random

def convert_md_to_html(title):
  content = util.get_entry(title)
  markdowner = Markdown()
  if content == None:
     return None
  else:
     return markdowner.convert(content)
  

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
   html_content = convert_md_to_html(title)
   if html_content == None:
      return render(request, "encyclopedia/error.html", {
         "message": "This entry does not exist"
      })
   else:
      return render(request, "encyclopedia/entry.html", {
         "title": title, 
         "content": html_content
      })
  
def search(request):
    if request.method == "POST":
        if 'q' in request.POST:
            entry_search = request.POST['q']
            entry_content = util.get_entry(entry_search)
            if entry_content is not None:
                return redirect('entry', title=entry_search)
            allEntries = util.list_entries()
            recommendation = [entry for entry in allEntries if entry_search.lower() in entry.lower()]
            if not recommendation:
                return render(request, "encyclopedia/error.html", {
                   "message": "No entry found :("
                })                
            return render(request, "encyclopedia/search.html", {
                "recommendation": recommendation,
                "query": entry_search,
            })


def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        titleExist = util.get_entry(title.lower().strip())
        if titleExist is not None:
            return render(request, "encyclopedia/error.html", {
                "message": "Entry page already exists"
            })
        elif not bool(title.strip()):
            return render(request, "encyclopedia/error.html", {  #TODO: check if is required in the project
                "message": "Title is required"
            })
        else:
            util.save_entry(title, content)
            html_content = convert_md_to_html(title) 
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": html_content
            })
        
def edit_page(request):
    if request.method == 'POST':
        title = request.POST['entry_title']
        content =util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
         "title": title,
         "content": content   
       })
    
def save_edit(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = convert_md_to_html(title)
        return render(request, "encyclopedia/entry.html", {
         "title": title,
         "content": html_content   
       })
    
def rand(request):
    allEntries = util.list_entries()
    rand_entry = random.choice(allEntries)
    html_content = convert_md_to_html(rand_entry)
    return render(request, "encyclopedia/entry.html", {
        "title": rand_entry,
        "content": html_content
    })
