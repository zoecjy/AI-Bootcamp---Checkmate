import streamlit as st
import json
import re
from helper_functions import create_prompt, get_completion


def highlight_phrases_in_text(full_text, annotations):
   highlighted_text = full_text
   # Sort annotations by their keys
   sorted_annotations = sorted(annotations.items())


   # Replace phrases with highlighted versions in one go
   for number, (phrase, _, _, _) in sorted_annotations:
       pattern = re.escape(phrase)
       replacement = f"<span style='background-color: #ADD8E6;'><strong>[{number}] {phrase}</strong></span>"
       highlighted_text = re.sub(pattern, replacement, highlighted_text, flags=re.IGNORECASE)


   return highlighted_text


def app():
   # Page Title
   st.title("✏️ Student: Responses")


   # Access errors_dict from session state
   errors_dict = st.session_state.get('errors_dict', {})
    # Access previous response from session state or set it as an empty string if not present
   if "student_response" not in st.session_state:
       st.session_state["student_response"] = ""


   if "used_annotations" not in st.session_state:
       st.session_state["used_annotations"] = {}


   if "feedback" not in st.session_state:
       st.session_state["feedback"] = ""


   # Display the question at the top
   st.subheader("Check your response here")


   # Create two columns for layout
   left_column, right_column = st.columns([2, 1])


   with left_column:
       # Display the student's response in a text area
       student_text = st.text_area("Answer", value=st.session_state["student_response"], height=200)


       # Button to send the student text to OpenAI
       if st.button("♟️ Checkmate"):
           if student_text:
               st.session_state["student_response"] = student_text


               # Create prompt for OpenAI
               prompt = create_prompt(errors_dict, student_text)


               # Get feedback from OpenAI
               response = get_completion(prompt)


               try:
                   if response.strip():
                       # Parse response safely
                       response_data = json.loads(response)


                       # Check if the response is a list or a dictionary
                       if isinstance(response_data, list):
                           # Handle response as a list
                           errors = response_data
                           feedback = ""  # Clear feedback if no specific feedback is provided
                       elif isinstance(response_data, dict):
                           # Handle response as a dictionary
                           feedback = response_data.get("feedback", "")
                           errors = response_data.get("errors", [])
                       else:
                           st.error("Unexpected response format.")
                           feedback = ""


                       # Update session state
                       st.session_state["feedback"] = feedback
                       used_annotations = {}
                    
                       # Prepare a list for ordered annotations
                       if errors:
                           annotation_counter = 1
                           for error in errors:
                               phrase = error.get("phrase containing error", "")
                               annotation_feedback = error.get("feedback", "")
                               error_tag = error.get("error tag", "No error tag provided")
                               if phrase.strip():
                                   used_annotations[annotation_counter] = (phrase, None, annotation_feedback, error_tag)
                                   annotation_counter += 1
                           st.session_state["used_annotations"] = used_annotations
                       else:
                           st.session_state["used_annotations"] = {}


                       # Display highlighted text based on annotations
                       highlighted_text = highlight_phrases_in_text(student_text, st.session_state["used_annotations"])


                       # Show disclaimer above highlighted text
                       if st.session_state["feedback"] or errors:
                           st.markdown("<div style='background-color: #FFFFE0; font-size: 14px; text-align: center; padding: 10px; border-radius: 5px;'><em> ✨ Checkmate uses generative AI and may be inaccurate at times. Please check the feedback given.✨</em></div>", unsafe_allow_html=True)


                           # Display feedback only if present
                           if st.session_state["feedback"]:
                               st.write(st.session_state["feedback"])


                       # Check if no errors were found
                       if not errors:
                           st.markdown("<div style='background-color: #CDEBC5; font-size: 14px; padding: 10px; border-radius: 5px; text-align: center;'><strong>No errors found ✅</strong></div>", unsafe_allow_html=True)


                       # Display the highlighted text
                       st.markdown(highlighted_text, unsafe_allow_html=True)
                   else:
                       st.error("Received an empty response from OpenAI.")


               except json.JSONDecodeError:
                   st.error("Error parsing response from OpenAI. The response may not be in a valid JSON format.")
               except Exception as e:
                   st.error("An error occurred while processing the response from OpenAI.")
                   st.error(f"Details: {str(e)}")
           else:
               st.warning("Please type your answer.")


   # Right column: display the feedback and annotations
   with right_column:
       st.markdown("### ♟️ Checkmate")


       # Display the annotations in order
       if st.session_state["used_annotations"]:
           sorted_annotations = sorted(st.session_state["used_annotations"].items())
           feedback_output = []


           for number, annotation in sorted_annotations:
               if len(annotation) == 4:  # Expecting 4 values
                   phrase, _, annotation_feedback, error_tag = annotation
                   formatted_feedback = f"[{number} - {error_tag}]<br> **{phrase}**<br>{annotation_feedback}<br><br>"
                   feedback_output.append(formatted_feedback)
               else:
                   st.error(f"Unexpected annotation format: {annotation}")


           st.markdown("".join(feedback_output), unsafe_allow_html=True)
       else:
           st.write("No annotations available.")





