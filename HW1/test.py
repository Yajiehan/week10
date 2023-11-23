import openai
response = openai.Completion.create(
    model="curie:ft-personal-2023-11-22-20-09-46",
    prompt="When do I need to start my air conditioner?"
    # additional parameters
    # temperature,
    # frequency_penalty,
    # presence_penalty
    # ..etc
)

print(response.choices[0].text)