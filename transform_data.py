import json

# Load the data from the json file
with open("training_examples.json", "r") as f:
    profiles = json.load(f)

# Output file to save the formatted messages
with open("mydata.jsonl", "w") as out_file:
    for profile in profiles:
        profile_details = json.dumps(profile)

        # Create the desired format
        formatted_message = {
            "messages": [
                {
                    "role": "system",
                    "content": "As a response, provide the following fields in a JSON dict: name, handle, age, hobbies, email, bio, location, is_blue_badge, joined, gender, appearance, avatar_prompt, and banner_prompt.",
                },
                {
                    "role": "user",
                    "content": "Generate details of a random Twitter profile.",
                },
                {"role": "assistant", "content": profile_details},
            ]
        }

        # Write the formatted message to the output file, each on a new line
        out_file.write(json.dumps(formatted_message) + "\n")
