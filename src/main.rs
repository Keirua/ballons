extern crate rand;

mod ballons;
mod player;
use ballons::{Balloons, ActionCard};
use player::Player;



use rand::seq::SliceRandom;
use rand::thread_rng;

struct BalloonGame {
	nb_players: usize,
	nb_balloons_per_player: usize,
	nb_parent_cards: usize
}

impl BalloonGame {
	fn new(nb_players:usize, nb_balloons_per_player:usize, nb_parent_cards:usize) -> BalloonGame {
		let mut balloonGame = BalloonGame{
			nb_players,
			nb_parent_cards,
			nb_balloons_per_player
		};

		return balloonGame;
	}
}

#[derive(Debug)]
struct BalloonDeck {
	cards: Vec<Balloons>
}

#[derive(Debug)]
struct ActionDeck {
	cards: Vec<ActionCard>,
	nb_parent_cards: usize
}

impl BalloonDeck {
	pub fn new() -> BalloonDeck {
		let mut deck = BalloonDeck{
			cards: Vec::new()
		};
		deck.fill();

		deck
	}

	fn fill(&mut self) {
		for i in 0..5 {
			for c in &[Balloons::Red, Balloons::Yellow, Balloons::Blue, Balloons::Green, Balloons::Violet] {
				self.cards.push(*c);
			}
		}
	}
}

impl ActionDeck {
	pub fn new(nb_parent_cards:usize) -> ActionDeck {
		let mut deck = ActionDeck{
			cards: Vec::new(),
			nb_parent_cards: nb_parent_cards
		};
		deck.fill();

		deck
	}

	pub fn fill(&mut self) {
		for i in 0..5 {
			for c in &[ActionCard::Red, ActionCard::Yellow, ActionCard::Blue, ActionCard::Green, ActionCard::Violet] {
				self.cards.push(*c);
			}
		}
		for i in 0..self.nb_parent_cards {
			self.cards.push(ActionCard::Parent);
		}
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

	let balloonGame = BalloonGame::new(2, 5, 5);

	// let mut balloon_deck = create_balloon_deck();
	// let action_deck = create_action_deck(5);
	let action_deck = ActionDeck::new(5);
	let balloon_deck = BalloonDeck::new();
	
	// let mut rng = thread_rng();
	// balloon_deck.shuffle(&mut rng);
    println!("{:?}", p);
    // println!("{:?}", balloon_deck);
    println!("{:?}", action_deck);
}
