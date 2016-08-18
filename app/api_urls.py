from django.conf.urls import url, include

from . import rest_form_views
from . import rest_retrieve_views

urlpatterns = [
    url(r'^edit/user_profile/(?P<pk>\d+)/$',
        rest_form_views.UserProfileUpdateFormView.as_view()),
    url(r'^create/question/$',
        rest_form_views.QuestionCreateFormView.as_view()),
    url(r'^edit/question/(?P<pk>\d+)/$',
        rest_form_views.QuestionUpdateFormView.as_view()),
    url(r'^create/wanted/$',
        rest_form_views.WantedCreateFormView.as_view()),
    url(r'^edit/wanted/(?P<pk>\d+)/$',
        rest_form_views.WantedUpdateFormView.as_view()),
    url(r'^create/available/$',
        rest_form_views.AvailableCreateFormView.as_view()),
    url(r'^edit/available/(?P<pk>\d+)/$',
        rest_form_views.AvailableUpdateFormView.as_view()),
    url(r'^create/story/$',
        rest_form_views.StoryCreateFormView.as_view()),
    url(r'^edit/story/(?P<pk>\d+)/$',
        rest_form_views.StoryUpdateFormView.as_view()),
    url(r'^create/event/$',
        rest_form_views.EventCreateFormView.as_view()),
    url(r'^edit/event/(?P<pk>\d+)/$',
        rest_form_views.EventUpdateFormView.as_view()),
    url(r'^create/project/$',
        rest_form_views.ProjectCreateFormView.as_view()),
    url(r'^edit/project/(?P<pk>\d+)/$',
        rest_form_views.ProjectUpdateFormView.as_view()),
    url(r'^create/comment/$',
        rest_form_views.CommentCreateFormView.as_view()),
    url(r'^edit/comment/(?P<pk>\d+)/$',
        rest_form_views.CommentUpdateFormView.as_view()),
    url(r'^delete/comment/(?P<pk>\d+)/$',
        rest_form_views.CommentDeleteView.as_view()),
    url(r'^create/answer/$',
        rest_form_views.AnswerCreateFormView.as_view()),
    url(r'^edit/answer/(?P<pk>\d+)/$',
        rest_form_views.AnswerUpdateFormView.as_view()),
    url(r'^delete/answer/(?P<pk>\d+)/$',
        rest_form_views.AnswerDeleteView.as_view()),
    url(r'^delete/story/(?P<pk>\d+)/$',
        rest_form_views.StoryDeleteView.as_view()),
    url(r'^delete/question/(?P<pk>\d+)/$',
        rest_form_views.QuestionDeleteView.as_view()),
    url(r'^delete/available/(?P<pk>\d+)/$',
        rest_form_views.AvailableDeleteView.as_view()),
    url(r'^delete/wanted/(?P<pk>\d+)/$',
        rest_form_views.WantedDeleteView.as_view()),
    url(r'^list/wanted/$',
        rest_retrieve_views.WantedListView.as_view()),
    url(r'^detail/wanted/(?P<pk>\d+)/$',
        rest_retrieve_views.WantedDetailView.as_view()),
    url(r'^list/wanted/$',
        rest_retrieve_views.WantedListView.as_view()),
    url(r'^detail/wanted/(?P<pk>\d+)/$',
        rest_retrieve_views.WantedDetailView.as_view()),
    url(r'^list/story/$',
        rest_retrieve_views.StoryListView.as_view()),
    url(r'^detail/story/(?P<pk>\d+)/$',
        rest_retrieve_views.StoryDetailView.as_view()),
    url(r'^list/available/$',
        rest_retrieve_views.AvailableListView.as_view()),
    url(r'^detail/available/(?P<pk>\d+)/$',
        rest_retrieve_views.AvailableDetailView.as_view()),
    url(r'^list/question/$',
        rest_retrieve_views.QuestionListView.as_view()),
    url(r'^detail/question/(?P<pk>\d+)/$',
        rest_retrieve_views.QuestionDetailView.as_view()),
    url(r'^list/project/$',
        rest_retrieve_views.ProjectListView.as_view()),
    url(r'^detail/project/(?P<pk>\d+)/$',
        rest_retrieve_views.ProjectDetailView.as_view()),
    url(r'^list/event/$',
        rest_retrieve_views.EventListView.as_view()),
    url(r'^detail/event/(?P<pk>\d+)/$',
        rest_retrieve_views.EventDetailView.as_view()),
    url(r'^list/comment/$',
        rest_retrieve_views.CommentListView.as_view()),
    url(r'^list/answer/$',
        rest_retrieve_views.AnswerListView.as_view()),
    url(r'^detail/user_profile/(?P<pk>\d+)/$',
        rest_retrieve_views.UserProfileDetailView),
]
