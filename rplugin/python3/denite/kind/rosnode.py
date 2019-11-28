import typing

from denite.kind.base import Base
from denite.util import Nvim, UserContext
import rosgraph
import rosnode
try:
    from xmlrpc.client import ServerProxy
except ImportError:
    from xmlrpclib import ServerProxy


class Kind(Base):
    def __init__(self, vim: Nvim) -> None:
        super().__init__(vim)

        self.name = 'rosnode'
        self.default_action = 'gdb'
        self._rosapi_caller_id = 'denite-ros'

    def _get_node_pid(self, node: str) -> int:
        master = rosgraph.Master(self._rosapi_caller_id)
        uri = rosnode.get_api_uri(master, node)
        node = ServerProxy(uri)
        pid = node.getPid(self._rosapi_caller_id)[-1]
        return pid

    def action_gdb(self, context: UserContext) -> None:
        pid = self._get_node_pid(context['targets'][0]['word'])
        self.vim.call('nvimgdb#Spawn', 'gdb', 'gdb_wrap.sh', 'gdb -q --pid {}'.format(pid))
