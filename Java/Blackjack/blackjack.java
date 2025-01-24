package Blackjack;

import java.util.ArrayList;

public class blackjack {

    int numberOfDecks = 6;
    int numberOfCards = 52 * numberOfDecks;

    ArrayList<ArrayList<Card>> deck = new ArrayList<>();

    public static void main(String[] args) {
        new blackjack();
    }

    public blackjack() {
        for (int i = 1; i <= numberOfDecks; i++) {

            ArrayList<Card> row = new ArrayList<>();

            for (int j = 1; j <= 4; j++) {
                for (int k = 1; k <= 13; k++) {
                    int color = j;
                    int value = k;
                    Card card = new Card(color, value);
                    row.add(card);
                }
            }
        }
    }
}
