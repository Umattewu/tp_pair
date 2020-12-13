import main as m

def test_affiche_message_features_1_2_and_2_with_spaces_and_3():
    assert m.afficher_message("bob") == "Hello, Bob"
    assert m.afficher_message("") == "Hello, my friend"
    assert m.afficher_message(" ") == "Hello, my friend"
    assert m.afficher_message("      ") == "Hello, my friend"
    assert m.afficher_message("JERRY") == "HELLO, JERRY!"

def test_affiche_plusieurs_personnes_features_4_5_6_7_and_8():
    assert m.afficher_message("Amy,bob") == "Hello, Amy and Bob"
    assert m.afficher_message("Amy,Bob,Jerry") =="Hello, Amy, Bob and Jerry"
    assert m.afficher_message("Amy,BOB,Jerry") == "Hello, Amy and Jerry. AND HELLO, BOB !"
    assert m.afficher_message("bob     ,amy") == "Hello, Bob and Amy"

def test_affiche_message_avec_particularites_features_9_10_11_12_and_15():
    assert m.afficher_message("!bob,amy") == "Hello, Amy"
    assert m.afficher_message("bob,!bob,amy ,bob") == "Hello, Bob(X2) and Amy"
    assert m.afficher_message("bob,!bob,amy ,bob, jean,alice,jules,albert") == "Hello, world !"
    assert m.afficher_message("!bob, JULES,AMY,ALICE,CHARLOTTE,ANTOINE,MARTIN") == "HELLO, WORLD !"
    assert m.afficher_message("bob,*alice, amy") == "Hello, Bob and Amy and our special guest Alice"

def test_affiche_message_avec_yoda_features_13_and_14():
    assert m.afficher_message("bob,yoda,amy") == "Bob, Yoda and Amy, Hello"
    assert m.afficher_message("bob,!bob,amy ,bob, jean,alice,jules,albert,yoda") == "World, Hello !"
    assert m.afficher_message("!bob, JULES,AMY,ALICE,CHARLOTTE,ANTOINE,MARTIN,yoda") == "WORLD, HELLO !"


    
