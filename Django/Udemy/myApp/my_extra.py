from django import template


register=template.Library()
@register.filter(name="cutt")
def cutt(value,args):
    return value.replace(args,"")

# register.filter("cutt",cutt)