extern crate ballons;
use ballons::game::BalloonGame;
use std::collections::HashMap;

fn main() {
	let nb_games = 100;
	let mut frequencies:HashMap<usize, usize> = HashMap::new();

	for _ in 0..nb_games {
    	let mut balloon_game = BalloonGame::new(2, 5, 5);
    	let nb_cards = balloon_game.run_game();

    	let entry = frequencies.entry(nb_cards).or_insert(0);
    	*entry += 1;
	}

    println!("{:?}", frequencies);
}
