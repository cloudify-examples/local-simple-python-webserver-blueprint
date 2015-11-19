import os
import signal

from cloudify import ctx

pid = ctx.instance.runtime_properties['pid']
try:
    os.kill(pid, signal.SIGTERM)
    ctx.logger.info('Python Webserver Terminated!')
except:
    ctx.logger.info('Webserver not running.')
