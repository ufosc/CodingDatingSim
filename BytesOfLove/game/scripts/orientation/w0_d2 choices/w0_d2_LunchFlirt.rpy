label w0_d2_LunchFlirt:
    menu w0_d2_LunchFlirtC:
        # I added this line can be removed - Lazzy
        mc "Hmmm who should I flirt with?"

        "Python":
            $ p_rep = reputation(p_rep, -2)
            mc "Especially you Python."
            mc "*winks*"
            p "Wow, way to ruin an apology."
            p "I expected nothing less."
            c "Typical man..."
        "C++":
            $ c_rep = reputation(c_rep, -2)
            mc "Especially you C++."
            mc "*winks*"
            c "Wow, way to ruin an apology."
            c "I expected nothing less."
            js "Typical man..."

        "JavaScript":
            $ js_rep = reputation(js_rep, -2)
            mc "Especially you JavaScript."
            mc "*winks*"
            js "Wow, way to ruin an apology."
            js "I expected nothing less."
            c "Typical man..."

        "Everyone":
            $ p_rep = reputation(p_rep, -6)
            $ js_rep = reputation(js_rep, -6)
            $ c_rep = reputation(c_rep, -6)
            mc "Maybe I could get to know all of you really well back at my hotel tonight…"
            c "What the actual fuck is wrong with you."
            c "That is so disgusting."
            p "I can’t believe you, you are despicable."
            js "I think I actually might throw up"

    mc "Hmm, I thought that would go differently."
    mc "Can’t blame me, shooters gotta shoot…"

    jump w0_d2_AfterLunch
