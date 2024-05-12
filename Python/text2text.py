import openai

def generate_business_plan(description):
    openai.api_key = 'sk-proj-gyZEl33ElA6XqtDPEbDMT3BlbkFJtIQcpeElYHxohzNuXeGz'

    # Ensure the prompt is correctly formatted
    prompt = f"""Based on the following business idea, develop a comprehensive business plan covering the startup phase, growth stage, plateau, and exit strategy:

    {description}

    1. Startup Phase: Key activities, initial funding, team building, and market entry strategy.
    2. Growth Stage: Expansion strategies, scaling operations, and diversification.
    3. Plateau: Sustaining operations, maintaining market share, and optimizing costs.
    4. Exit Strategy: Preparing for acquisition, public offering, or other exit strategies.
    """

    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=1000,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text.strip()

# Example usage
description = input("Please describe your business idea: ")
plan = generate_business_plan(description)
print("Generated Business Plan:\n", plan)

