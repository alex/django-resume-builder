from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from people.models import Person

def resume(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render_to_response('resume.html', {'person': person}, context_instance=RequestContext(request))
