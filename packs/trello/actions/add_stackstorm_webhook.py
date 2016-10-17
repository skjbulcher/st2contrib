from lib import action

class AddStackStormWebhookAction(action.BaseAction):
    def run(self, st2_domain=None, st2_url=None, st2_api_key=None, id_model=None, description=None, active=False, api_key=None, token=None):
        if api_key:
            self._set_creds(api_key=api_key, token=token)

        if not st2_domain:
            st2_domain = self.config['st2_domain']
        if not st2_domain:
            raise ValueError('[AddStackStormWebhookAction]: "st2_domain" config value is required')

        if not st2_api_key:
            st2_api_key = self.config['st2_api_key']
        if not st2_api_key:
            raise ValueError('[AddStackStormWebhookAction]: "st2_api_key" config value is required')

        callback_url = "https://{}/api/v1/webhooks/{}?st2-api-key={}".format(st2_domain, st2_url, st2_api_key)

        hook = self._client().create_hook(callback_url, id_model, description, token)

        if hook:
            return hook.id
        else:
            return (False, 'Failed to create webook')