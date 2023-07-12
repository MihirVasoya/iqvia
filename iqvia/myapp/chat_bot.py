# chat_bot.py
import json
import openai



openai.api_key = "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"

chat_history = []  # Store chat history

def generate_response(input_text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input_text,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

def chatbot_response(user_input, context):
    input_text = f"""
    Context: {context}
    Question: {user_input}

    Answer: 
    """

    response = generate_response(input_text)

    # Store current user input and chatbot response in chat history
    chat_history.append({"user_input": user_input, "response": response})

    return chat_history



# from django.http import JsonResponse
# from django.shortcuts import render



# def your_view(request):
#     if request.method == 'POST' and 'arrayData' in request.POST:
#         array_data = request.POST.get('patient')
       
        
   

# def index(request):
   

   
#     return render(request, 'index.html')