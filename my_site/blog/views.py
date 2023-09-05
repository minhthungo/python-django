from datetime import date
from django.shortcuts import render

all_post = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Maximilian",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Illum, praesentium, expedita aliquid qui id amet porro,
            at similique facilis fugit impedit ipsam blanditiis cupiditate corrupti veniam eos provident. Aliquam, soluta.
        
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Illum, praesentium, expedita aliquid qui id amet porro,
            at similique facilis fugit impedit ipsam blanditiis cupiditate corrupti veniam eos provident. Aliquam, soluta.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Illum, praesentium, expedita aliquid qui id amet porro,
            at similique facilis fugit impedit ipsam blanditiis cupiditate corrupti veniam eos provident. Aliquam, soluta.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Maximilian",
        "date": date(2021, 7, 21),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code?",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Illum, praesentium, expedita aliquid qui id amet porro,
            at similique facilis fugit impedit ipsam blanditiis cupiditate corrupti veniam eos provident. Aliquam, soluta.
        
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Illum, praesentium, expedita aliquid qui id amet porro,
            at similique facilis fugit impedit ipsam blanditiis cupiditate corrupti veniam eos provident. Aliquam, soluta.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Illum, praesentium, expedita aliquid qui id amet porro,
            at similique facilis fugit impedit ipsam blanditiis cupiditate corrupti veniam eos provident. Aliquam, soluta.
        """
    },
    {
        "slug": "into-the-world",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2021, 7, 21),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amout of inspiration",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Illum, praesentium, expedita aliquid qui id amet porro,
            at similique facilis fugit impedit ipsam blanditiis cupiditate corrupti veniam eos provident. Aliquam, soluta.
        
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Illum, praesentium, expedita aliquid qui id amet porro,
            at similique facilis fugit impedit ipsam blanditiis cupiditate corrupti veniam eos provident. Aliquam, soluta.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Illum, praesentium, expedita aliquid qui id amet porro,
            at similique facilis fugit impedit ipsam blanditiis cupiditate corrupti veniam eos provident. Aliquam, soluta.
        """
    },
]

def get_date(post):
    return post.get("date")

# Create your views here.
def starting_page(request):
    sorted_posts = sorted(all_post, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_post
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_post if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })