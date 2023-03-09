import openai
import readchar 

openai.api_key = "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"

keep_going = True
while keep_going:
  text_to_correct = input("Enter an animal: ")
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"query: {text_to_correct}",
    temperature=0,
    max_tokens=200,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )

  print(response["choices"][0]["text"])
  print()

  print("Press y to continue, n to quit")
  keep_going= readchar.readkey() == "y"