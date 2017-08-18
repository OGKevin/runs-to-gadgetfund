#!/usr/bin/env python3

import os
import config
from bunq.sdk import context
from bunq.sdk.json import converter

ctx = context.ApiContext(
    context.ApiEnvironmentType.PRODUCTION,
    config.bunq_key,
    config.bunq_device_name
)

ctx.save()
ctx_restored = context.ApiContext.restore()
print('Is original context equal the one saved and restored?:',
        converter.class_to_json(ctx) == converter.class_to_json(ctx_restored))
