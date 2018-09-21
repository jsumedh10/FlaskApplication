with open(r'PythonFiles/LinkedLists.py', 'r') as pycode:
    code = pycode.read()

html_code = '''<html><body><code>'''+code+'''</code></body></html>'''
newHTMLFile = pycode.name.split('/')[1].split('.')[0] + '.html'

with open(r'templates/'+newHTMLFile, 'w') as html_file:
    html_file.write(html_code)