#!/usr/bin/env python2.7
import config
from endomondo import MobileApi


endomondo = MobileApi(email=config.endomondo_email,
                      password=config.endomondo_password)

print(endomondo.get_auth_token()) 

