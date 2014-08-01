import django.forms as forms
from string import Template
from django.utils.safestring import mark_safe

class ColourChooserWidget(forms.TextInput):
  def render(self, name, value, attrs=None):
    tpl = Template(u"""<h1>There would be a colour widget here, for value $colour</h1>""")
    return mark_safe(tpl.substitute(colour=value))