import random

CATEGORY_OPTIONS = {
    "fantasy": {
         "option1": ['Ram', 'Arjun', 'Kiran', 'Shiva', 'Krishna', 'Vishnu', 'Indra', 'Agni', 'Varuna', 'Brahma'],
         "option2": ['Sita', 'Radha', 'Parvati', 'Lakshmi', 'Saraswati', 'Ganga', 'Durga', 'Kali', 'Uma', 'Rukmini'],
         "option3": ['in a mystical forest', 'in a dark castle', 'in a magical village', 'by an enchanted lake', 'within a hidden cave', 'on a floating island', 'under a starlit sky', 'in a realm of magic', 'amid ancient ruins', 'beside a sacred river'],
         "option4": ['a powerful wizard emerged', 'a wise sage appeared', 'a brave warrior stood', 'a cunning thief lurked', 'a noble knight arrived', 'a fearless hunter ventured', 'a legendary bard sang', 'a mysterious seer foretold', 'a guardian spirit protected', 'a benevolent king ruled'],
         "option5": ['and battled a fierce dragon', 'and discovered a lost treasure', 'and vanquished a dark force', 'and saved the enchanted realm', 'and fulfilled an ancient prophecy', 'and restored peace', 'and forged new alliances', 'and conquered evil', 'and ignited hope', 'and transformed destiny'],
         "option6": ['bringing eternal peace.', 'ushering in a golden age.', 'and became a legend.', 'with magic and wonder.', 'as the stars aligned.', 'while destiny smiled.', 'and myths were born.', 'with the gods watching.', 'as legends echoed.', 'and fate was sealed.']
    },
    "adventure": {
         "option1": ['Explorer A', 'Captain X', 'Ranger Y', 'Adventurer Z', 'Seeker Q', 'Nomad W', 'Traveler V', 'Pioneer U', 'Scout T', 'Wanderer S'],
         "option2": ['with his loyal friend', 'accompanied by a brave guide', 'supported by a trusted ally', 'with a fearless companion', 'joined by a wise mentor', 'with a steadfast partner', 'with an experienced scout', 'supported by a comrade', 'with an intrepid sidekick', 'joined by a daring friend'],
         "option3": ['in treacherous mountains', 'through dangerous jungles', 'across uncharted islands', 'in mysterious deserts', 'through ancient ruins', 'across stormy seas', 'in wild savannas', 'through perilous canyons', 'across frozen tundras', 'in remote highlands'],
         "option4": ['found a hidden map', 'discovered a secret key', 'uncovered a cryptic clue', 'retrieved a lost artifact', 'stumbled upon an old compass', 'received a mysterious letter', 'encountered a coded message', 'secured an ancient relic', 'obtained a legendary token', 'was given a sacred scroll'],
         "option5": ['and faced relentless challenges', 'and overcame insurmountable odds', 'and braved formidable foes', 'and outsmarted dangerous traps', 'and fought against overwhelming forces', 'and navigated treacherous paths', 'and defied destiny', 'and risked everything', 'and solved ancient riddles', 'and conquered the unknown'],
         "option6": ['returning as a hero.', 'earning eternal glory.', 'and rewriting history.', 'with tales of valor.', 'and becoming a legend.', 'with their name forever remembered.', 'and inspiring future adventurers.', 'as the journey transformed them.', 'with an undying spirit.', 'and their saga continued.']
    },
    "romance": {
         "option1": ['Lover A', 'Sweetheart B', 'Beloved C', 'Darling D', 'Paramour E', 'Cupid F', 'Valentine G', 'Amour H', 'Cherish I', 'Adore J'],
         "option2": ['met Sweetheart K', 'encountered Darling L', 'embraced Beloved M', 'gazed at Lover N', 'admired Paramour O', 'cherished Cupid P', 'adored Valentine Q', 'savored Amour R', 'treasured Cherish S', 'worshipped Adore T'],
         "option3": ['in a quaint town', 'in a bustling city', 'by the sparkling seaside', 'in a serene village', 'under a starlit sky', 'at a romantic resort', 'in a secret garden', 'near a gentle river', 'in an old town square', 'at a moonlit balcony'],
         "option4": ['where destiny intervened', 'where fate brought them together', 'in an unexpected twist', 'amid soft whispers', 'as hearts aligned', 'with a magical spark', 'in a serendipitous encounter', 'as time stood still', 'with silent glances', 'in a moment of wonder'],
         "option5": ['overcoming all obstacles', 'despite the odds', 'with passion and perseverance', 'through trials of heart', 'against societal norms', 'with unwavering faith', 'beyond all challenges', 'with tender resolve', 'through bittersweet moments', 'amid infinite hope'],
         "option6": ['and their love became timeless.', 'and passion bloomed eternally.', 'and dreams intertwined.', 'as hearts sang in unison.', 'and romance flourished.', 'as their story became a legend.', 'and destiny smiled upon them.', 'and the world embraced their tale.', 'and love conquered all.', 'and forever was written in their stars.']
    },
    "mystery": {
         "option1": ['Detective X', 'Inspector Y', 'Agent Z', 'Sleuth A', 'Investigator B', 'Spy C', 'Officer D', 'Analyst E', 'Researcher F', 'Tracker G'],
         "option2": ['with his clever partner', 'assisted by a skilled aide', 'with a sharp-witted colleague', 'joined by a trusted sidekick', 'with a keen observer', 'aided by a resourceful friend', 'with a diligent assistant', 'accompanied by a quiet confidant', 'with an experienced analyst', 'supported by a loyal helper'],
         "option3": ['in a gloomy city', 'in a shadowy town', 'amid foggy streets', 'within a maze of alleys', 'in a mysterious mansion', 'beneath a cloak of night', 'around haunted corners', 'in a silent suburb', 'amid urban whispers', 'in a city of secrets'],
         "option4": ['uncovered a hidden clue', 'discovered a coded message', 'stumbled upon disturbing evidence', 'found a secret diary', 'revealed a shocking truth', 'unraveled an enigma', 'detected a silent warning', 'exposed a cunning plot', 'revealed a dark secret', 'discovered an unexpected lead'],
         "option5": ['that twisted the case further', 'leading to unexpected turns', 'that baffled even the experts', 'which deepened the mystery', 'that challenged the obvious', 'causing chaos among suspects', 'that blurred the lines of truth', 'that forced new inquiries', 'which left everyone in suspense', 'that shattered preconceptions'],
         "option6": ['and the case was closed.', 'and justice was served.', 'and truth emerged from shadows.', 'and mysteries unraveled.', 'and secrets faded away.', 'and clarity replaced confusion.', 'and the detective prevailed.', 'and answers finally surfaced.', 'and the enigma was solved.', 'and darkness was dispelled.']
    },
    "horror": {
         "option1": ['A cursed soul', 'A haunted figure', 'A restless spirit', 'An eerie wanderer', 'A doomed victim', 'A mysterious entity', 'A sinister shadow', 'A ghastly apparition', 'A chilling presence', 'A macabre specter'],
         "option2": ['tormented by the past', 'haunted by lost memories', 'pursued by nightmares', 'bound by a sinister fate', 'plagued with dread', 'enshrouded in darkness', 'lost in perpetual terror', 'shadowed by doom', 'gripped by horror', 'enslaved by fear'],
         "option3": ['in an abandoned mansion', 'within a cursed village', 'in a dark forest', 'inside a haunted asylum', 'at a forsaken cemetery', 'beneath a stormy sky', 'in a desolate ruin', 'amid crumbling walls', 'in a shadowy labyrinth', 'under a blood-red moon'],
         "option4": ['encountered unearthly sounds', 'heard bloodcurdling screams', 'witnessed ghastly visions', 'experienced supernatural chills', 'faced a terrifying presence', 'saw things no mortal should', 'encountered spectral figures', 'heard whispers from the abyss', 'witnessed impossible horrors', 'felt a creeping dread'],
         "option5": ['that shattered their sanity', 'that froze their blood', 'that tormented their soul', 'that defied reason', 'that summoned pure terror', 'that blotted out hope', 'that clawed at their mind', 'that ensnared their spirit', 'that left scars unseen', 'that defied explanation'],
         "option6": ['and the terror was everlasting.', 'and nightmares became reality.', 'and horror reigned supreme.', 'and darkness consumed all.', 'and despair took hold.', 'and the haunted remained.', 'and no light could break through.', 'and fear prevailed.', 'and the curse lived on.', 'and terror echoed forever.']
    },
    "sci-fi": {
         "option1": ['A space explorer', 'A futuristic warrior', 'A time traveler', 'An alien diplomat', 'A cybernetic agent', 'A star pilot', 'A galactic hero', 'A cosmic wanderer', 'A virtual reality savant', 'A robotic engineer'],
         "option2": ['from a distant planet', 'of an advanced civilization', 'with a mysterious past', 'with cutting-edge tech', 'accompanied by an AI', 'with cybernetic limbs', 'with quantum abilities', 'armed with futuristic gear', 'on a secret mission', 'with interstellar charm'],
         "option3": ['in a universe of endless stars', 'in a galaxy far away', 'across interstellar voids', 'in an alternate dimension', 'in a dystopian future', 'in a digital realm', 'amid cosmic wonders', 'in an ever-expanding cosmos', 'beyond known space', 'in a realm of science'],
         "option4": ['discovered a hidden planet', 'uncovered alien secrets', 'encountered bizarre phenomena', 'traversed wormholes', 'faced rogue robots', 'explored uncharted galaxies', 'challenged the laws of physics', 'battled cosmic foes', 'decoded ancient signals', 'unveiled futuristic marvels'],
         "option5": ['that redefined existence', 'that shattered reality', 'that defied expectations', 'that sparked a revolution', 'that altered destiny', 'that ignited innovation', 'that blurred science and myth', 'that reshaped the cosmos', 'that inspired awe', 'that rewrote the future'],
         "option6": ['and the universe marveled.', 'and the stars aligned in wonder.', 'and destiny was transformed.', 'and time bent in awe.', 'and the future was reborn.', 'and cosmic legends were born.', 'and science prevailed.', 'and the galaxy cheered.', 'and the saga continued.', 'and fate was rewritten.']
    }
 

  
}

def generate_story(category, option1, option2, option3, option4, option5, option6):
    start_options = [
        "Once upon a time,",
        "In a land far away,",
        "Long ago,",
        "In a forgotten kingdom,",
        "On a cold winter night,"
    ]
    
    story = random.choice(start_options) + " "
    
    if category not in CATEGORY_OPTIONS:
        return "Invalid category."
    
    data = CATEGORY_OPTIONS[category]
    try:
        idx1 = int(option1) - 1
        idx2 = int(option2) - 1
        idx3 = int(option3) - 1
        idx4 = int(option4) - 1
        idx5 = int(option5) - 1
        idx6 = int(option6) - 1
    except Exception:
        return "Invalid options selection."
    
    part1 = data['option1'][idx1] if idx1 < len(data['option1']) else ""
    part2 = data['option2'][idx2] if idx2 < len(data['option2']) else ""
    part3 = data['option3'][idx3] if idx3 < len(data['option3']) else ""
    part4 = data['option4'][idx4] if idx4 < len(data['option4']) else ""
    part5 = data['option5'][idx5] if idx5 < len(data['option5']) else ""
    part6 = data['option6'][idx6] if idx6 < len(data['option6']) else ""
    

    if category == "fantasy":
        story+=f"""{part1} the brave knight and {part2} the wise sorcerer stood at the edge of {part3}, the Forbidden Forest. 
        Legends spoke of {part4}, the Crystal of Eternity, hidden deep within its cursed heart. 
        Determined to retrieve it, they ignored the warnings of {part5}, an old hermit who spoke of ancient curses. 
        As they ventured deeper, the air grew thick with {part6}, a swirling mist infused with magic, whispering forgotten spells. 
        Suddenly, the ground trembled, and dark shadows moved between the trees. 
        "We're not alone," {part2} whispered, gripping their staff.  
        A pair of glowing eyes emerged from the darkness, followed by a monstrous figure.  
        The guardian of the crystal had awakened, its colossal form blocking their path.  
        {part1} drew their sword, its blade shimmering with enchantment.  
        "We fight or perish," they declared, stepping forward.  
        The beast roared, shaking the very fabric of the world, as the final battle for the Crystal of Eternity began."""

    elif category == "adventure":
        story+=f"""{part1}, an eager explorer, and {part2}, a skilled navigator, arrived at {part3}, the uncharted ruins of Zantora. 
        Tales spoke of {part4}, the lost map that led to untold riches. 
        Ignoring the warnings of {part5}, a weary traveler who barely escaped, they entered the ruins. 
        The air grew thick with {part6}, a musty scent of ancient stone and damp moss. 
        As they proceeded, they discovered strange carvings on the walls, depicting a forgotten civilization. 
        Suddenly, the ground beneath them shifted, revealing a hidden chamber.  
        Inside, a massive golden door stood locked with an intricate puzzle.  
        {part2} examined the symbols while {part1} deciphered an ancient text.  
        "It’s a test," {part2} murmured. "Only the worthy may enter."  
        As they placed the right pieces into the puzzle, the door rumbled open.  
        The treasure was within reach, but so was the deadly trap waiting to be triggered."""

    elif category == "sci-fi":
        story+=f"""{part1}, a daring astronaut, and {part2}, an AI companion, stood before {part3}, the mysterious space anomaly.  
        Data suggested it was a gateway to {part4}, a parallel dimension of infinite knowledge.  
        Suddenly, {part5}, a rogue AI drone, warned them to turn back.  
        But they proceeded, and the deeper they went, the air (or lack thereof) grew thick with {part6}, a pulsating energy field distorting reality itself.  
        As they passed through the anomaly, the ship’s controls flickered uncontrollably.  
        "This isn’t just a portal," {part1} realized. "It’s alive."  
        An eerie voice echoed in their minds, speaking in unknown frequencies.  
        They were no longer alone.  
        The anomaly had brought them to a strange dimension where time moved differently.  
        Planets orbited in unnatural patterns, and gravity bent at impossible angles.  
        Then, the AI companion detected something horrifying—  
        They were being watched by beings beyond human comprehension.  
        And they had just opened the door to their realm."""

    elif category == "horror":
       story+=f"""{part1}, a skeptical journalist, and {part2}, a paranormal investigator, arrived at {part3}, the abandoned Blackwood Manor.  
        Rumors spoke of {part4}, a cursed artifact that brought nightmares to life.  
        As they stepped inside, {part5}, an eerie voice from the shadows, warned them to leave.  
        But curiosity led them forward, and the air grew thick with {part6}, a putrid mix of decay and something... unnatural.  
        The wooden floor creaked under their weight as they ascended the grand staircase.  
        A sudden cold breath brushed against {part1}’s neck, sending shivers down their spine.  
        "Did you feel that?" {part2} whispered.  
        Then, a loud bang echoed through the halls.  
        The doors slammed shut behind them, locking them in.  
        In the dim candlelight, shadows danced on the walls, moving on their own.  
        A mirror at the end of the hall reflected not just them—but something else.  
        Something that wasn't there.  
        And it was smiling."""

    elif category == "mystery":
        story+=f"""{part1}, a brilliant detective, and {part2}, a sharp-eyed reporter, reached {part3}, the crime scene of a high-profile disappearance.  
        The only clue was {part4}, a cryptic note left behind.  
        A local informant, {part5}, warned them that some secrets should remain buried.  
        But as they pieced together the puzzle, the air grew thick with {part6}, a tense silence, as if someone—or something—was watching.  
        The victim’s apartment was left untouched, except for a single red string tied around the doorknob.  
        "A message," {part1} muttered, inspecting the strange mark on the floor.  
        Then, a hidden door was discovered behind a bookshelf.  
        Inside, dozens of photographs lined the walls—each one of the missing person, taken at different times of the day.  
        "Someone was watching them," {part2} whispered.  
        Suddenly, the door behind them clicked shut.  
        The trap had been set.  
        And the real game had just begun."""

    elif category == "romance":
        story+=f"""{part1}, a shy artist, and {part2}, a passionate writer, found themselves at {part3}, the charming old bookstore where they first met.  
        Stories whispered of {part4}, a love letter lost between the pages of a forgotten novel.  
        Just as {part5}, a mysterious shopkeeper, hinted at its whereabouts, a sudden hush filled the store.  
        The air grew thick with {part6}, the scent of aged paper and unspoken words hanging in the air.  
        As {part1} reached for a dusty book, a faded envelope slipped onto the floor.  
        "Could this be it?" {part2} murmured, picking it up with trembling hands.  
        Inside was a heartfelt confession, written decades ago but never delivered.  
        "It’s like fate wanted us to find this," {part1} said softly.  
        Their eyes met, and in that moment, the world seemed to pause.  
        Perhaps this letter wasn’t just a relic of the past—  
        But a sign for the future they could write together."""

    else:
        return "Invalid category. Please choose from: fantasy, adventure, sci-fi, horror, mystery, romance."
    
    return story
    