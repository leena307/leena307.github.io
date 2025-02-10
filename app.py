# import streamlit as st
# import openai

# # Set your OpenAI API key here
# openai.api_key = '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'

# def get_response(code, temperature, frequency):
#     try:
#         response = openai.Completion.create(
#             engine="gpt-4o-mini",  # Choose the appropriate engine
#             prompt=code,
#             temperature=temperature,
#             max_tokens=int(frequency)  # Adjusting frequency as max_tokens for simplicity
#         )
#         return response.choices[0].text.strip()
#     except Exception as e:
#         return str(e)

# # Streamlit UI
# st.title('Gen AI Python Coding App')

# with st.form("my_form"):
#     user_code = st.text_area("Enter your Python code here:", height=300)
#     temperature = st.slider("Select the temperature:", min_value=0.0, max_value=1.0, step=0.01, value=0.5)
#     frequency = st.slider("Select the max tokens (frequency):", min_value=50, max_value=500, value=100)
#     submitted = st.form_submit_button("Submit")

# if submitted:
#     result = get_response(user_code, temperature, frequency)
#     st.text_area("Output:", result, height=300)



    print("Cognito:", bot_response)

