extern crate ballons;
use ballons::game::BalloonGame;

fn main() {
    let mut balloon_game = BalloonGame::new(2, 5, 5);

    println!("{}", balloon_game.run_game());
}
