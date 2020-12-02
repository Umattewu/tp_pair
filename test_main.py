import main.main as m

def test_affiche_message():
    assert m.affiche_message("bob") == "Hello, Bob"
    assert m.affiche_message("") == "Hello, my friend"
    assert m.affiche_message(" ") == "Hello, my friend"
    assert m.affiche_message("      ") == "Hello, my friend"
    assert m.affiche_message("JERRY") == "HELLO, JERRY!"
    assert m.affiche_message("Amy,bob") == "Hello, Amy and Bob"
    assert m.affiche_message("Amy,Bob,Jerry") =="Hello, Bob, Amy and Jerry"
    assert m.affiche_message("Amy,BOB,Jerry") == "Hello, Amy, Jerry. AND HELLO, BOB !"
    
    
    
    
    
