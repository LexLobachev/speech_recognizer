import logging
from decouple import config
from google.cloud import dialogflow
import json


def create_intent(project_id, display_name, training_phrases_parts, message_text):
    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)
    message_text = [message_text]
    text = dialogflow.Intent.Message.Text(text=message_text)
    message = dialogflow.Intent.Message(text=text)
    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )

    logging.info("Intent created: {}".format(response))


def main():
    project_id = config("PROJECT_ID")
    with open("questions.json", "r", encoding='UTF-8') as file:
        intents = json.loads(file.read())
    for display_name, training_phrases in intents.items():
        create_intent(project_id, display_name, training_phrases['questions'], training_phrases['answer'])


if __name__ == '__main__':
    main()
