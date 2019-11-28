import typing

from denite.source.base import Base
from denite.util import Nvim, UserContext, Candidates
import rosnode


class Source(Base):
    def __init__(self, vim: Nvim) -> None:
        super().__init__(vim)
        self.name = 'rosnode'
        self.kind = 'rosnode'

    def gather_candidates(self, context: UserContext) -> Candidates:
        nodes = rosnode.get_node_names(context['args'][0] if len(context['args']) >= 1 else None)
        return [{'word': node} for node in nodes]
