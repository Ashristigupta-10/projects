import random

R_Eating="i don't like eating anything because I,m a bot obviosly!"


def unknown():
    response=['could you please re-phrase that?',
              "...",
              "Sounds about right",
              "what does that mean?"][random.randrange(4)]
    return response
