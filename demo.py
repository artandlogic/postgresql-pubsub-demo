#!/usr/bin/env python3

# stdlib imports
import asyncio
import json
import os
import sys

# venv imports
try:
   # ensure asyncpg is available
   import asyncpg
except ImportError:
   print('You need to install asyncpg as outlined in the tutorial')
   sys.exit(1)


# ensure environment variables are set.
if None in (
   os.environ.get('PGHOST'),
   os.environ.get('PGPORT'),
   os.environ.get('PGUSER'),
   os.environ.get('PGPASSWORD'),
):
   print('You need to set PG* environment variables as outlined in the tutorial')
   sys.exit(1)


def _pg_notify(conn, pid, channel, notification):
   """Callback for notifications"""
   # prove we can load our JSON
   data = json.loads(notification)
   # Here, we just print to stdout, but you can imagine looking up cached
   # websockets based on channel and sending the notification to
   # subscribers.
   print(f'RECEIVED notification from {conn}[pid: {pid}] on channel {channel}:')
   print(json.dumps(data, indent=4))
   print('-' * 78)


async def main():
   """Entrypoint.  Connect to PG and add listener"""
   try:
      # establish connection.  By not providing an URN, this will use
      # PG* environment variables.
      conn = await asyncpg.connect()
      # test schema assumptions
      await conn.execute('SELECT COUNT(*) FROM appuser')

      # add listener, i.e., "LISTEN broadcast;"
      await conn.add_listener('broadcast', _pg_notify)
      # NOTE SHOWN: `conn.remove_listener()`, e.g., "UNLISTEN broadcast;"
   except Exception as exc:
      print('Exception connecting to expected database and schema:', exc)
      return

   print('Main task Waiting for notifications...')

   # we simulate a server waiting on requests by entering an async sleep.
   await asyncio.sleep(3600)


if __name__ == '__main__':
   try:
      print('Type Ctrl-c to exit')
      asyncio.run(main())
   except KeyboardInterrupt:
      pass

   print('Exiting')
