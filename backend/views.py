import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from backend import utils


class HomepageView(TemplateView):
    template_name = 'backend/homepage.html'


class TwitterInfoView(LoginRequiredMixin, utils.JSONView):
    def get(self, request, *args, **kwargs):
        twitter = utils.Twit(self.request.user)
        rv = {
            'profile_image_url': twitter.profile_image_url,
            'screen_name': twitter.screen_name,
            'characters_reserved_per_media': twitter.characters_reserved_per_media,
        }
        return self.render_to_response(rv)


class SendTweetView(LoginRequiredMixin, utils.JSONView):
    def post(self, request, *args, **kwargs):
        if not request.body:
            raise Exception

        tweets = json.loads(request.body.decode('utf-8'))

        if not tweets:
            raise Exception

        twitter = utils.Twit(self.request.user)
        rv = twitter.send_bulk_tweets(tweets)

        return self.render_to_response(rv)
