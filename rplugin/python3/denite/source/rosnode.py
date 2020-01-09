import typing

from denite.source.base import Base
from denite.util import Nvim, UserContext, Candidates
try:
    from rosnode import get_node_names, ROSNodeIOException
except ImportError:
    def get_node_names(foo):
        return []


class Source(Base):
    def __init__(self, vim: Nvim) -> None:
        super().__init__(vim)
        self.name = 'rosnode'
        self.kind = 'rosnode'

    def gather_candidates(self, context: UserContext) -> Candidates:
        try:
            nodes = get_node_names(context['args'][0] if len(context['args']) >= 1 else None)
            return [{'word': node} for node in nodes]
        except ROSNodeIOException:
            return [{'word': "CONNECTION_TO_ROSMASTER_REFUSED"}]
