import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name="inline")
def inline(text):
    pattern = r'\{\{(\d+)\}\}'

    def replace_match(match):
        question_id = match.group(1)
        ret  = '<input type="text" name="question_{question_id}" class="inline-input border-b-2 border-gray-400 bg-gray-50 text-center w-32 focus:outline-none focus:border-blue-600" autocomplete="off">'
        return ret

    processed_text = re.sub(pattern, replace_match, text)
    return mark_safe(processed_text)



@register.filter(name="radios")
def radios(text, arg):
    pattern = r'\{\{(.+?)\}\}'

    def replace_text(match):
        question_text = match.group(1)
        ret = f'''
            <div class="form-check">
              <input class="form-check-input" type="radio" name="{arg}" id="{question_text}">
              <label class="form-check-label" for="{question_text}">{question_text}</label>
            </div>
            '''
        return ret
    
    processed = re.sub(pattern, replace_text, text)
    return mark_safe(processed)
