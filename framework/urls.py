from views import (post_list, post_detail,
                post_create, post_update, post_delete)

urlpatterns = [
    (r'^$', post_list),
    (r'[0-9]+/$', post_detail),
    (r'create/$', post_create),
    (r'[0-9]+/update/$', post_update),
    (r'[0-9]+/delete/$', post_delete)
]
