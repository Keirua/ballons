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
    returned_cards: Vec<ActionCard>,
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
        for _ in 0..5 {
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
            returned_cards: Vec::new(),
            nb_parent_cards,
            rng,
        };
        deck.fill();

        deck
    }

    pub fn deal(&mut self) -> ActionCard {
        match self.cards.pop() {
            Some(card) => {
                // Si on a une carte, on a distribue
                self.returned_cards.push(card);
                card
            }
            None => {
                // S’il n’y a plus de cartes, on retourne la pioche,
                // on la mélange et distribue la première carte
                self.cards = self.returned_cards.clone();
                self.returned_cards.clear();
                self.deal()
            }
        }
    }

    pub fn shuffle(&mut self) {
        self.cards.shuffle(&mut self.rng);
    }

    pub fn fill(&mut self) {
        for _ in 0..5 {
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
        for _ in 0..self.nb_parent_cards {
            self.cards.push(ActionCard::Parent);
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use rand::rngs::ThreadRng;
    use rand::thread_rng;

    #[test]
    fn test_greet() {
        let mut d = ActionDeck::new(3, thread_rng());
        for _ in 0..100 {
            d.deal();
        }
    }
}
