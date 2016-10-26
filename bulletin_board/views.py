# Create your views here.
from django.views.generic import FormView

from bulletin_board.forms import BulletinForm


class BulletinView(FormView):
    form_class = BulletinForm
    template_name = "bulletin_board/change_form.html"
