import streamlit as st
import openai


# Function to create final prompt with error list & student text
def create_prompt(errors_dict, student_input):
 # Convert error_list into a formatted string
 formatted_error_list = '\n'.join([f'"{key}": "{value}"' for key, value in errors_dict.items()])
 prompt = f"""
 You are a diligent teacher identifying errors in students' responses to give them feedback.
 Your objectives are:


 1. Use the provided list of error tags and descriptions to create an example sentence for each error tag. Include these examples in your assessment.
 2. Carefully analyze the student's response, using the updated list of error tags and the examples you created.
 3. Identify and return any errors found in the student response.


 Here is the error list for your reference:
 {formatted_error_list}


 Give your response in the format below.
 Return a dictionary with three keys:
 1. "phrase containing error" - the specific part of the sentence containing an error.
 2. "error tag" - a concise error category based on formatted_error_list
 3. "feedback" - a concise student-friendly explanation or suggestion


Example response:
 [
 {{
     "phrase containing error": "phrase",
     "error tag": "error tag",
     "feedback": "feedback for student"
 }},
 {{
     "phrase containing error": "phrase",
     "error tag": "error tag",
     "feedback": "feedback for student"
 }},
 ]
  Read the response carefully and understand the surrounding context to avoid raising false errors. For more than 1 error, make sure you list all errors in the list in the order they appear in the student input.
  If there are no errors, respond with an empty list [].

 Student response: {student_input}"""
 return prompt




openai.api_key = st.secrets["api"]["key"]
def get_completion(prompt, model="gpt-4o-mini", temperature=0):
 messages = [{"role": "user", "content": prompt}]
 response = openai.chat.completions.create( #originally was openai.chat.completions
     model=model,
     messages=messages,
     temperature=temperature,
 )
 return response.choices[0].message.content


