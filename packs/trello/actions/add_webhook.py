from lib import action

class AddWebhookAction(action.BaseAction):
    def run(self, callback_url=None, id_model=None, description=None, active=False, api_key=None, token=None):
        if api_key:
            self._set_creds(api_key=api_key, token=token)

        hook = self._client().create_hook(callback_url, id_model, description, token)

        if hook:
            return hook.id
        else:
            return (False, 'Failed to create webook')