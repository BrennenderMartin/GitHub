package Blackjack;

import java.util.ArrayList;

/**
 * @author 
 * @version 
 */
public class blackjack {

    Card[] deck = {};
    for (int color = 1; color < 4; color++) {
        for (int value  = 1; value < 13; value++) {
            deck[(value * color) - 1] = Card.Card(color, value);
        }
    }

    public static void main(String[] args) {
        new blackjack();
    }

    public blackjack() {

    }
}
