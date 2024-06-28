# Actual API key
OPENAI_API_KEY = "your_openai_api_key_here"

# Function to extract the response content
def get_response_content(response_dict, exclude_tokens=None):
    if exclude_tokens is None:
        exclude_tokens = []
    if response_dict and response_dict.get("choices") and len(response_dict["choices"]) > 0:
        content = response_dict["choices"][0]["message"]["content"].strip()
        if content:
            for token in exclude_tokens:
                content = content.replace(token, '')
            return content
    raise ValueError(f"Unable to resolve response: {response_dict}")

# Asynchronous function to send a request to the OpenAI chat API
async def send_openai_chat_request(prompt, model_name, temperature=0.0):
    openai.api_key = OPENAI_API_KEY
    message = {"role": "user", "content": prompt}
    response = await openai.ChatCompletion.acreate(
        model=model_name,
        messages=[message],
        temperature=temperature,
    )
    return get_response_content(response)

# Example usage
async def main():
    prompt = "Hello!"
    model_name = "gpt-4o"
    response = await send_openai_chat_request(prompt, model_name)
    print(response)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
async def send_plugin_request(plugin_name, prompt):
    # Send request to plugin
    response = await openai.PluginRequest.acreate(
        plugin_name=plugin_name,
        prompt=prompt,
    )
    # Extract image data from response
    image_data = response.get("image_data")
    return image_data

# Example usage
async def main():
    prompt = "Generate an image of a cat"
    plugin_name = "image_generator_plugin"
    image_data = await send_plugin_request(plugin_name, prompt)
    # Use image data to interact with end-user
    print(image_data)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())