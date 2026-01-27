import re
from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter(name="render_gap_fill")
def render_gap_fill(text):

    pattern = r'\{\{(\d+)\}\}'


    def replace_match(match):
        question_id = match.group(1)

        ret  = '<input type="text" name="question_{question_id}" class="inline-input border-b-2 border-gray-400 bg-gray-50 text-center w-32 focus:outline-none focus:border-blue-600" autocomplete="off">'
        return ret

    processed_text = re.sub(pattern, replace_match, text)

    return mark_safe(processed_text)


@register.filter(name="capy")
def capy(text):
    return "dance"