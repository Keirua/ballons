use crate::ballons::{ActionCard, Balloons};
use std::collections::HashMap;

#[derive(Debug)]
pub struct Player {
    ballons: HashMap<Balloons, usize>,
    returned_balloons: Vec<Balloons>,
    nb_cards: usize,
}

impl Player {
    pub fn default() -> Player {
        let mut p = Player {
            ballons: HashMap::new(),
            returned_balloons: Vec::new(),
            nb_cards: 0,
        };
        p.ballons.insert(Balloons::Red, 0);
        p.ballons.insert(Balloons::Blue, 0);
        p.ballons.insert(Balloons::Green, 0);
        p.ballons.insert(Balloons::Violet, 0);
        p.ballons.insert(Balloons::Yellow, 0);
        p
    }

    pub fn new_with_hand(hand: Vec<Balloons>) -> Player {
        let mut p = Player {
            ballons: HashMap::new(),
            returned_balloons: Vec::new(),
            nb_cards: 0,
        };
        for b in hand.iter() {
            p.deal(*b);
        }

        p
    }

    pub fn deal(&mut self, b: Balloons) {
        let count = self.ballons.entry(b).or_insert(0);
        *count += 1;
        self.nb_cards += 1;
    }

    pub fn has_lost(&self) -> bool {
        self.returned_balloons.len() == self.nb_cards
    }

    pub fn play_card(&mut self, c: ActionCard) {
        match c {
            ActionCard::Red => self.burst(Balloons::Red),
            ActionCard::Blue => self.burst(Balloons::Blue),
            ActionCard::Green => self.burst(Balloons::Green),
            ActionCard::Violet => self.burst(Balloons::Violet),
            ActionCard::Yellow => self.burst(Balloons::Yellow),
            ActionCard::Parent => self.recover(),
        }
    }

    pub fn notify(&mut self, c: ActionCard) {

    }

    fn burst(&mut self, b: Balloons) {
        let count = self.ballons.entry(b).or_insert(0);
        if *count > 0 {
            *count -= 1;
            self.returned_balloons.push(b);
        }
    }

    fn recover(&mut self) {
        if let Some(b) = self.returned_balloons.pop() {
            let count = self.ballons.entry(b).or_insert(0);
            *count += 1;
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_run_game() {
        let mut p = Player::default();
        p.deal(Balloons::Red);
        p.deal(Balloons::Green);
        p.deal(Balloons::Yellow);
        p.burst(Balloons::Blue);
        p.burst(Balloons::Red);

        p.recover();
        p.recover();
        p.burst(Balloons::Yellow);

        assert_eq!(1, *p.ballons.entry(Balloons::Red).or_insert(0));
        assert_eq!(0, *p.ballons.entry(Balloons::Blue).or_insert(0));
        assert_eq!(1, *p.ballons.entry(Balloons::Green).or_insert(0));
        assert_eq!(0, *p.ballons.entry(Balloons::Violet).or_insert(0));
        assert_eq!(0, *p.ballons.entry(Balloons::Yellow).or_insert(0));
    }

    #[test]
    fn test_has_lost() {
        let mut p = Player::default();
        p.deal(Balloons::Red);
        p.deal(Balloons::Green);

        p.burst(Balloons::Blue);
        p.burst(Balloons::Red);

        assert_eq!(false, p.has_lost());
        p.burst(Balloons::Red);
        assert_eq!(false, p.has_lost());
        p.burst(Balloons::Green);
        assert_eq!(true, p.has_lost());
    }
}
