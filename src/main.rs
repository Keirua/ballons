use std::collections::HashMap;

#[derive(Debug, PartialEq, Eq, Hash, Copy, Clone)]
enum Balloons {
	Red,
	Blue,
	Green,
	Violet,
	Yellow
}

#[derive(Debug, PartialEq, Eq, Hash, Copy, Clone)]
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
	ballons: HashMap<Balloons, usize>,
	returned_balloons: Vec<Balloons>
}

impl Player {
	pub fn new() -> Player {
		let mut p = Player {
			ballons: HashMap::new(),
			returned_balloons: Vec::new()
		};
		p.ballons.insert(Balloons::Red, 0);
		p.ballons.insert(Balloons::Blue, 0);
		p.ballons.insert(Balloons::Green, 0);
		p.ballons.insert(Balloons::Violet, 0);
		p.ballons.insert(Balloons::Yellow, 0);
		p
	}

	pub fn deal(&mut self, b: Balloons) {
		let count = self.ballons.entry(b).or_insert(0);
		*count += 1;
	}

	pub fn burst(&mut self, b: Balloons) {
		let count = self.ballons.entry(b).or_insert(0);
		if *count > 0 {
			*count -= 1;
			self.returned_balloons.push(b);
		}
	}
}

fn main() {
	let mut p = Player::new();
	p.deal(Balloons::Red);
	p.burst(Balloons::Blue);
	p.burst(Balloons::Red);

    println!("{:?}", p);
}
