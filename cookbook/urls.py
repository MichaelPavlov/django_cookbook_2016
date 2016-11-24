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
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login
from django.urls import reverse_lazy
from django.utils.translation import string_concat
from django.utils.translation import ugettext_lazy as _

from utils.views import render_js

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

# class CrispySearchView(SearchView):
#     def extra_context(self):
#         helper = FormHelper()
#         helper.form_tag = False
#         helper.disable_csrf = True
#         return {"search_helper": helper}


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'login/$', login, {"extra_context": {"login_helper": login_helper}}, name="login_page"),
    # url(r'^quotes/', include("quotes.urls")),
    # url(r'^cv/', include("cv.urls")),
    # url(r'^movie-list/$', movie_list, name="movie-list"),
    url(r'^movie-list-cbv/', include('movies.urls')),
    url(r'^locations/', include('locations.urls', namespace="locations")),
    # url(r'^bulettin$', BulletinView.as_view(), name="home"),
    # url(r'^$', BulletinView.as_view(), name="home"),
]

urlpatterns += i18n_patterns(
    # url(r'^search/$', CrispySearchView(), name='haystack_search')
    url(r'^js-settings/$', render_js, {"template_name": "settings.js"}, name='js-settings')
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)