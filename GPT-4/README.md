## Experimenting with Chat GPT-4 on Entity Recognition Task

### The purpose of this exp. is to check how good GPT-4 is at the time of this experimentation (October 2023)

#### Steps to Reproducing the Experiment:
1) We took the original 13 diseases containing 90 documents from the Test folder (see "input/test/*").
2) Combined the contents of all these diseases into a single file (see "input/1.Test_Combined.json").
3) Used format_json.py script in order to take only the "text" field from the combined data ("input/2.Text_Only_Test.json")
4) Masked the Header portion (e.g., Causes, Symptoms, etc.) of the Test Data with ?'s so that the LLMs do not get any hint about the Topic of the Documents.
   - We used an exact number of characters consisting of '?' in order to mask the topic (see "input/3.Entity_Type_Masking.json").
   - The Masked Test data is used in order to get the prediction from the Chat GPT-4. (see "input/4.Masked_Text_Only_Test.json")
5) The prompts used to achieve this are provided in the file "Prompt.docx"
   - You have to put the prompt at the beginning of the chat.
6) Chat GPT is not good with calculating the span that we need as our desired JSON format in order to compare the results.
   - Thus, you have to use the "**Display_Predicted_Entities.ipynb**" each time manually with the output of the Chat GPT.
   - Simply put the text, entities, and entity_types each time into the above notebook and check if the output can be visualized or not.
   - The visualization part of the code will show errors/warnings if there are some problems in the output of ChatGPT.
7) Remember to check the ENTITY_TYPES often because Chat GPT has a certain context window, and it tends to forget the original Entity Types.
   - In this case, you have to re-open a new chat window and repeat from STEP-5.
8) Important Note: Since Chat GPT's output may differ from time to time, you will most likely never going to get the same results as we got.
   - The point is to show how we did this experimentation.
9) The outputs produced by GPT-4 are listed in the "output/GPT_Pred.json" file.
	
	
	
	
	
	


