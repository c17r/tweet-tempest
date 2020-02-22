from django.conf import settings

from social_django.models import UserSocialAuth
import twitter


__all__ = [
    'Twit'
]


class Twit:
    def __init__(self, user):
        info = UserSocialAuth.get_social_auth_for_user(user, provider='twitter').first()
        assert info is not None

        user_token = info.access_token['oauth_token']
        user_secret = info.access_token['oauth_token_secret']
        app_token = settings.SOCIAL_AUTH_TWITTER_KEY
        app_secret = settings.SOCIAL_AUTH_TWITTER_SECRET

        self.twit = twitter.Twitter(
            auth=twitter.OAuth(
                user_token,
                user_secret,
                app_token,
                app_secret
            )
        )

    def _get_user_info(self):
        if not hasattr(self, '_user_info'):
            self._user_info = self.twit.account.verify_credentials()

    def _get_configuration(self):
        if not hasattr(self, '_configuration'):
            self._configuration = self.twit.help.configuration()

    @property
    def profile_image_url(self):
        self._get_user_info()
        return self._user_info['profile_image_url']

    @property
    def screen_name(self):
        self._get_user_info()
        return self._user_info['screen_name']

    @property
    def characters_reserved_per_media(self):
        self._get_configuration()
        return self._configuration['characters_reserved_per_media']

    def send_bulk_tweets(self, tweets):
        rv = []
        previous_id = None

        for tweet in tweets:
            params = {
                'status': tweet['text'],
                'trim_user': 1
            }

            if previous_id:
                params['in_reply_to_status_id'] = previous_id

            try:
                data = self.twit.statuses.update(**params)
                tweet.update(success=True, error=None, id=data['id_str'])
                rv.append(tweet)
                previous_id = tweet['id']
            except Exception as e:
                tweet.update(success=False, error=str(e))
                rv.append(tweet)
                return rv

        return rv
