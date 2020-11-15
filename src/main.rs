extern crate rand;
mod ballons;
mod deck;
mod game;
mod player;
use game::BalloonGame;

fn main() {
    let mut balloon_game = BalloonGame::new(2, 5, 5);

    println!("{}", balloon_game.run_game());
}
