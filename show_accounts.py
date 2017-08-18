#!/usr/bin/env python3
import config

from bunq.sdk import context
from bunq.sdk.model import generated


api_context = context.ApiContext.restore()
accounts = generated.MonetaryAccount.list(api_context, config.bunq_user_id)

for account in accounts:
    print(account.to_json())
