from lib import action


class CloseBoardAction(action.BaseAction):
    def run(self, board_id, api_key=None, token=None):
        if api_key:
            self._set_creds(api_key=api_key, token=token)

        board = self._client().get_board(board_id)
        board.close()

        if board.closed:
            return board.closed
        else:
            return (False, "Failed to close board")
