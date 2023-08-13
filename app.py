import click as click_package
import streamlit as st

def game_intro():
    st.write("Welcome to the Text Adventure Game!")
    st.write("You are Cody Sewell, a brave adventurer on a quest.")
    st.write("Your companion, Bruce, has a habit of getting into trouble.")
    st.write("Can you overcome Bruce's antics and achieve victory?")
    st.write("\n")

def start_adventure():
    player_hp = 10
    monster_hp = 15
    has_key = False
    has_map = False

    st.write("You find yourself at the entrance of a mysterious dungeon.")
    st.write("Bruce suggests, 'Let's explore the depths and find treasure!'")
    choice = st.selectbox("What will you do?", options=["Enter the dungeon", "Turn back"])

    if choice == "Enter the dungeon":
        st.write("You and Bruce enter the dark dungeon.")
        st.write("As you explore, you encounter a ferocious dragon!")
        st.write("Bruce accidentally steps on a loose stone, making a loud noise.")
        st.write("The dragon awakens and roars angrily.")
        st.write("Options:")
        action = st.radio("Choose your action:", options=["Fight", "Hide", "Run"])

        if action == "Fight":
            st.write("You decide to fight the dragon head-on!")
            if has_key and has_map:
                st.write("With the help of the magic key and map, you defeat the dragon!")
                st.success("Congratulations! You've saved the day!")
            else:
                st.error("You're not adequately prepared to defeat the dragon.")
                st.error("The dragon's fiery breath overwhelms you.")
                st.write("Game Over")
        elif action == "Hide":
            st.write("You and Bruce hide behind some rocks, hoping the dragon doesn't spot you.")
            st.write("Unfortunately, Bruce sneezes loudly, drawing the dragon's attention.")
            st.error("The dragon spots you and unleashes its fiery breath.")
            st.write("Game Over")
        else:
            st.write("You and Bruce attempt to flee the dungeon in a panic.")
            st.write("The dragon gives chase, but you manage to escape just in time.")
            st.write("You're back outside the dungeon, safe but shaken.")
            st.success("You've narrowly escaped the dragon's wrath.")
def main():
    st.title("Cody's Epic Adventure")

    game_intro()
    st.button("Start Adventure", start_adventure)

if __name__ == "__main__":
    main()

import streamlit as st

def game_intro():
    st.write("Welcome to the Text Adventure Game!")
    st.write("You are Cody Sewell, a brave adventurer on a quest.")
    st.write("Your companion, Bruce, has a habit of getting into trouble.")
    st.write("Can you overcome Bruce's antics and achieve victory?")
    st.write("\n")

def start_adventure():
    player_hp = 10
    monster_hp = 15
    has_key = False
    has_map = False

    st.write("You find yourself at the entrance of a mysterious dungeon.")
    st.write("Bruce suggests, 'Let's explore the depths and find treasure!'")
    choice = st.selectbox("What will you do?", options=["Enter the dungeon", "Turn back"])

    if choice == "Enter the dungeon":
        st.write("You and Bruce enter the dark dungeon.")
        st.write("As you explore, you encounter a ferocious dragon!")
        st.write("Bruce accidentally steps on a loose stone, making a loud noise.")
        st.write("The dragon awakens and roars angrily.")
        st.write("Options:")
        action = st.radio("Choose your action:", options=["Fight", "Hide", "Run"])

        if action == "Fight":
            st.write("You decide to fight the dragon head-on!")
            if has_key and has_map:
                st.write("With the help of the magic key and map, you defeat the dragon!")
                st.success("Congratulations! You've saved the day!")
            else:
                st.error("You're not adequately prepared to defeat the dragon.")
                st.error("The dragon's fiery breath overwhelms you.")
                st.write("Game Over")
        elif action == "Hide":
            st.write("You and Bruce hide behind some rocks, hoping the dragon doesn't spot you.")
            st.write("Unfortunately, Bruce sneezes loudly, drawing the dragon's attention.")
            st.error("The dragon spots you and unleashes its fiery breath.")
            st.write("Game Over")
        else:
            st.write("You and Bruce attempt to flee the dungeon in a panic.")
            st.write("The dragon gives chase, but you manage to escape just in time.")
            st.write("You're back outside the dungeon, safe but shaken.")
            st.success("You've narrowly escaped the dragon's wrath.")

def main():
    st.title("Cody's Epic Adventure")

    game_intro()
    st.button("Start Adventure", start_adventure)

if __name__ == "__main__":
    main()
