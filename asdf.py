import openai
def openaiDoc(changes_in_file):
    openai.api_key = ""
    prompt = "Please provide a short summary of the functionality introduced by these changes.\n Check and report whether the committed function/changes include comments. If comments are present but not understandable, indicate 'Given comment not understandable; please correct it'. If comments are not present, inform the developer to add comments.\n" + str(changes_in_file)
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