from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, GenerationConfig
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, GenerationConfig
import os

# Specify the paths to the model and tokenizer directories
# Use raw strings (prefix paths with 'r') to properly handle backslashes in Windows file paths
model_dir = r"E:\Projects\HCAI NLP PROJ\nlp_proj\app\pegasus-samsum-model"
tokenizer_dir = r"E:\Projects\HCAI NLP PROJ\nlp_proj\app\tokenizer"
# model_dir = "app/pegasus-samsum-model"
# tokenizer_dir = "app/tokenizer"

# Remove leading or trailing whitespace (though it should not be necessary with your provided paths)
model_dir = model_dir.strip()
tokenizer_dir = tokenizer_dir.strip()

# Load the tokenizer from the local directory
tokenizer = AutoTokenizer.from_pretrained(tokenizer_dir)

# Load the model from the local directory
model = AutoModelForSeq2SeqLM.from_pretrained(model_dir)

# Load generation configuration if necessary (optional, if you want custom settings)
generation_config = GenerationConfig.from_pretrained(model_dir)


def summarize_text(input_text):
    """
    Summarizes the input text using the loaded model and tokenizer.

    Parameters:
    input_text (str): The input text to be summarized.

    Returns:
    str: The summarized text.
    """
    # Tokenize the input text
    inputs = tokenizer(input_text, return_tensors="pt", truncation=True, padding="max_length", max_length=1024)

    # Generate the summary
    summary_ids = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=350,  # You can adjust the max_length as needed
        min_length=100,  # You can adjust the min_length as needed
        length_penalty=0.8,
        num_beams=4,  # You can adjust the num_beams as needed
    )

    # Decode the summary
    summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    clean_summary = summary_text.replace("<n>", "")
    return clean_summary
