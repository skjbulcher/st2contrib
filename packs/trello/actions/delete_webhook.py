from lib import action
from pprint import pprint

class DeleteWebhookAction(action.BaseAction):
    def run(self, webhook_id, api_key=None, token=None):
        if api_key:
            self._set_creds(api_key=api_key, token=token)

        hooks = []
        hooks = self._client().list_hooks(token)

        if hooks:
            for hook in hooks:
                if hook.id == webhook_id:
                    hook.delete()
                    return (True, "")
        else:
            return (False, "Trello did not return any hooks")

        return (False, "hook id {} does not exist".format(webhook_id))