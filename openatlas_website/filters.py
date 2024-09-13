from openatlas_website import app

@app.template_filter()
def sanitize(string: str) -> str:
    return ''.join(i for i in string if i not in [' ', '(', ')'])
