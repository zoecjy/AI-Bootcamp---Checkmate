import streamlit as st
from PIL import Image

def app():
  # Page Title
  st.title("📋 Methodology")

  # Using tabs for different sections
  tab1, tab2, tab3, tab4, tab5 = st.tabs(
      ["Problem Statement", "Overall Flow",
       "Prompt Refinement", "User Testing", "Possible Applications"])

  with tab1:
      st.subheader("Step 1: Problem Statement 🤕")
      st.write(
          """
          Currently the Short Answer Feedback Assistant in Student Learning Space is only able to compare semantic similarity between a suggested answer/ set of rubrics and provide summative feedback (in teacher comments). This hinders students' learning progress as they may not get detailed feedback at the point at which the mistake occurred, making it challenging for them to understand and correct their errors effectively.
        
          **Proposed Solution:**


          1. Error Detection: Use LLM to scan the text and detect errors from a student response.
          2. Error Categorisation: From a prescribed list of error tags and descriptions, LLM tags errors in students' responses. The prescribed list of errors can be subject-specific.
          3. Feedback Generation: After categorising errors, the LLM provides actionable feedback to help the student understand why the error occurred and offers suggestions for improvement.
        
          """
      )




  with tab2:
      st.subheader("Step 2: Overall Flow 🔁")
     
      st.markdown("[Click here to view full resolution image](https://drive.google.com/file/d/17EpS_DMgEEL8BcZfrWcawDBJQrtK0USu/view?usp=drive_link)")
      st.image("images/flow.png", use_column_width=True)
      st.write(
          """
           **Teacher Settings**
          
           1. Teacher uploads a .csv file containing error tags and their description for the LLM to pick it out. 
           2. The file is saved as a dictionary (*errors_dict*) and formatted to a string (*formatted_errors_list*).


           **Student Response**


           3. Student enters their response to the question in the text input box and Checkmate! The text is saved as *student_text*.
           4. The LLM prompt now begins to work its magic by combining *formatted_errors_list* and *student_text* to return a dictionary contatining the phrase which contains and error, the error tag and feedback.
           5. Checkmate gives feedback through highlighting the text and numbering the annotations in the main *student_text* and on the right column.


          """
      )


  with tab3:
      st.subheader("Step 3: Prompt Refinement ✍🏻")
      st.write(
          """
          Using Google Colab, we first crafted a basic prompt that took in a list of error tags, and created an output which highlighted the phrase containing the error tag, the error tag, and feedback for the student.
         
          Our subsequent iterations were as follows:
         
          **Refinement #1: Experimenting with RAG**
          
         We tried experimenting using an RAG on a database of error tags which included examples of the error, non examples and also contextutal variations. However, we found that it did not improve the feedback provided and the experience was better when the errors were sent within the prompt itself.
          
          **Refinement #2: Refining the Prompt Sent to LLM**
         
         We adjusted our prompt to ensure it returned a list of dictionaries with three key-value pairs corresponding to the error tag, the phrase containing error and the feedback. We also ensured that when no errors are found, an empty list was returned. To refine it further, we tweaked the prompt to also allow phrases to be returned instead of whole sentences, making the feedback more targeted. Finally, we experimented with the strictness of error detection to reduce instances of non-errors being flagged. This was also important so that students do not feel overwhelmed by the suggestions or false positives.
         
          **Refinement #3: Refining Error Tags**

        We used ChatGPT to refine the error tags to be mutually exclusive so that the errors picked up were less likely to overlap in the types of errors. This also made the error detection more accurate.





          """
      )




  with tab4:
      st.subheader("Step 4: User Testing 🧪")
      st.write(
          """
          We tested with 5 teachers to get a sense of how our prototype fits their needs.
          """
      )


      st.write(
          """
          **Feedback from our user testing:**
         
          "*This is impressive, didn't think that this will be possible.*"


          "*A bit too complicated with where to store the error tags and don't need to input questions.*"


          "*This will be useful for even categorising customer feedback at a customer helpdesk.*"


          "*The feedback is useful and accurate for English and it's accurate though the error tag title can be better.*"


          \n
          **Changes made after user testing:**
         
          1. We removed the question input to reduce complexity as this was not being sent to the LLM.
          2. We simplified the error adding process to an upload only function and provided samples for users to try Checkmate.
          3. We revised our error tags so that they are mutually exclusive, which makes the error tagging more accurate.

          """
      )

      st.image("images/usertest.png", use_column_width=True)

  with tab5:
      st.subheader("Step 5: Possible Applications 🛠️")
      st.write(
          """
          Checkmate can also be applied across a wide range of industries by adjusting the prompt and error tags.
          - Analyse customer feedback: Highlight issues and suggest areas of improvement.
          - Auditing records: Highlight inconsistencies or missing information and suggest corrections.
          - Code review: Highlight problematic errors of code and suggest areas of improvement.

          """
      )

# To run the app
if __name__ == "__main__":
 
  app()















