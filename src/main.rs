extern crate rand;

mod ballons;
mod deck;
mod player;

use deck::{ActionDeck, BalloonDeck};
use player::Player;

use rand::rngs::ThreadRng;
use rand::thread_rng;

#[derive(Debug)]
struct BalloonGame {
    nb_players: usize,
    nb_balloons_per_player: usize,
    players: Vec<Player>,
    action_deck: ActionDeck,
    rng: ThreadRng,
}

impl BalloonGame {
    fn new(
        nb_players: usize,
        nb_parent_cards: usize,
        nb_balloons_per_player: usize,
    ) -> BalloonGame {
        let rng = thread_rng();

        let mut balloon_game = BalloonGame {
            nb_players,
            nb_balloons_per_player,
            players: Vec::with_capacity(nb_players),
            action_deck: ActionDeck::new(nb_parent_cards, rng),
            rng: rng,
        };

        for _ in 0..nb_players {
            balloon_game.players.push(Player::new());
        }
        balloon_game.action_deck.shuffle();

        return balloon_game;
    }

    pub fn deal_cards(&mut self) {
        let mut balloon_deck = BalloonDeck::new(self.rng);
        balloon_deck.shuffle();

        for p in 0..self.nb_players {
            for _ in 0..self.nb_balloons_per_player {
                if let Some(b) = balloon_deck.cards.pop() {
                    self.players[p].deal(b);
                }
            }
        }
    }

    pub fn run_game(&mut self) -> usize {
    	let mut nb_cards = 0;

    	
    	nb_cards
    }
}

fn main() {
    let mut p = Player::new();
    // p.deal(Balloons::Red);
    // p.deal(Balloons::Green);
    // p.deal(Balloons::Yellow);
    // p.burst(Balloons::Blue);
    // p.burst(Balloons::Red);

    // p.recover();
    // p.recover();
    // p.burst(Balloons::Yellow);

    let mut balloon_game = BalloonGame::new(2, 5, 5);
    balloon_game.deal_cards();

    println!("{}", balloon_game.run_game());
}
