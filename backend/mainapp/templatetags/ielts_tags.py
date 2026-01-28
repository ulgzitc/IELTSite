import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name="inline")
def inline(text):
    pattern = r'\{\{(\d+)\}\}'

    def rep_inline(match):
        question_id = match.group(1)
        ret  = '<input type="text" name="question_{question_id}" class="inline-input border-b-2 border-gray-400 bg-gray-50 text-center w-32 focus:outline-none focus:border-blue-600" autocomplete="off">'
        return ret

    processed_text = re.sub(pattern, rep_inline, text)
    return mark_safe(processed_text)



@register.filter(name="radios")
def radios(text, arg):
    pattern = r'\{\{(.+?)\}\}'

    def rep_radios(match):
        question_text = match.group(1)
        ret = f'''
            <div class="form-check">
              <input class="form-check-input" type="radio" name="{arg}" id="{question_text}">
              <label class="form-check-label" for="{question_text}">{question_text}</label>
            </div>
            '''
        return ret
    
    processed = re.sub(pattern, rep_radios, text)
    return mark_safe(processed)



@register.filter(name="inline_tab")
def inline_tab(text):
    pattern = r'\{\{(.+?)\}\}\s*\{\{(.+?)\}\}'

    def rep_inline_tab(match):
        idx1 = match.group(1)
        idx2 = match.group(2)

        if idx2 == "_":
            ret = f'''
                <strong>{idx1}</strong> - <input type="text" name="question_{idx1}" class="inline-input border-b-2 border-gray-400 bg-gray-50 text-center w-32 focus:outline-none focus:border-blue-600" autocomplete="off">.<br><br>
            '''
            return ret
        ret = f'<strong>{idx1}</strong> - {idx2}.<br><br>'
        return ret
    
    processed = re.sub(pattern, rep_inline_tab, text)
    return mark_safe(processed)