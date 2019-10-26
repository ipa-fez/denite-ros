import typing

from denite.kind.base import Base
from denite.util import Nvim, UserContext, debug


class Kind(Base):
    def __init__(self, vim: Nvim) -> None:
        super().__init__(vim)

        self.name = 'ros'
        self.default_action = 'rosed'

    def action_rosed(self, context: UserContext) -> None:
        # Create a file/rec for each selected package
        context['sources_queue'].append([{'name': 'file/rec', 'args': [x['ros_pkg_path']]}
                                         for x in context['targets']])
