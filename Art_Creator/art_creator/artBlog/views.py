from django.shortcuts import render
from django.http import HttpResponseNotFound
from datetime import date

all_posts = [
    {
        "slug": "Oil-Pastel-Art",
        "image": "oilpastel.jpg",
        "date": date(2021, 3, 21),
        "title": "Oil Pastel",
        "summary": "Never knew using oil pastel can be so much fun.",
        "content": """
        An oil pastel is a painting and drawing medium formed into a stick which consists of pigment mixed with a binder mixture of non-drying oil and wax, in contrast to other pastel sticks which are made with a gum or methyl cellulose binder, and in contrast to wax crayons which are made without oil. The surface of an oil pastel painting is less powdery than one made from gum pastels, but more difficult to protect with a fixative.
        """
    },
    {
        "slug": "One-Line-Drawing",
        "image": "oneline.jpg",
        "date": date(2020, 4, 24),
        "title": "One Line Drawing Art",
        "summary": "This is such a fun and easy, simple art.",
        "content": """
        A one line drawing, also known as a single line drawing, is a drawing made with just one line. For most artists it is a way to simplify the complex world around us. Yet there are many different kinds out there, with each artist having their own specific charisteristics. The main differences I found are:
Simple versus complex
Smooth versus rough
Sharp corners versus curved corners
Analog versus digital
One thickness versus a variation of thin and thick areas
With or without filled areas
With or without color
Open or closed
Focussed on a theme such as animals, full body illustrations, portraits or erotics

       """
    },
    {
        "slug": "Stippling-Art",
        "image": "point.jpg",
        "date": date(2021, 3, 28),
        "title": "Stippling Art",
        "summary": "This is also called as Pointillism.",
        "content": """
        Stippling is the creation of a pattern simulating varying degrees of solidity or shading by using small dots. Such a pattern may occur in nature and these effects are frequently emulated by artists. In a drawing or painting, the dots are made of pigment of a single colour, applied with a pen or brush; the denser the dots, the darker the apparent shade—or lighter, if the pigment is lighter than the surface.
        """
    },
    {
        "slug": "Stone-Paint",
        "image": "stoneart.jpg",
        "date": date(2021, 6, 30),
        "title": "Stone Painting",
        "summary": "Paint on things you see around.",
        "content": """
        Stone Painting is very much connected with history. In ancient times, people used to paint on stones, caves and rock and have left their identity in the same way.
        """
    },
    {
        "slug": "Acrylic-Art",
        "image": "acrylic.jpg",
        "date": date(2021, 7, 30),
        "title": "Acrylic Painting",
        "summary": "Paint Paint Paint and make this world around you colorful.",
        "content": """
        Acrylic paint is a fast-drying paint made of pigment suspended in acrylic polymer emulsion and plasticizers, silicon oils, defoamers, stabilizers, or metal soaps. Most acrylic paints are water-based, but become water-resistant when dry. Depending on how much the paint is diluted with water, or modified with acrylic gels, mediums, or pastes, the finished acrylic painting can resemble a watercolor, a gouache, or an oil painting, or have its own unique characteristics not attainable with other media.
        """
    }
]


def get_date(post):
    return post['date']

def index_page(request):
    sorted_post = sorted(all_posts, key=get_date)
    latest_posts = sorted_post[-3:]
    return render(request, "artBlog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "artBlog/all_posts.html", {
        "posts": all_posts
    })

def post_detail(request, post_slug):
    selected_post = next((post for post in all_posts if post['slug'] == post_slug), False)
    if selected_post:
        return render(request, "artBlog/post_detail.html", {
            "post": selected_post
        })
    else:
        return HttpResponseNotFound("Post Not Found")