import cohere
from dotenv import load_dotenv
import os
load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))


def web_search(query, school_website, schoolname, language):
    print(query)
    msg = co.chat(
        model="command",
        chat_history=[
            {"role": "system", "message": f"You are a bot assisting parents with school information about {schoolname}. Base all  your responses from data gathered from the school's website- {school_website}. Ensure that all responses are in {language}."},
        ],
        message=query,
        connectors=[{"id": "web-search"}])

    return msg.text
