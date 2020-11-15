
mod ballons;
mod player;
use ballons::{Balloons, ActionCard};
use player::Player;

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

pub fn create_balloon_deck() -> Vec<Balloons> {
	let mut deck:Vec<Balloons> = Vec::new();
	for i in 0..5 {
		for c in &[Balloons::Red, Balloons::Yellow, Balloons::Blue, Balloons::Green, Balloons::Violet] {
			deck.push(*c);
		}
	}

	deck
}

pub fn create_action_deck(nb_parent_cards:usize) -> Vec<ActionCard> {
	let mut deck:Vec<ActionCard> = Vec::new();
	for i in 0..5 {
		for c in &[ActionCard::Red, ActionCard::Yellow, ActionCard::Blue, ActionCard::Green, ActionCard::Violet] {
			deck.push(*c);
		}
	}
	for i in 0..nb_parent_cards {
		deck.push(ActionCard::Parent);
	}

	deck
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

	let balloon_deck = create_balloon_deck();
	let action_deck = create_action_deck(5);
    println!("{:?}", p);
    println!("{:?}", balloon_deck);
    println!("{:?}", action_deck);
}
