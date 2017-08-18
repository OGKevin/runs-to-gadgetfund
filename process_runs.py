#!/usr/bin/env python3

import sqlite3
import config

from bunq.sdk import context
from bunq.sdk.model import generated
from bunq.sdk.model.generated import object_

def make_payment(distance, multiplier):
    payment_amount = str(round(distance * multiplier, 2))
    payment_currency = 'EUR'
    counterparty_pointer_type = 'IBAN'
    counterparty_name = config.bunq_counterparty_name
    counterparty_iban = config.bunq_counterparty_iban

    payment_description = 'Because you ran {} km today!'.format(distance)
    user_item_id = config.bunq_user_id
    monetary_account_item_id = config.bunq_monetary_account
    api_context = context.ApiContext.restore(config.folder_path + 'bunq.conf')
    pointer = object_.Pointer(
        counterparty_pointer_type,
        counterparty_iban
    )
    pointer.name = counterparty_name
    request_map = {
        generated.Payment.FIELD_AMOUNT: object_.Amount(
            payment_amount,
            payment_currency
        ),
        generated.Payment.FIELD_COUNTERPARTY_ALIAS: pointer,
        generated.Payment.FIELD_DESCRIPTION: payment_description
    }

    generated.Payment.create(
        api_context,
        request_map,
        user_item_id,
        monetary_account_item_id
    )


ammount_per_km = 1
connection = sqlite3.connect(config.db_path)
cursor = connection.cursor()
cursor.execute("SELECT * FROM Runs WHERE processed < 1")
for row in cursor.fetchall():
    make_payment(row[2],ammount_per_km)
    connection.execute("UPDATE Runs set processed=1 WHERE id=?", [str(row[0])])

connection.commit()
connection.close()
