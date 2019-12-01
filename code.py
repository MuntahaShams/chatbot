import aiml

# Create the kernel and learn AIML files

kernel = aiml.Kernel()
kernel.learn("negative_sentence.aiml")
# Press CTRL-C to break this loop
while True:
    print (kernel.respond(input("Enter your message >> ")))