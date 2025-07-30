from django.shortcuts import render, reverse
from . import markdown_html
from . import util
from django.http import HttpResponseRedirect
from django import forms
import random


class NewPageForm(forms.Form):
    title = forms.CharField(
        label="Title", 
        max_length=100, 
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the title of your page"
        })
    )
    content = forms.CharField(
        label="Content",
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 20,
            "placeholder": "Enter Markdown content here..."
        })
    )


class EditPageForm(forms.Form):
    content = forms.CharField(
        label="Content",
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 20,
            "placeholder": "Edit Markdown content here..."
        })
    )


def index(request):
    # Home Page, displays all available entries
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    # Displays the requested entry
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "title": title
        })
    else:
        html = markdown_html.simple_markdown_to_html(content)
        return render(request, "encyclopedia/entry.html", {
            "content": html,
            "title": title
        })


def search(request):
    #Loads requested title page if it exists, else displays search results
    query = request.GET.get("q", "").strip()
    entries = util.list_entries()

    if not query:
        return HttpResponseRedirect(reverse("index"))

    for entry in entries:
        if query.lower() == entry.lower():
            return HttpResponseRedirect(reverse("entry", args=[entry]))
    
    results = []
    for entry in entries:
        if query.lower() in entry.lower():
            results.append(entry)
    return render(request, "encyclopedia/search.html", {
        "results": results,
        "query": query
    })


def new_page(request):
    #Lets users create a new page on the wiki
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if util.get_entry(title):
                form.add_error("title", "An entry with this title already exists.")
            else: 
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse("entry", args=[title]))
    else:
        form = NewPageForm()

    return render(request, "encyclopedia/new_page.html", {
        "form": form
    })


def edit(request, title):
    #Lets users edit an existing page on the wiki
    if request.method == "POST":
        form = EditPageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("entry", args=[title]))
    else:
        content = util.get_entry(title)
        form = EditPageForm(initial={"content": content})

    return render(request, "encyclopedia/edit.html", {
        "form": form,
        "title": title
    })


def random_page(request):
    #Loads a random page from the wiki
    entries = util.list_entries()
    if entries:
        title = random.choice(entries)
        return HttpResponseRedirect(reverse("entry", args=[title]))
