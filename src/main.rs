
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

    println!("{:?}", p);
}
