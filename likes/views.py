import json

from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt

from likes.models import Like
from likes.templatetags.likes_tags import get_likes_count


@never_cache
@csrf_exempt
def json_set_like(request, content_type_id, object_id):
    """
    Sets the object as favorite for the current user
    :param request:
    :param content_type_id:
    :param object_id:
    :return:
    """
    result = {
        "success": False,
    }
    if request.user.is_authenticated() and request.method == "POST":
        content_type = ContentType.objects.get(id=content_type_id)
        obj = content_type.get_object_for_this_type(pk=object_id)
        like, is_created = Like.objects.get_or_create(
            content_type=ContentType.objects.get_for_model(obj),
            object_id=obj.pk,
            user=request.user
        )

        if not is_created:
            like.delete()
        result = {
            "success": True,
            "content_type_id": content_type_id,
            "object_id": object_id,
            "action": is_created and "added" or "removed",
            "count": get_likes_count(obj),
        }

    json_str = json.dumps(result, ensure_ascii=False).encode("utf-8")
    return HttpResponse(json_str, mimetype="application/json; charset=utf-8")
