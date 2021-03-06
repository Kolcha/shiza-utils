# -*- coding: utf-8 -*-

import requests


def login(email, passw):
    login_url = "http://shiza-project.com/accounts/login"

    session = requests.session()

    result = session.get(login_url)
    if result.status_code != 200:
        return None

    result = session.post(
        login_url,
        data={"field-email": email, "field-password": passw}
    )
    if result.status_code != 200:
        return None

    return session


def logout(session):
    session.post("http://shiza-project.com/accounts/logout")
    session.close()
