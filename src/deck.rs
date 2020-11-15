use crate::ballons::{ActionCard, Balloons};
use rand::rngs::ThreadRng;
use rand::seq::SliceRandom;

#[derive(Debug)]
pub struct BalloonDeck {
    pub cards: Vec<Balloons>,
    rng: ThreadRng,
}

#[derive(Debug)]
pub struct ActionDeck {
    pub cards: Vec<ActionCard>,
    nb_parent_cards: usize,
    rng: ThreadRng,
}

impl BalloonDeck {
    pub fn new(rng: ThreadRng) -> BalloonDeck {
        let mut deck = BalloonDeck {
            cards: Vec::new(),
            rng,
        };
        deck.fill();

        deck
    }

    pub fn shuffle(&mut self) {
        self.cards.shuffle(&mut self.rng);
    }

    fn fill(&mut self) {
        for i in 0..5 {
            for c in &[
                Balloons::Red,
                Balloons::Yellow,
                Balloons::Blue,
                Balloons::Green,
                Balloons::Violet,
            ] {
                self.cards.push(*c);
            }
        }
    }
}

impl ActionDeck {
    pub fn new(nb_parent_cards: usize, rng: ThreadRng) -> ActionDeck {
        let mut deck = ActionDeck {
            cards: Vec::new(),
            nb_parent_cards,
            rng,
        };
        deck.fill();

        deck
    }
    pub fn shuffle(&mut self) {
        self.cards.shuffle(&mut self.rng);
    }

    pub fn fill(&mut self) {
        for i in 0..5 {
            for c in &[
                ActionCard::Red,
                ActionCard::Yellow,
                ActionCard::Blue,
                ActionCard::Green,
                ActionCard::Violet,
            ] {
                self.cards.push(*c);
            }
        }
        for i in 0..self.nb_parent_cards {
            self.cards.push(ActionCard::Parent);
        }
    }
}
