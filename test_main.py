import main.main as m

def test_affiche_message():
    assert m.affiche_message("bob") == "Hello, Bob"
    assert m.affiche_message("") == "Hello, my friend"
    assert m.affiche_message(" ") == "Hello, my friend"
    assert m.affiche_message("      ") == "Hello, my friend"
    assert m.affiche_message("JERRY") == "HELLO, JERRY!"

def test_affiche_plusieur_message():
    assert m.affiche_message("Amy,bob") == "Hello, Amy and Bob"
    assert m.affiche_message("Amy,Bob,Jerry") =="Hello, Amy, Bob and Jerry"
    assert m.affiche_message("Amy,BOB,Jerry") == "Hello, Amy and Jerry. AND HELLO, BOB !"
    assert m.affiche_message("bob     ,amy") == "Hello, Bob and Amy"

def test_affiche_message_avec_particulariter():
    assert m.affiche_message("!bob,amy") == "Hello, Amy"
    assert m.affiche_message("bob,!bob,amy ,bob") == "Hello, Bob(X2) and Amy"
    assert m.affiche_message("bob,!bob,amy ,bob, jean,alice,jules,albert") == "Hello, world !"
    assert m.affiche_message("!bob, JULES,AMY,ALICE,CHARLOTTE,ANTOINE,MARTIN") == "HELLO, WORLD !"
    assert m.affiche_message("bob,yoda,amy") == "Bob, Yoda and Amy, Hello"
    assert m.affiche_message("bob,!bob,amy ,bob, jean,alice,jules,albert,yoda") == "World, Hello !"

def test_affiche_message_plusieur_particulariter():
    assert m.affiche_message("!bob, JULES,AMY,ALICE,CHARLOTTE,ANTOINE,MARTIN,yoda") == "WORLD, HELLO !"
    assert m.affiche_message("bob,*alice, amy") == "Hello, Bob and Amy and our special guest Alice"

    
