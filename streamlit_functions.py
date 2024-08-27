#! - WorklistQuery

import requests
import streamlit_constants as ru
import pandas as pd
import streamlit as st


report_url = 'https://clario.usradiology.com/rpc/app.php?app=analyse&sysClient='
login_url  = 'https://clario.usradiology.com/rpc/app.php?app=login&sysClient='
worklist_url = 'https://clario.usradiology.com/rpc/app.php?app=workflow&sysClient='

def run_test():
    login_header  = ru.loginHeaders()
    login_payload = ru.loginValidate()
    login_response = requests.post(login_url, 
                            headers=login_header,
                            json   =login_payload)
    session_id = login_response.cookies._cookies['clario.usradiology.com']['/']['SESSION-SWL'].value
    user_id    = login_response.json()[0]['result']['loginID']
    #response_json = response.json()

    report_header   = ru.reportHeaders(session_id)
    report_payload  = ru.worklistQuery(user_id, '2024-08-01', '2024-08-27')
    report_response = requests.post(worklist_url, 
                            headers=report_header,
                            json   =report_payload)
    response_json = report_response.json()

    df = pd.DataFrame(response_json)['result'][0]
    stats = df['title']
    df = pd.DataFrame(df['data'])
    df = df[ru.worklist_columns()]
    df_summary = df[['modality','group','accession']]
    gdf = df_summary.groupby(['modality','group']).count().reset_index()
    return st.dataframe(gdf,hide_index=True,height=600)