import openai
def openaiDoc(changes_in_file):
    openai.api_key = ""
    prompt = ""
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
        )
    generated_documentation = response.choices[0].text.strip()

    print("generated openai Document - {}".format(generated_documentation))
    return generated_documentation



import re

def extract_req_id_defect_id(commit_message):
    pattern = r'\b(Req \d+|Defect \d+)\b'
    matches = re.findall(pattern, commit_message)
    return matches