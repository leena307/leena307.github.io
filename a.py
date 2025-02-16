import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "gpt2"  ## my own try
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def get_response(question, max_tokens):
  
    inputs = tokenizer.encode(f"Python coding question: {question}\nAnswer:", return_tensors="pt")
    outputs = model.generate(inputs, max_length=max_tokens + inputs.shape[1], pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    response = response.split("Answer:")[-1].strip()
    return response


st.title('Python Coding Assistance')
user_question = st.text_area("Ask your Python coding question here:", placeholder="E.g., How do I open a file in Python?", height=150)
max_tokens = st.slider("Select the response length (max tokens):", min_value=50, max_value=500, value=150)
if st.button("Get Answer"):
    if user_question:
        result = get_response(user_question, max_tokens)
        st.text_area("Answer", result, height=300)
    else:
        st.error("Please enter a question.") # main func have not implemented for testing
