extern crate rand;
mod game;
mod deck;
mod player;
mod ballons;
use game::BalloonGame;

fn main() {
    let mut balloon_game = BalloonGame::new(2, 5, 5);

    println!("{}", balloon_game.run_game());
}
