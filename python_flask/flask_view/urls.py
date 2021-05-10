from app_run import app
from views import *

app.add_url_rule('/cases', view_func=get_case)
app.add_url_rule('/', view_func=index)
app.add_url_rule('/redir', view_func=redir_home)