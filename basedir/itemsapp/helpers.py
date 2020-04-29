# Helper functions:

def grouped(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i+n]


# in views:

# from app.helpers import grouped

# def foo(request):
#     context['object_list'] = grouped(Bar.objects.all(), 4)
#     return render_to_response('index.html', context)

# in template:

# {% for group in object_list %}
#    <ul>
#         {% for object in group %}
#             <li>{{ object }}</li>
#         {% endfor %}
#    </ul>
# {% endfor %}
