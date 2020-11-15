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
	returned_balloons: Vec<Balloons>,
	nb_cards: usize
}

impl Player {
	pub fn new() -> Player {
		let mut p = Player {
			ballons: HashMap::new(),
			returned_balloons: Vec::new(),
			nb_cards: 0
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
		self.nb_cards += 1;
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

fn main() {
	let mut p = Player::new();
	p.deal(Balloons::Red);
	p.deal(Balloons::Green);
	p.deal(Balloons::Yellow);
	p.burst(Balloons::Blue);
	p.burst(Balloons::Red);

	p.recover();
	p.recover();
	p.burst(Balloons::Yellow);

    println!("{:?}", p);
}
