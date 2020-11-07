import eel

eel.init('web', allowed_extensions=['.js', '.html'])
@eel.expose
def sey_hello_py(x):
    print('Hello form %s' %x)

sey_hello_py('Python World')
eel.say_hello_js('Python World!')

eel.start('html/index.html')
