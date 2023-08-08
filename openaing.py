import openai
from config import key, location, endpoint
openai.api_type = "azure"
openai.api_key = key
openai.api_base = endpoint
deployment_id_gpt4='gpt4'
deployment_id_gpt35='gpt35'
deployment_id_text_davinci='gta'
openai.api_key = key

def create_prompt(context,query):
    header = "Answer the question as truthfully as possible \
        using the provided context, and if the answer is not contained \
within the text and requires some latest information to be updated, \
    print 'Sorry Not Sufficient context to answer query' \n"
    return header + context + "\n\n" + query + "\n"


def generate_answer(conversation,deployment_plan):
    openai.api_version = "2023-03-15-preview"
    response = openai.ChatCompletion.create(
    engine=deployment_id_gpt4,
    messages=conversation,
    temperature=0,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop = [' END']
    )
    return (response['choices'][0]['message']['content']).strip()

def generate_answer_davinci(prompt):
    openai.api_version = "2022-12-01"
    response = openai.Completion.create(
    engine=deployment_id_text_davinci,
    prompt=prompt,
    temperature=0,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop = [' END']
    )
    return (response['choices'][0].text).strip()


def generate_answer_from_context(user_input, context,deployment_plan):
    conversation=[{"role": "system", "content": "Assistant is a large language model \
                   trained by OpenAI."}]
    prompt = create_prompt(context,user_input)            
    conversation.append({"role": "assistant", "content": prompt})
    conversation.append({"role": "user", "content": user_input})

    if deployment_plan=='GPT-3.5':
        deployment_plan_=deployment_id_gpt35
        reply = generate_answer(conversation,deployment_plan_)
    elif deployment_plan=='GPT-4':
        deployment_plan_=deployment_id_gpt4
        reply = generate_answer(conversation,deployment_plan_)
    else:
        reply = generate_answer_davinci(prompt)
    return reply