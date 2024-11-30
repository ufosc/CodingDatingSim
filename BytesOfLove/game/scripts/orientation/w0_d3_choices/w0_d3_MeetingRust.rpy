label w0_d3_MeetingRust:

    if r_rep == 50:
        r "\"Hey there! My name is Rust.\""
        show rust_base_1 at right with dissolve 


        menu w0_d3_FirstTimeRust:
            r "\"You look about my age, do you go to UB?\""
            
            "Be mean":
                $ r_rep = reputation(r_rep, -2)
                mc "\"Yeah, I do, my name is [mc].\""
                r "\"Cool, you seem chill. What’s your major?\""
                mc "\"Wouldn’t you like to know...\""
                hide rust_base_1 
                show rust_angry at right
                r "\"Damn, I was just wondering.\""
                r "\"I’m in Computer Engineering, in case you wanted to know mine.\""
                mc "\"Oh thanks, I didn’t want to know.\""
                r "\"Jeez, you don’t have to be mean about it, man.\""
                mc "\"Whatever.\""
                hide rust_angry with dissolve
                "{i}Rust leaves{/i}"

           "Be nice":
                $ r_rep = reputation(r_rep, 2)
                mc "\"Yeah I do! My name is [mc], nice to meet you!\""
                mc "\"What major are you?\""
                hide rust_angry
                show rust_base_2 at right
                r "{i}*Smiles*{/i} \"I’m in computer engineering, what about you?\""
                hide rust_base_2
                show rust_base_1 at right
                mc "\"Oh cool, I’m in computer science!\""
                mc "\"We both need to take Programming 1 as freshmen, right?\""
                mc "\"Are you going to be doing it this semester?\""
                hide rust_base_1
                show rust_base_2 at right
                r "\"Yeah, that’s what I am planning on doing.\""
                r "\"I have some programming experience from highschool, but I’m excited to start learning more here.\""
                r "\"We could totally work on projects and study together!\""
                hide rust_base_2
                show rust_base_1 at right
                mc "\"Absolutely! That would be really cool!\""
                mc "\"We’ll probably be spending a lot of time together then.\""
                hide rust_base_1
                show rust_base_2 at right
                r "\"For sure, I’m excited to become better friends with you.\""
                r "\"Well anyway, I have to get going.\""
                r "\"Gotta do a few more things before I leave for orientation.\""
                r "\"It was nice seeing you again, hope to see you around soon!\""
                hide rust_base_2 with dissolve
                "{i}Rust leaves{/i}"

    elif r_rep < 50:
        mc "Hey there, your name is..."
        window hide
        show rust_base_1 at right with dissolve 
        
        menu w0_d3_RustName:
            "Robust":
                window show
                $ r_rep = reputation(r_rep, -2)
                mc "Your name is Robust, right?"
                hide rust_base_1
                show rust_angry at right
                r "Oh, it’s you."
                r "Of course you don’t remember."
                r "My name is Rust."
                r "Now what do you want?"
            
            "Robin":
                window show
                $ r_rep = reputation(r_rep, -2)
                mc "Your name is Robin, right?"
                hide rust_base_1
                show rust_angry at right
                r "Oh, it’s you."
                r "Of course you don’t remember."
                r "My name is Rust."
                r "Now what do you want?"
            
            "Rust":
                window show
                mc "Your name is Rust, right?"
                hide rust_base_1
                show rust_angry at right
                r "Oh, it’s you."
                r "Yeah, that's my name."
                r "What do you want?"

            "Resch":
                window show
                $ r_rep = reputation(r_rep, -2)
                mc "Your name is Resch, right?"
                hide rust_base_1
                show rust_angry at right
                r "Oh, it’s you."
                r "Of course you don’t remember."
                r "My name is Rust."
                r "Now what do you want?"

        menu w0_d3_RustConvo1:
            r "\"Now what do you want?\""

            "Be mean":
                $ r_rep = reputation(r_rep, -2)
                mc "\"Don’t act like you have something I want, this is the only seat left.\""
                mc "\"If I had it my way, you wouldn’t be here.\""
                hide rust_angry
                show rust_confusedglare at right
                r "\"Dude, what is your problem?\""
                r "\"I don’t even know you and you’ve been nothing but mean to me.\""
                hide rust_confusedglare
                show rust_angry at right
                mc "\"I told you my problem, the only chair open was the one next to you.\""
                r "{i}Stands up{i} \"Let me solve that for you, then!\""
                r "\"I was just leaving anyway!\""
                mc "\"Cya.\""
                hide rust_angry with dissolve
                "{i}Rust leaves{/i}"
                

            "Be nice":
                $ r_rep = reputation(r_rep, 1)
                mc "\"Listen, Rust...\""
                mc "\"I’m sorry about our encounter the other day.\""
                mc "\"I was fresh off the drive here and was way too mean to you for no reason.\""
                mc "\"It was wrong of me and I’m sorry.\""
                hide rust_angry
                show rust_base_2 at right
                r "{i}Sighs{/i} \"That makes sense, I get it.\""
                r "\"No hard feelings.\""
                r "\"[mc], right? So what is your major?\""
                hide rust_base_2
                show rust_base_1 at right
                mc "\"Yes, and I’m in computer science.\""
                mc "\"You're in computer engineering, right?\""
                hide rust_base_1
                show rust_base_2 at right
                r "\"Yes I am!\""
                r "\"So we’re supposed to be signing up for classes today, what are you trying to get into?\""
                hide rust_base_2
                show rust_base_1 at right
                mc "\"I’m hoping to take Programming 1 this semester, are you doing the same?\""
                hide rust_base_1
                show rust_base_2 at right
                r "\"Yes, I have some programming experience from highschool, but I am excited to start learning more here.\""
                r "\"We could totally work on projects and study together!\""
                hide rust_base_2
                show rust_base_1 at right
                mc "\"Absolutely! That would be really cool!\""
                mc "\"We’ll probably be spending a lot of time together then.\""
                hide rust_base_1
                show rust_base_2 at right
                r "\"Yes, I’m excited to become better friends with you.\""
                r "\"Well anyway, I have to get going.\""
                r "\"Gotta do a few more things before I leave for orientation.\""
                r "\"It was nice seeing you again, hope to see you around soon!\""
                hide rust_base_2 with dissolve
                "{i}Rust leaves.{/i}"
                
    else:
        show rust_base_1 at right with dissolve
        mc "\"Hey, Rust!\""
        hide rust_base_1
        show rust_base_2 at right
        r "\"Oh hey! What’s up [mc]?\""
        hide rust_base_2
        show rust_base_1 at right
        mc "\"Same as you, I guess. Eating breakfast before I go to orientation and select my schedule for the semester!\""
        hide rust_base_1
        show rust_base_2 at right
        r "\"I’m a little nervous. I really hope I get in Programming 1 before they run out of spots.\""
        hide rust_base_2
        show rust_base_1 at right
        mc "\"I’m sure we’ll both get it just fine.\""
        hide rust_base_1
        show rust_base_2 at right
        r "\"That’s reassuring to hear.\""
        r "\"Hey, listen. Not to run out on you or anything, but I have to get going.\""
        r "\"I still have a few more things to do back in my room before orientation.\""
        hide rust_base_2
        show rust_base_1 at right
        mc "\"No worries! You don’t wanna be late like I was yesterday!\""
        hide rust_base_1
        show rust_base_2 at right
        r "\"You were late to day one?!\""
        hide rust_base_2
        show rust_base_1 at right
        mc "\"Yeah, it all worked out though.\""
        menu w0_d3_RustBaddiesOrFriends:
            mc "\"In fact-\""

            "\"I met some baddies.\"":
                $ r_rep = reputation(r_rep, -1)
                mc "\"When I eventually made it to my breakout room, there was only one place to sit.\""
                mc "\"Luckily, the open table had 3 girls at it\""
                mc "\"And they were BADDDD!\""
                hide rust_base_1
                show rust_base_2 at right
                r "\"Oh...\""
                r "\"That's kinda cool, I guess...\""
                hide rust_base_2
                show rust_base_1 at right
                mc "\"Oh yeah man, and they wanted me SO bad!\""
                mc "\"You should’ve seen it.\""
                hide rust_base_1
                show rust_base_2 at right
                r "\"Hey, I don’t think you should be talking about women like-\""
                hide rust_base_2
                show rust_base_1 at right
                mc "\"And THEN, we went on a tour around the school…\""
                mc  "\"The whole time they were just begging for my attention!\""
                mc "\"They were all over me!\""
                mc "\"They were literally down subterranean...\""
                hide rust_base_1
                show rust_base_2 at right
                r "\"Uh, yeah, I bet...\""
                r "\"Anyway I have to run, I'll see you later.\""
                hide rust_base_2
                show rust_base_1 at right
                mc "\"Bye!\""
                "{i}Rust leaves.{/i}"
            
            "\"I made three friends.\"":
                $ r_rep = reputation(r_rep, -1)
                mc "\"When I eventually made it to my breakout room, there was only one place to sit.\""
                mc "\"Luckily, that table had 3 girls at it who were really nice.\""
                hide rust_base_1
                show rust_base_2 at right
                r "\"Oh, cool!\""
                r "\"What were they like?\""
                hide rust_base_2
                show rust_base_1 at right
                mc "\"Their names are Python, JavaScript, and C++.\""
                mc "\"They are all computer science majors, so we should have Programming 1 with them this semester.\""
                hide rust_base_1
                show rust_base_2 at right
                r "\"Nice, we’ll need all the help we can get!\""
                hide rust_base_2
                show rust_base_1 at right
                mc "\"Haha, definitely.\""
                mc "\"And they all had interesting reasons for being in computer science.\""
                hide rust_base_1
                show rust_base_2 at right
                r "\"Cool, they sound pretty interesting.\""
                hide rust_base_2
                show rust_base_1 at right
                mc "\"Totally, we should definitely hang out with them some time.\""
                hide rust_base_1
                show rust_base_2 at right
                r "\"Absolutely!\""
                r "\"Anyway, I have to run…\""
                r "\"I’ll see you later!\""
                hide rust_base_2
                show rust_base_1 at right
                mc "\"Bye!\""
                "{i}Rust leaves.{/i}"
