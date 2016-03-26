#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
It is just used to test the database,orm,models
'''

import orm
import asyncio
import sys
from models import User, Blog, Comment


async def test(loop):
    await orm.create_pool(loop, user='www-data', password='www-data', db='awesome')
    for n in range(10):
        u = User(name='wwfwwfww' + str(n), email= str(n) + 'rere@example.com', passwd='844290678', image='funk you')
        await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
if loop.is_closed():
    sys.exit(0)
