# RandTalkBot Bot matching you with a random person on Telegram.
# Copyright (C) 2016 quasiyoke
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging
from .stranger_sender import StrangerSender

class StrangerSenderServiceError(Exception):
    pass

class StrangerSenderService:
    _instance = None

    def __init__(self, bot):
        self._bot = bot
        self._stranger_senders = {}

    @classmethod
    def get_instance(cls, bot=None):
        if cls._instance is None:
            if bot is None:
                raise StrangerSenderServiceError(
                    'Instance wasn\'t initialized. Provide arguments to construct one.',
                    )
            else:
                cls._instance = cls(bot)
        return cls._instance

    def get_or_create_stranger_sender(self, telegram_id):
        try:
            return self._stranger_senders[telegram_id]
        except KeyError:
            stranger_sender = StrangerSender(self._bot, telegram_id)
            self._stranger_senders[telegram_id] = stranger_sender
            return stranger_sender