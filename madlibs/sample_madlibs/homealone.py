def madlib():
    time_of_day = input("Time of day: ")
    adj1 = input("Adjective: ")
    adj2 = input("Adjective: ")
    animal1 = input("Animal: ")
    verb1 = input("Verb(past-tense): ")
    verb2 = input("Verb: ")
    time1 = input("Time: ")
    time2 = input("Time: ")
    noun1 = input("Noun(plural): ")

    madlib = f"It was a dark and stormy {time_of_day}. \
I was alone at home and about to go to bed, when I saw a {adj1} shadow figure at my window.\
'Who’s there' I shouted. Suddenly there was a flash of lightning followed by thundershower. \
I saw a {animal1}’s face followed by a {adj2} thunderous roar at the window. It looked like the {animal1} from the local circus \
that had been announced missing on the television news channel. I felt very {verb1}. I ran to my bed and pulled my blanket \
over my head. I started to {verb2} for my {noun1} but there was no reply. Then I remembered they were at a late night party. \
I peeped out of my blanket but it was too dark to see anything. Then I heard footsteps. \
They were getting louder and louder. Soon the footsteps died off. \
The grand father clock struck {time1}. I went back to bed and tried to sleep, but couldn’t. I felt too frightened. \
I sat up my mind full of scary thoughts. After some time passed, finally I fell asleep. \
I woke up only after {time2} in the morning and switched on the TV news. \
I was excited to see the {animal1} was already trapped in the wee hours of the morning by the ring master of the circus. \
I felt very much relieved after the news. \
Later I narrated the whole incident to my {noun1}. \
They were dumb shocked and decided in future not to leave me alone at home during {time_of_day}." \

    print(madlib)