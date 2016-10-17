from lib import action


class ViewWebhooksAction(action.BaseAction):
    def run(self, api_key=None, token=None):
        if api_key:
            self._set_creds(api_key=api_key, token=token)

        hooks = {}
        for hook in self._client().list_hooks(token):
            hooks[hook.id] = {
                'description': hook.desc,
                'id_model': hook.id_model,
                'callback_url': hook.callback_url,
                'active': hook.active
            }

        return hooks
