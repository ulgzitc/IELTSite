import re
from django import template
from django.utils.safestring import mark_safe
import json

register = template.Library()

"""Old version
#Inline
@register.filter(name="inline")
def inline(text):
    pattern = r'\{\{(\d+)\}\}'

    def rep_inline(match):
        question_id = match.group(1)
        ret  = f'<input type="text" name="question_{question_id}" placeholder={question_id} class="inline-input border-b-2 border-gray-400 bg-gray-50 text-center w-32 focus:outline-none focus:border-blue-600" autocomplete="off">'
        return ret

    processed_text = re.sub(pattern, rep_inline, text)
    return mark_safe(processed_text)
"""
#Inline
@register.filter(name="inline")
def inline(jdata):
    data = dict(jdata)
    text = data['text']
    #a = int(data['question_ids'][0])
    #b = int(data['question_ids'][1]) + 1
    #question_ids = range(a, b)

    pattern = r'\{\{(\d+)\}\}'

    def rep_inline(match):
        question_id = match.group(1)
        ret  = f'<input type="text" name="question_{question_id}" placeholder={question_id} class="inline-input border-b-2 border-gray-400 bg-gray-50 text-center w-32 focus:outline-none focus:border-blue-600" autocomplete="off">'
        return ret

    processed_text = re.sub(pattern, rep_inline, text)
    return mark_safe(processed_text)


##There was no old verion.
#Inline List
@register.filter(name="inline_list")
def inline_list(jdata):
    data = dict(jdata)
    lines = data['lines']
    #a = int(data['question_ids'][0])
    #b = int(data['question_ids'][1]) + 1
    #question_ids = range(a, b)
    processed_text = ""
    pattern = r'\{\{(\d+)\}\}'

    def rep_inline(match):
        question_id = match.group(1)
        ret  = f'<input type="text" name="question_{question_id}" placeholder={question_id} class="inline-input border-b-2 border-gray-400 bg-gray-50 text-center w-32 focus:outline-none focus:border-blue-600" autocomplete="off">'
        return ret

    for line in lines:
        processed_text += "- "
        processed_text += re.sub(pattern, rep_inline, line)
        processed_text += "<br><br>"

    return mark_safe(processed_text)


"""Old version
#Radios
@register.filter(name="radios")
def radios(text, arg):
    pattern = r'\{\{(.+?)\}\}'

    def rep_radios(match):
        question_text = match.group(1)
        ret = f'''
            <div class="form-check">
              <input class="form-check-input-radios" type="radio" name="{arg}" id="{question_text}">
              <label class="form-check-label-radios" for="{question_text}">{question_text}</label>
            </div>
            '''
        return ret
    
    processed = re.sub(pattern, rep_radios, text)
    return mark_safe(processed)
"""
#Radios
@register.filter(name="radios")
def radios(jdata):
    data = dict(jdata)
    headers = data['headers']
    a = int(data['question_ids'][0])
    b = int(data['question_ids'][1]) + 1
    question_ids = range(a, b)
    ret = ""

    for head in headers:
        options = data[head]
        ret += f"<h3>{head}</h3>"

        for idx, option in zip(question_ids, options):
            ret += f'''
                <div class="form-check">
                  <input class="form-check-input-radios" type="radio" name="{head}" id="{option}">
                  <label class="form-check-label-radios" for="{option}">{option}</label>
                </div>
                '''
    return mark_safe(ret)
    

"""Old version
#Inline Tab
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
"""
#Inline Tab
@register.filter(name="inline_tab")
def inline_tab(jdata):
    data = dict(jdata)
    left = data['left']
    right = data['right']
    #a = int(data['question_ids'][0])
    #b = int(data['question_ids'][1]) + 1
    #question_ids = range(a, b)
    ret = ""

    for l, r in zip(left, right):
        ret += f'<strong>{l}</strong> -'
        if r.isdigit() == True:
            ret += f'<input type="text" name="question_{r}" placeholder={r} class="inline-input border-b-2 border-gray-400 bg-gray-50 text-center w-32 focus:outline-none focus:border-blue-600" autocomplete="off">.<br><br>'
        else:
            ret += f'{r}<br><br>'

    return mark_safe(ret)



#Checkbox
@register.filter(name="checkbox")
def checkbox(text, arg):
    pattern = r'\{\{(.+?)\}\}'

    def rep_checkbox(match):
        question_text = match.group(1)
        ret = f'''
            <div class="form-check">
              <input class="form-check-input-checkbox" type="checkbox" name="{arg}" id="{question_text}">
              <label class="form-check-label-checkbox" for="{question_text}">{question_text}</label>
            </div>'''

        return ret
    
    processed = re.sub(pattern, rep_checkbox, text)
    return mark_safe(processed)


#Grid
@register.filter(name="grid")
def grid(jdata):
    data = dict(jdata)
    cols = data["cols"]
    rows = data["rows"]
    a = int(data['question_ids'][0])
    b = int(data['question_ids'][1]) + 1
    question_ids = range(a, b)

    def col_str(incols):
        columns_str = ""
        for col in incols:
            columns_str += f"<th>{col}</th>"
        return mark_safe(columns_str)

    def row_col_in(inrows, incols, inquestion_ids):
        rowshit = ""
        for inr, idx in zip(inrows, inquestion_ids):
            rowshit += "<tr>"
            row_first = f'<td>{idx}&nbsp;&nbsp;{inr}</td>'
            rowshit += row_first
            for inc in incols:
                col_list = f'<td><input type="radio" name="q{idx}" value="{inc}"></td>'
                rowshit += col_list
            rowshit += "</tr>"
        return mark_safe(rowshit)

    html = f'''
        <table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse;">
            <thead>
                <tr>
                    <th style="width: 260px;"></th>
                    {col_str(cols)}
                </tr>
            </thead>
            <tbody>
                {row_col_in(rows, cols, question_ids)}
            </tbody>
        </table>'''

    return mark_safe(html)


#Tabular
@register.filter(name="tabular")
def tabular(jdata):
    data = dict(jdata)
    cols = data["cols"]
    rows = data["rows"]
    content = data["content"]
    
    pattern = r'\{\{(\d+)\}\}'
    def rep_inline(match):
        question_id = match.group(1)
        ret  = f'<input type="text" name="question_{question_id}" placeholder={question_id} class="inline-input border-b-2 border-gray-400 bg-gray-50 text-center w-32 focus:outline-none focus:border-blue-600" autocomplete="off">'
        return ret

    def col_str(incols):
        columns_str = ""
        for col in incols:
            columns_str += f"<th>{col}</th>"
        return mark_safe(columns_str)


    def row_col_in(inrows, incontent):
        rowshit = ""
        for idx, inr in enumerate(inrows):
            rowshit += "<tr>"
            row_first = f'<td>{inr}</td>'
            rowshit += row_first
            for con in incontent[idx]:
                col_list = f'<td>{re.sub(pattern, rep_inline, con)}</td>'
                rowshit += col_list
            rowshit += "</tr>"
        return mark_safe(rowshit)

    html = f'''
        <table border="1" cellpadding="10" cellspacing="0" style="border-collapse: collapse; width: 100%;">
            <thead>
                <tr>
                    {col_str(cols)}
                </tr>
            </thead>
            <tbody>
                {row_col_in(rows, content)}
            </tbody>
        </table>'''

    return mark_safe(html)


#Assign
@register.filter(name='assign')
def assign(jdata):
    data = dict(jdata)
    tldr = data['tldr']
    option_char = data['option_char']
    option_lett = data['option_w']
    op = data['op']
    answers = data['answers']
    a = int(data['question_ids'][0])
    b = int(data['question_ids'][1]) + 1
    question_ids = range(a, b)

    def intldr(option_char, option_lett):
        ret = ""
        for char, lett in zip(option_char, option_lett):
            ret += f"<li><strong>{char}</strong>&nbsp;&nbsp;{lett}</li>"
        return ret


    def inop(answers):
        ret = ""
        for idx, asnwer in zip(question_ids, answers):
            ret += f'''
            <tr>
                <td>{asnwer}</td>
                <td>
                    <input placeholder="{idx}" type="text" name="q17" maxlength="1" size="1"
                           style="text-transform: uppercase; text-align: center;">
                </td>
            </tr>'''
        return ret


    html = f'''
        <form method="post">

            <div style="border: 2px solid #a855f7; border-radius: 10px; padding: 20px; margin-bottom: 30px;">
                <h3 style="text-align: center; color: #7e22ce; margin-top: 0;">
                    {tldr}
                </h3>

                <ul style="list-style: none; padding-left: 0; margin: 0;">
                    {intldr(option_char, option_lett)}
                </ul>
            </div>


            <h4 style="color: #7e22ce; margin-bottom: 10px;">{op}</h4>

            <table cellpadding="6" cellspacing="0">
                <tbody>
                    {inop(answers)}
                </tbody>
            </table>

        </form>
        '''
    return mark_safe(html)


@register.filter(name="draganddrop")
def draganddrop(jdata):
    data = dict(jdata)
    section1 = data['section1']
    section2 = data['section2']
    fields = data['fields']
    options = data['options']
    a = int(data['question_ids'][0])
    b = int(data['question_ids'][1]) + 1
    question_ids = range(a, b)

    def fieldy(fields):
        ret = ""
        for field in fields:
            ret += f'''
                <div class="trend" data-question="26">
                    <div class="trend-title">{field}</div>
                    <div class="dropzone"></div>
                </div>'''
        return ret

    def opit(options):
        ret = ""
        for option in options:
            ret += f'''
            <div class="opinion" draggable="true" data-value="A">
                {option}
            </div>'''
        return ret


    html = f'''
        <form method="post">
        <div class="container">

            <div>
                <h3>{section1}</h3>
                {fieldy(fields)}
            </div>

            <div>
                <h3>{section2}</h3>
                <div class="opinions" id="opinions-zone">
                    {opit(options)}
                </div>
            </div>

        </div>
        </form>
        '''

    return mark_safe(html)


