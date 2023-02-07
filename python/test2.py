import os
import dialogflow
from google.api_core.exceptions import InvalidArgument
DIALOGFLOW_PROJECT_ID = 'small-talk-vpagjr'
DIALOGFLOW_LANGUAGE_CODE = 'ru'
GOOGLE_APPLICATION_CREDENTIALS = 'private_key.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "private_key.json"
SESSION_ID = 'current-user-id'
text_to_be_analyzed = "Привет"
session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
text_input = dialogflow.types.TextInput()
query_input = dialogflow.types.QueryInput()
try:
    response = session_client.detect_intent(session=session, query_input=query_input)
except InvalidArgument:
    raise
print("Query text:", response.query_result.query_text)
print("Detected intent:", response.query_result.intent.display_name)
print("Detected intent confidence:", response.query_result.intent_detection_confidence)
print("Fulfillment text:", response.query_result.fulfillment_text)
