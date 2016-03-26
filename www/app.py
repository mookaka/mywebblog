#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'mookaka'

import logging
import asyncio
from aiohttp import web


logging.basicConfig(level=logging.INFO)


def index(request):
    return web.Response(body=b'<h1>Awesome!</h1>')


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    svr = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('we have run the tiny web server successfully!')
    return svr

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()