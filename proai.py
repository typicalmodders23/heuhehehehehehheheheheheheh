import tkinter as tk
import requests

# Create the root window
root = tk.Tk()

root.geometry("1600x1200")

completions = "completions"

# Set the API endpoint and your API key
endpoint = f"https://api.openai.com/v1/models/{completions}"
api_key = "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"

# Define a function to handle the API request
def handle_request():
    # Get the input text from the user
    input_text = input_field.get()
    import requests
    url = "https://api.openai.com/v1/completions"
    key = "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"
    headers = {"Authorization": f"Bearer {key}"}
    data = {
        'model': 'text-davinci-002',
        'prompt': input_text,
        'temperature': 0.7,
        'max_tokens': 200,}
    x = requests.post(url, headers=headers, json=data).json()
    # Make the API request to OpenAI
    # response = requests.post(
    #     endpoint,
    #     headers={"Content-Type": "text/plain", "Authorization": f"Bearer {api_key}"},
    #     data=input_text
    # )
    print(x)
    # Get the response text from the API
    response_text = x["choices"][0]["text"]
    print(response_text)
    label.config(text=response_text)

    # Set the response text to the label
    #response_label.config(text=response_text)

# Create the input field and response label
input_field = tk.Entry(root,width=100,)
response_label = tk.Label(root)
temperature=tk.Entry()
# Create the submit button
submit_button = tk.Button(root, text="Submit", command=handle_request)

# Place the input field and response label on the window
input_field.pack()
response_label.pack()

# Place the submit button on the window
submit_button.pack()


# Create a scrollable frame
frame = tk.Frame(root)
frame.pack()
canvas = tk.Canvas(frame)
canvas.pack(side=tk.LEFT)

# Add a scrollbar to the frame
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

# Bind the frame to the scrollbar's scroll command
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

# Create a label and add it to the frame
label = tk.Label(canvas, text="")
label.pack()

# Start the main event loop
root.mainloop()
