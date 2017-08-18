#!/usr/bin/env python3

from bunq.sdk import context
from bunq.sdk.model import generated


api_context = context.ApiContext.restore()
users = generated.User.list(api_context)

for user in users:
    print(user.to_json())
