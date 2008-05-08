from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog', {'packages': ('mailinglist',),}),
)

urlpatterns += patterns('mailinglist.admin_views',
    (r'^json/message/(.+)/subscribers/$', 'json_subscribers'),
    (r'^message/(.+)/preview/$', 'message_preview'),
    (r'^message/(.+)/submit/$', 'message_submit'),
    (r'^message/(.+)/preview/html/$', 'html_preview'),
    (r'^message/(.+)/preview/text/$', 'text_preview'),
    (r'^submission/(.+)/submit/$', 'submit'),
)
