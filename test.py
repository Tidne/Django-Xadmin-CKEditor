a = '''
'''
b = '''

'''
import os
path = r'F:\python\blogEditTest\CkeditorTest\static\css'
file = os.listdir(path)
for i in file:
    str = '''{% load staticfiles %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="{% static '/css/''' +i +'''' %}">
</head>
<body>
       {% autoescape off %}{{ blog.title }}{% endautoescape %}
        <br/>
        <br/>
        {% autoescape off %}{{ blog.content }}{% endautoescape %}
        <script src="{% static '/js/highlight.pack.js' %}"></script>
        <script>hljs.initHighlightingOnLoad();</script>
</body>
</html>'''
    name = i[:-4]
    print(name)
    newpath = r"F:\python\blogEditTest\CkeditorTest\templates\app\\"
    with open(newpath+name+".html","w") as f:
        f.write(str)

