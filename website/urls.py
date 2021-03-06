from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'website'
urlpatterns = [
    #path('', views.index, name='index'),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^view_profile/$', views.view_profile, name='view_profile'),
    re_path(r'^proposal/$', views.proposal, name='proposal'),
    #path('login', views.login, name='login'),
    #path('accounts/', include('django.contrib.auth.urls')),
    #re_path(r'^', include('django.contrib.auth.urls')),
    #path('proposal/view', views.view_abstracts, name='view_abstracts'),
    #path('proposal/submitcfp', views.submitcfp, name='submitcfp'),
    #path('accounts/register', views.userregister, name='userregister'),
    re_path(r'^workshops/$', views.workshops, name='workshops'),
    re_path(r'^dwsimquiz/$', views.dwsimquiz, name='dwsimquiz'),
    re_path(r'^jobfair/$', views.jobfair, name='jobfair'),
    re_path(r'^cfp/$', views.cfp, name='cfp'),
    #re_path(r'^quiz/$', views.quiz_view, name='quiz_view'),
    re_path(r'^question_list/$', views.question_list, name='question_list'),
    re_path(r'^view_solutions/$', views.view_solutions, name='view_solutions'),
    re_path(r'^add_questions/$', views.add_questions, name='add_questions'),
    re_path(r'^edit_question/(?P<qid>\d+)$', views.edit_question, name='edit_question'),
    re_path(r'^take_quiz/$', views.take_quiz, name='take_quiz'),
    re_path(r'^quiz_intro/$', views.quiz_intro, name='quiz_intro'),
    re_path(r'^leaderboard/$', views.leaderboard, name='leaderboard'),
    re_path(r'^submit-cfp/$', views.submitcfp, name='submitcfp'),
    re_path(r'^submit-cfw/$', views.submitcfw, name='submitcfw'),
    #url(r'^submit-cfp/$', 'website.views.cfp', name='home'),
    #url(r'^submit-cfw/$', 'website.views.home', name='home'),
    re_path(r'^accounts/register/$', views.user_register, name='user_register'),
    re_path(r'^accounts/login/$', views.user_login, name='user_login'),
    re_path(r'^gallery/$', views.gallery, name='gallery'),
    # url(r'^view-abstracts/$', 'website.views.view_abstracts', name='view_abstracts'),
    re_path(r'^view-abstracts/$', views.view_abstracts, name='view_abstracts'),
    re_path(r'^abstract-details/(?P<proposal_id>\d+)$',
            views.abstract_details, name='abstract_details'),
    re_path(r'^edit-proposal/(?P<proposal_id>\d+)$',
            views.edit_proposal, name='edit_proposal'),
    re_path(r'^view-abstracts/status_change/$',
            views.status_change, name='status_change'),
    re_path(r'^comment-abstract/(?P<proposal_id>\d+)$',
            views.comment_abstract, name='comment_abstract'),
    re_path(r'^comment-abstract/status/(?P<proposal_id>\d+)$',
            views.status, name='status'),
    re_path(r'^comment-abstract/rate/(?P<proposal_id>\d+)$',
            views.rate_proposal, name='rate_proposal'),
    re_path(r'^process-contact-form/(?P<next_url>\d+)',
            views.contact_us, name='contact_us'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
