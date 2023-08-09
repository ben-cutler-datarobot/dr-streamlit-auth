import streamlit as st
import os
import streamlit_google_oauth as oauth
from datarobot_streamlit import streamlit_app

client_id = os.getenv('clientid')
client_secret = os.getenv('clientsecret')
external_url = os.getenv('DR_CUSTOM_APP_EXTERNAL_URL', 'https://foo.bar@0.0.0.0:8080')


if __name__ == "__main__":
    redirect_uri = 'https://' + external_url.split('@')[1]

    app_name = '''
    DataRobot Streamlit Google Authentication Demo
    '''
    app_desc = '''
    Demo of DataRobot Streamlit which has a Google login page
    '''
    login_info = oauth.login(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        app_name=app_name,
        app_desc=app_desc,
        logout_button_text="Logout",
    )
    if login_info:
        user_id, user_email = login_info
        streamlit_app.main()