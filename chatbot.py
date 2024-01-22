def chattbot(user_input):
    if "hello" in user_input.lower():
        return "hello!"
    elif "how are you" in user_input.lower():
        return "I'm just a program, but thanks for asking."
    elif "what's your name" in user_input.lower():
        return "I'm chatbot."
    # we acn add more responses.
    return "I'm not sure how to respond you because your question is not match with my stored questions answers."
f=1
while f==1:
    user_input=input('user:')
    if user_input.lower()=="exit":
        print("chatbot:","Goodbye friend!")
        f=0
    else:
        print('chatbot:',chattbot(user_input))