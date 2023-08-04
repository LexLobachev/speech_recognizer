from decouple import config


def detect_intent_texts(project_id, session_id, text, language_code, is_fallback=True):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""
    from google.cloud import dialogflow

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print("Session path: {}\n".format(session))

    # for text in texts:
    text_input = dialogflow.TextInput(text=text, language_code=language_code)

    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )
    if response.query_result.intent.is_fallback and is_fallback is False:
        return None

    return response.query_result.fulfillment_text


if __name__ == '__main__':
    project_id = config("PROJECT_ID")
    session_id = config("YOUR_TELEGRAM_ID")
    detect_intent_texts(project_id, session_id, input(), 'ru-Ru')
