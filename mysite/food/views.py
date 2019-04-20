import argparse
import io

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from google.cloud import vision
from google.cloud.vision import types
from urllib.parse import unquote

# Create your views here.
def index(request):
    """This function handles the response and requests for when
    a user enters the URL of an image of food
    """
    meta = request.__dict__.get('META')
    query_string = meta.get('QUERY_STRING')
    if request.method == 'GET' and len(query_string) is not 0:
        print(reverse('results'), type(reverse('results')))
        return redirect(reverse('results') + 'search?%s' % query_string)
    return render(request, 'food/index.html')

def results(request, input_value):
    print(input_value)
    print('IN RESULTS', request.__dict__)
    if input_value == 'search':
        query = request.__dict__.get('META').get('QUERY_STRING')
        query = unquote(query)
        query_list = query.split('&')
        query_dict = {}
        for i in range(len(query_list)):
            single_query = query_list[i].split('=')
            query_dict[single_query[0]] = single_query[1]
         
        food_image_name = report(annotate(query_dict.get('image-url')))
        print(food_image_name)
        html_dict = {'food': food_image_name}
        return render(request, 'food/results.html', {'food_image': food_image_name})
    return render(request, 'food/results.html')

def report(annotations):
    """Returns name associated with food image"""
    if annotations.web_entities:
        return annotations.web_entities[0].description

def annotate(path):
    """Returns web annotations given the path to an image.
    This function was taken from Google Cloud's Web API tutorial
    https://cloud.google.com/vision/docs/internet-detection
    """
    client = vision.ImageAnnotatorClient()

    if path.startswith('http') or path.startswith('gs:'):
        image = types.Image()
        image.source.image_uri = path

    else:
        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

    web_detection = client.web_detection(image=image).web_detection

    return web_detection
