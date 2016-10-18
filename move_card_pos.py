from lib import action


class MoveCardAction(action.BaseAction):
    def run(self, card_id, target_pos, api_key=None, token=None):
        if api_key:
            self._set_creds(api_key=api_key, token=token)

        card = self._client().get_card(card_id)
        card.change_pos(target_pos)

        return card
