use std::collections::HashMap;

#[derive(Debug, PartialEq, Eq, Hash)]
enum Balloons {
	Red,
	Blue,
	Green,
	Violet,
	Yellow
}

#[derive(Debug, PartialEq, Eq, Hash)]
enum ActionCard {
	Red,
	Blue,
	Green,
	Violet,
	Yellow,
	Parent
}

#[derive(Debug)]
struct Player {
	ballons: HashMap<Balloons, usize>
}

impl Player {
	pub fn new() -> Player {
		let mut p = Player {
			ballons: HashMap::new()
		};
		p.ballons.insert(Balloons::Red, 0);
		p.ballons.insert(Balloons::Blue, 0);
		p.ballons.insert(Balloons::Green, 0);
		p.ballons.insert(Balloons::Violet, 0);
		p.ballons.insert(Balloons::Yellow, 0);
		p
	}
}

fn main() {
	let p = Player::new();

    println!("{:?}", p);
}
