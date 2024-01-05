import spacy
from spacy import displacy
from IPython.display import display
import html2text

text = """
Albert Einstein was a German-born theoretical physicist, widely
acknowledged to be one of the greatest and most influential physicists of all
time.
Einstein is best known for developing the theory of relativity, but he also
made important contributions to the development of the theory of quantum
mechanics.
Einstein was born in the German Empire, but moved to Switzerland in 1895,
forsaking his German citizenship (as a subject of the Kingdom of
Württemberg) the following year.
In 1897, at the age of 17, he enrolled in the mathematics and physics teaching
diploma program at the Swiss Federal polytechnic school in Zürich,
graduating in 1900
"""
def html_to_text(html_string):
    # Create an HTML to text converter
    converter = html2text.HTML2Text()

    # Convert HTML to plain text
    text_result = converter.handle(html_string)

    return text_result

def get_entities_html(text, ner_result, title=None):
    ents = []
    for ent in ner_result:
        e = {}
        e["start"] = ent["start"]
        e["end"] = ent["end"]
        e["label"] = ent["entity"]
        if ents and -1 <= ent["start"] - ents[-1]["end"] <= 1 and ents[-1]["label"] == e["label"]:
            ents[-1]["end"] = e["end"]
        ents.append(e)
    render_data = [{"text": text, "ents": ents, "title": title,}]
    html_string = displacy.render(render_data, style="ent", manual=True, jupyter=False)

    # Convert HTML to text
    if html_string:
        text_result = html_to_text(html_string)
        print(text_result)
    else:
        print("No HTML content to convert.")
