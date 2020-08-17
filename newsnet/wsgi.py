"""
WSGI config for newsnet project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
from pathlib import Path
runner__path = Path(__file__).resolve(strict=True).parent.__str__()
print(runner__path)


import os


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsnet.settings')

application = get_wsgi_application()

# import asyncio
# from runner import run
# new_loop = asyncio.new_event_loop()
# print(new_loop.is_running())
# # loop = asyncio.get_event_loop()
# asyncio.set_event_loop(new_loop)
# new_loop.run_until_complete(run())
# # new_loop.run_forever(run())
# new_loop.is_running()

