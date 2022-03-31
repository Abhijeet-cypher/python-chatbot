import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_HELP = "Kindly contact College through this mail 'royalcollege@gmail.com'"
R_ADDRESS = "It\'s location is Ground floor, Gautam Labdhi Apt., Savarkar Road, Dombivli East"
R_LOCATION = "It\'s location is Ground floor, Gautam Labdhi Apt., Savarkar Road, Dombivli East 421201"
R_COURSE = "Royal College provide courses like Bcom., BMS, BAF, BSc. IT, BMM. For more detail visit " \
           "official website of Royal College"
R_COURSES = "Royal College provides courses like Bcom., BMS, BAF, BSc. IT, BMM, etc."

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sorry, couldn't get you",
                "What does that mean?"][
        random.randrange(4)]
    return response
