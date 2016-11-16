"""cookbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from crispy_forms import layout
from crispy_forms.helper import FormHelper
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login
from django.urls import reverse_lazy
from django.utils.translation import string_concat
from django.utils.translation import ugettext_lazy as _

from bulletin_board.views import BulletinView
from movies.views import movie_list

login_helper = FormHelper()
login_helper.form_action = reverse_lazy("login_page")
login_helper.form_method = "POST"
login_helper.form_class = "form-signin"
login_helper.html5_required = True
login_helper.layout = layout.Layout(
    layout.HTML(string_concat("""<h2 class="form-signin-heading">""", _("Please Sign In"), """</h2>""")),
    layout.Field("username", placeholder=_("username")),
    layout.Field("password", placeholder=_("password")),
    layout.HTML("""<input type="hidden" name="next" value="{{ next }}" />"""),
    layout.Submit("submit", _("Login"), css_class="btn-lg")
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'login/$', login, {"extra_context": {"login_helper": login_helper}}, name="login_page"),
    url(r'^quotes/', include("quotes.urls")),
    url(r'^movie-list/$', movie_list, name="movie-list"),
    url(r'^movie-list-cbv/$', include('movies.urls')),
    url(r'^$', BulletinView.as_view(), name="home"),
]
