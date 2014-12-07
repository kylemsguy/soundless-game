label gen2:
    scene bg gen2
    with fade

    "CORNELIUS THATCHER, 1875"

    "I wake to muffled knocking."

    "I don’t answer it-- not yet. I grab my father’s watch off my bedside table."

    "10:07. God have mercy."

    "The 9:30 train’s come and gone, right outside my window, and I never heard a thing. Fourth time this week."

    "I want to scream at the sky, just to prove I can, but hearing half a scream would only frighten me more."

    "Lift your feet. Answer the door. Someone smarter than you will put the world right soon enough."
    
    # if answered North
    if northsouth == 0:
        "I open the door. Temperance Goodwinson's on the other side, covering her eyes with her hand."
        
        menu:
            g "You're not decent, are you? Get decent, Cornelius."
            
            "Flirt":
                t "You've never dreamt of seeing me in my long johns, Temperance?"

                g "Cornelius!"

                "Temperance turns red and balls her fists in anger. She realizes a moment too late that she can see me now. She stuffs her fists back over her eyes."

                "I roar with laughter, but quickly stop. Of all the things that just don't sound right anymore, laughter's the worst of them. I start putting on work clothes."
            
            "Be respectful":
                t "Long johns is decent among friends, Temperance."

                "She's rolling her eyes behind her hand, no doubt about it. I start putting on work clothes."
                
                
        "I can tell Temperance is straining her voice to speak at a normal level."

        "For someone who talks about the Lord's will as often as Temperance, she sure can't take a hint that the Lord wants us to be quiet."

        t "Does your boy want to help out at the construction site today? My crew's always glad to have him."

        g "Not today. We're meeting at Barrow's office. To discuss the… thing."

        t "Who's we, and what thing?"

        g "Oh, you know, just some pillars of the community. And you know what thing."

        "I do. There's only one thing worth discussing these days."

        "The Recent Change, they call it euphemistically. The Lull, they call it optimistically."

        "A \"Lull\" would end. And ever since the world started going quiet, it has shown no sign of reversing course."

        "When we arrive at Barrow's office, a crowd has already gathered."

        t "Just pillars of the community, eh?"

        "Temperance shrugs."

        g "Every good citizen is a pillar, I suppose."

        "The crowd parts as we approach. Every man doffs their cap to Temperance-- she's a teacher, after all, and even grown men never quite lose that fear and respect you have for a schoolmarm."

        "A fair few doff their caps to me as well. It's an honor hard earned; I've built half the houses in this town, and half of those with my own hands."
    
    elif northsouth == 1:
        "I open the door. Terrence Crenshaw's on the other side, impatiently bouncing his leg up and down like his kneecap's trying to escape."

        c "Still in your long johns, Cornelius? Honestly, I'm worried that bed will swallow you whole one day."

        "He knows as well as I do why the train doesn't wake me anymore. It's rare to hear someone make light of it though. And, to be honest, a bit of a relief."

        "I chuckle, but quickly stop. Of all the things that just don't sound right anymore, laughter's the worst of them. I start putting on work clothes."

        t "Are you going hunting today? I could leave Willet in charge of the construction site if you need an extra rifle."

        c "Another time, gladly, but today duty calls. And by duty I mean Phineas Barrow. He wants a few of us for a meeting."

        "Terrence's voice is unnaturally quiet, and he doesn't bother raising it. I think he likes when people have to lean in and listen close to hear him."

        t "Who's us? And what's this meeting about?"

        c "Us as in a select handful of local notables. And you know what the meeting's about."

        "I do. There's only one thing worth discussing these days."

        "The Recent Change, they call it euphemistically. The Lull, they call it optimistically."

        "A \"Lull\" would end. And ever since the world started going quiet, it has shown no sign of reversing course."

        "When we arrive at Barrow's office, a crowd has already gathered."

        t "A select handful of local notables, I believe you said?"

        c "What can I say? Notability just keeps lowering its standards, apparently."

        "The crowd parts as we approach. Some folks doff their caps to Crenshaw-- his tales of military derring-do have made him a legend down at the tavern."

        "Besides, whenever he comes back from hunting he saves the best cuts of meat for his friends."

        "A fair few doff their caps to me as well. It's an honor hard earned; I've built half the houses in this town, and half of those with my own hands."
    
    # northsouth == 3: Doesn't matter
    else:
        "I open the door. Ichabod Salisbury's on the other side, shuffling his feet nervously. He perks up and gives a toothy grin when he sees me."

        s "Cornelius, m'boy! Is wearing long johns at 10 in the morning some crazy eastern fashion, or are you just getting lazier on me?"

        "He knows as well as I do why the train doesn't wake me anymore. It's rare to hear someone make light of it though. And, to be honest, a bit of a relief."

        t "Don't lose your head over it, Ichabod."

        "I chuckle, but quickly stop. Of all the things that just don't sound right anymore, laughter's the worst of them. I start putting on work clothes. Salisbury stamps his foot and scowls."

        s "Why do people keep telling me that?"

        "I can tell Salisbury is straining to speak at a normal level. In fact, he's overcompensating by speaking a little too loud, and a little too desperate."

        t "Does your boy want to help out at the construction site today? My crew's always glad to have him."

        s "Oh, I'll have you teach him honest work one of these days, but right now Mr. Barrow's called a few of us for a meeting."

        t "Who's us? And what's this meeting about?"

        s "Why, just us pillars of the community, of course! Imagine, Pacific Star Railways wants to know what this daft old farmer thinks."

        s "As for what it's about, well, I think you know as well as I do."

        "I do. There's only one thing worth discussing these days."

        "The Recent Change, they call it euphemistically. The Lull, they call it optimistically."

        "A \"Lull\" would end. And ever since the world started going quiet, it has shown no sign of reversing course."

        "When we arrive at Barrow's office, a crowd has already gathered."

        t "Just pillars of the community, eh?"

        "Ichabod shrugs."

        s "More pillars sprout up every time you look."

        "The crowd parts as we approach. Some folks doff their cap to Ichabod. Plenty of them work his fields, and he puts food on everyone's plate."

        "A fair few doff their caps to me as well. It's an honor hard earned; I've built half the houses in this town, and half of those with my own hands."
        
    jump gen3