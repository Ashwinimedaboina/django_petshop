from django import template
from datetime import datetime


register=template.Library()
def printDate():
    return datetime.now().strftime("%d-%m-%Y")

register.filter("PrintDate",printDate)



#this is cart item total amount function

@register.filter(name="multiply")
def multiply(v1,v2):
    return v1*v2